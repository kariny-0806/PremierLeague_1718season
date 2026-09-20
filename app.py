from pathlib import Path
import pandas as pd
import streamlit as st

from src.data_utils import load_data, filter_by_team

st.set_page_config(
    page_title="Premier League 2017-18 Dashboard",
    layout = "wide"
)

DATA_PATH = Path(__file__).parent / "data" / "raw" /"season-1718_csv.csv"

@st.cache_data
def get_data(path: Path) -> pd.DataFrame:
    """Cached wrapper around load_data to prevent redundant disk reads."""
    return load_data(path)

# Load master dataset
df = get_data(DATA_PATH)


# Team Selection sidebat
st.sidebar.header("Navigation")

all_teams = sorted(df["HomeTeam"].unique())
selected_team = st.sidebar.selectbox("Select a Team", options=all_teams)

team_df = filter_by_team(df, selected_team)


# Metric calculations (vectorized)
is_home = team_df["HomeTeam"] == selected_team

# goals
gf = team_df["FTHG"].where(is_home, team_df["FTAG"])
ga = team_df["FTAG"].where(is_home, team_df["FTHG"])

# Results
wins = ((is_home & (team_df["FTR"] == "H")) | (~is_home & (team_df["FTR"] == "A"))).sum()
draws = (team_df["FTR"] == "D").sum()
losses = len(team_df) - wins - draws
points = (wins * 3) + draws

# Display KPIs
st.subheader(f"Season Summary: {selected_team}")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Matches", len(team_df))
col2.metric("Wins", int(wins))
col3.metric("Draws", int(draws))
col4.metric("Losses", int(losses))
col5.metric("Points", int(points), delta=f"{int(gf.sum() - ga.sum())} GD")

# Charts and Data Table
st.subheader("Goals Trend")
trend_df = pd.DataFrame({
    "Goals Scored": gf.values,
    "Goals Conceded": ga.values
}, index=range(1, len(team_df) + 1))

trend_df["Cumulative Scored"] = trend_df["Goals Scored"].cumsum()
trend_df["Cumulative Conceded"] = trend_df["Goals Conceded"].cumsum()

st.line_chart(trend_df[["Cumulative Scored", "Cumulative Conceded"]])

# Toggle raw match logs
if st.checkbox("Show match logs"):
    st.subheader(f"Matches for {selected_team}")
    display_cols = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]
    st.dataframe(team_df[[c for c in display_cols if c in team_df.columns]])
