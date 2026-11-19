# Sunward — Energy Loss & Financial Impact Dashboard

Student 3: Prashant Banjade (@banjadecodes), Alabama A&M University.
Part of the [Net Zero Solar Portal](https://netzero-solar-portal.vercel.app).

A Python/Streamlit demonstration for exploring energy shortfalls, maintenance costs,
and the estimated cost of waiting. The app opens with 96 synthetic panels; no uploads,
API keys, private datasets, or database service are required to start.

## Run locally

Use Python 3.13.

```sh
git clone https://github.com/banjadecodes/netzero-energy-loss.git
cd netzero-energy-loss
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

At https://share.streamlit.io, sign in with GitHub and create an app using:

| Setting | Value |
|---|---|
| Repository | `banjadecodes/netzero-energy-loss` |
| Branch | `main` |
| Main file | `app.py` |
| Python version | `3.13` |
| Secrets | None required |

Deploy and copy the resulting public app URL to the project manager for the portal's
live-demo link. This repository contains the app code; pushing it does not deploy it
or create a live URL automatically.

## Demonstration flow

1. **Overview:** inspect the synthetic farm, urgent findings, and partial energy-loss estimate.
2. **Findings:** search/filter panels and review the selected panel's scenario.
3. **Decisions:** change electricity price, monthly loss growth, replacement cost, or wait time.
4. **Work orders:** filter the ranked queue and download CSV.
5. **Scenario library:** save and reopen current assumptions; download JSON for a portable copy.
6. **Energy & SCADA:** use packaged synthetic examples or upload interval energy/meter CSVs.
7. **Assumptions / Fall dashboard / Maintenance options:** edit, save, reopen, and export the supported input scenarios.

The app sidebar includes **Download synthetic sample files**. Choose a workspace to
download its clearly named sample bundle, or download all workspace samples and the
upload guide in one zip. The [upload guide](sample-inputs/UPLOAD-GUIDE.md) lists the
matching files and explains which workspaces accept uploads. Overview, Findings,
Decisions, and Work orders use built-in synthetic data; their sample/export CSVs are
not supported as uploads on those screens yet.

## Scope and limitations

- All panel observations and timelines are synthetic scenarios, not drone-image diagnoses or validated failure predictions.
- A high-loss threshold is a planning marker, not a predicted failure date.
- Missing expected generation remains unavailable. Missing panel inputs are excluded from partial aggregate estimates.
- Inverter-only measurements do not establish per-panel financial losses or fault causation.
- Maintenance comparisons and forecasts are simplified estimates, not verified savings or engineering recommendations.
- The SQLite scenario library lives on the app server, is shared between visitors, and may reset during redeployment. Use synthetic names and download important scenarios. There are no user accounts or access controls.
- No original site exports, local databases, credentials, historical reports, or machine-specific Downloads dependencies are included.

## Verification

```sh
python -m unittest -v
python verify_dashboard.py
python verify_maintenance.py
```

`requirements.txt` records the direct runtime dependencies used for this release.
The portal is a separate website; this app runs as its own Python server.
