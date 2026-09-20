from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"}


def load_data(csv_path: str | Path) -> pd.DataFrame:
    """Load EPL match dataset and validate mandatory columns."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df


def filter_by_team(df: pd.DataFrame, team: str) -> pd.DataFrame:
    """Filter rows where the team played as either Home or Away."""
    mask = (df["HomeTeam"] == team) | (df["AwayTeam"] == team)
    return df.loc[mask].copy()