import pandas as pd
import pytest
from src.data_utils import filter_by_team, load_data

@pytest.fixture
def sample_csv(tmp_path):
    """Temporary 4-row CSV with both home and away matches."""
    data = """Div,Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR
E0,11/08/17,Arsenal,Leicester,4,3,H
E0,12/08/17,Brighton,Man City,0,2,A
E0,12/08/17,Chelsea,Burnley,2,3,A
E0,19/08/17,Stoke,Arsenal,1,0,H
"""
    file_path = tmp_path / "sample_epl.csv"
    file_path.write_text(data)
    return file_path


def test_load_data_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_load_data_missing_columns(tmp_path):
    invalid_data = "HomeTeam,AwayTeam\nArsenal,Chelsea\n"
    file_path = tmp_path / "invalid_data.csv"
    file_path.write_text(invalid_data)

    with pytest.raises(ValueError):
        load_data(file_path)

def test_load_data_success(sample_csv):
    df = load_data(sample_csv)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) >= {"HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"}

def test_filter_by_team(sample_csv):
    df = load_data(sample_csv)
    filtered_df = filter_by_team(df, "Arsenal")
    assert len(filtered_df) == 2
    assert all((filtered_df["HomeTeam"] == "Arsenal") | (filtered_df["AwayTeam"] == "Arsenal"))

