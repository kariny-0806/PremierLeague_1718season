# Premier League 2017–18 Dashboard

A Streamlit dashboard for exploring Premier League 2017–18 match results by team.

The application displays team KPIs (wins, draws, losses, points, and goal difference), cumulative goal trends, and match-level results. It is tested with pytest, containerized with Docker, and checked automatically with GitHub Actions.

## Project structure

```text
PremierLeague_1718season/
├── .github/workflows/ci.yml
├── data/raw/season-1718_csv.csv # local only; ignored by Git
├── src/
│   └── data_utils.py
├── tests/
│   └── test_data_utils.py
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Local setup

```bash
git clone https://github.com/kariny-0806/PremierLeague_1718season.git
cd PremierLeague_1718season
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run tests

```bash
python -m pytest -v
```

The project contains four pytest unit tests for the data-loading and team-filtering functions.

## Run locally

```bash
streamlit run app.py
```

Open the dashboard at:

```text
http://localhost:8501
```

## Data note

The application uses:

```text
data/raw/season-1718_csv.csv
```

This raw dataset is gitignored and is therefore not included in a fresh Git clone. To run the project from source or build the image locally, place the CSV at the path above.

The Docker Hub image already contains the dataset and can be run directly without manually adding the CSV.

## Docker

Build locally:

```bash
docker build -t premierleague1718:latest .
```

Run the local image:

```bash
docker run --rm -p 8501:8501 premierleague1718:latest
```

Then open:

```text
http://localhost:8501
```

## Docker Hub

Published image:

```text
karinondocker/premierleague1718:latest
```

Pull and run it:

```bash
docker pull karinondocker/premierleague1718:latest
docker run --rm -p 8501:8501 karinondocker/premierleague1718:latest
```

Docker Hub repository: [karinondocker/premierleague1718](https://hub.docker.com/r/karinondocker/premierleague1718)

## CI/CD

GitHub Actions runs the pytest test suite automatically on every push and pull request.

Workflow file:

```text
.github/workflows/ci.yml
```

## Author

Karin Y

## AI Usage Disclosure

Generative AI tools (Perplexity) were utilized during the development of this project in a pair-programming and technical advisory capacity.

### Scope of Assistance
- **Architecture & Planning:** Outlining a phased implementation strategy to meet assignment milestones.
- **Workflow & DevOps Boilerplate:** Assisting with syntax and best practices for GitHub Actions (`ci.yml`) and container configuration (`Dockerfile`, `.dockerignore`).
- **Debugging & Troubleshooting:** Diagnosing local test runners, port allocation conflicts, and import structures.

### Human Oversight & Verification
All application code, data transformations, unit test designs, and container builds were reviewed, executed, manually verified, and committed by the author. The author made the final implementation and project-scope decisions.