"""Build clearly labeled, workspace-specific synthetic sample downloads."""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


SAMPLE_ROOT = Path(__file__).parent / "sample-inputs"

WORKSPACE_SAMPLES: dict[str, dict[str, object]] = {
    "Overview": {
        "files": ["01-farm-overview/UPLOAD-Farm-overview-synthetic-findings.csv"],
        "note": "Example findings file/schema. Overview currently loads its built-in synthetic farm data; CSV import is not enabled here yet.",
    },
    "Findings": {
        "files": ["02-findings/UPLOAD-Findings-synthetic-panel-findings.csv"],
        "note": "Example panel findings file/schema. Findings currently uses built-in synthetic data; CSV import is not enabled here yet.",
    },
    "Decisions": {
        "files": [],
        "note": "No upload is needed. Change the on-screen controls to explore act-now versus wait scenarios.",
    },
    "Work orders": {
        "files": ["04-work-orders/UPLOAD-Work-orders-synthetic-ranked-worklist.csv"],
        "note": "Example ranked worklist/export schema. Work orders currently generates its own list; CSV import is not enabled here yet.",
    },
    "Energy scenarios": {
        "files": [
            "05-energy-scada/UPLOAD-Energy-actual-intervals.csv",
            "05-energy-scada/UPLOAD-Energy-expected-baseline.csv",
        ],
        "note": "Upload both files together in Energy & SCADA → Energy scenarios. They are a matched actual/expected pair.",
    },
    "SCADA review": {
        "files": [
            "05-energy-scada/UPLOAD-SCADA-synthetic-meter-part-1.csv",
            "05-energy-scada/UPLOAD-SCADA-synthetic-meter-part-2.csv",
        ],
        "note": "Upload both parts together in Energy & SCADA → SCADA review. They represent one synthetic meter and include a deliberate timestamp gap.",
    },
    "Assumptions": {
        "files": ["06-assumptions/UPLOAD-Assumptions-costs.csv"],
        "note": "Upload this CSV in Assumptions to edit and validate example costs and tariff assumptions.",
    },
    "Fall dashboard": {
        "files": ["07-scenario-library/UPLOAD-Fall-dashboard-complete-scenario.json"],
        "note": "Upload this JSON in Fall dashboard. It includes sample energy data and editable costs.",
    },
    "Maintenance options": {
        "files": ["03-decisions/UPLOAD-Maintenance-options-scenario.json"],
        "note": "Upload this JSON in Maintenance options to compare inspect, clean, repair, replace, and wait.",
    },
    "Scenario library": {
        "files": [
            "07-scenario-library/UPLOAD-Scenario-library-Fall-example.json",
            "07-scenario-library/UPLOAD-Scenario-library-maintenance-example.json",
        ],
        "note": "Download the examples for reference. Open each from its matching workspace; the library does not yet import these examples directly.",
    },
}


def _make_zip(files: list[str], *, include_guide: bool = False) -> bytes:
    buffer = BytesIO()
    with ZipFile(buffer, "w", ZIP_DEFLATED) as archive:
        for relative_path in files:
            path = SAMPLE_ROOT / relative_path
            archive.write(path, arcname=relative_path)
        if include_guide:
            guide = SAMPLE_ROOT / "UPLOAD-GUIDE.md"
            archive.write(guide, arcname="UPLOAD-GUIDE.md")
    return buffer.getvalue()


def all_samples_zip() -> bytes:
    files = sorted(
        path.relative_to(SAMPLE_ROOT).as_posix()
        for path in SAMPLE_ROOT.rglob("*")
        if path.is_file() and path.name != "UPLOAD-GUIDE.md"
    )
    return _make_zip(files, include_guide=True)


def workspace_zip(workspace: str) -> bytes | None:
    files = WORKSPACE_SAMPLES[workspace]["files"]
    if not files:
        return None
    return _make_zip(files)


def render_sidebar_downloads(st: object) -> None:
    """Render beginner-friendly download controls in the Streamlit sidebar."""
    with st.expander("Download synthetic sample files", expanded=False):
        st.caption("Practice data only — these are not real farm measurements.")
        st.download_button(
            "Download all samples + guide (.zip)",
            data=all_samples_zip(),
            file_name="Sunward-synthetic-samples-by-workspace.zip",
            mime="application/zip",
            use_container_width=True,
        )
        st.divider()
        workspace = st.selectbox(
            "Choose the workspace you need a file for",
            list(WORKSPACE_SAMPLES),
            key="sample_download_workspace",
        )
        details = WORKSPACE_SAMPLES[workspace]
        st.caption(details["note"])
        data = workspace_zip(workspace)
        if data is not None:
            slug = workspace.lower().replace(" ", "-").replace("&", "and")
            st.download_button(
                f"Download {workspace} sample(s)",
                data=data,
                file_name=f"Sunward-{slug}-synthetic-sample.zip",
                mime="application/zip",
                key=f"download_{slug}_samples",
                use_container_width=True,
            )
