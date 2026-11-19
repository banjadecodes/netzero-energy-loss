# Upload guide — synthetic demonstration files

All files in this folder are synthetic training/demo inputs. Do not treat their values as site measurements or approved costs.

## Download samples from the dashboard

Open the app's left sidebar and expand **Download synthetic sample files**. Choose **Download all samples + guide (.zip)** to get every workspace folder, or select a workspace to download only its sample file(s). The zip names and folders match the workspace names below. Each sample filename also starts with `UPLOAD-<workspace>-` so it is easy to recognize.

Some workspaces show sample/export formats for demonstration; they do not currently accept uploads. The notes below state exactly where upload works.

| In-app workspace | File to use | Upload control / notes |
|---|---|---|
| **Overview** | `01-farm-overview/UPLOAD-Farm-overview-synthetic-findings.csv` | The current Overview is generated deterministically and does not import this CSV yet. Use the file as the panel findings export/sample schema. |
| **Findings** | `02-findings/UPLOAD-Findings-synthetic-panel-findings.csv` | Current Findings filters the generated demonstration set; upload support is not connected yet. This CSV shows the intended panel finding fields. |
| **Decisions** | Use sidebar controls | Synthetic panel scenarios are generated in app. `03-decisions/UPLOAD-Maintenance-options-scenario.json` is for the dedicated **Maintenance options** workspace, which contains editable action costs. |
| **Work orders** | `04-work-orders/UPLOAD-Work-orders-synthetic-ranked-worklist.csv` | Current Work orders exports its ranked list; importing an edited work-order CSV is not enabled yet. |
| **Energy & SCADA → Energy scenarios** | Upload both `05-energy-scada/UPLOAD-Energy-actual-intervals.csv` and `05-energy-scada/UPLOAD-Energy-expected-baseline.csv` | Select the upload interval CSVs option and load actual plus expected as a matched pair. A checkbox can also load the original packaged examples. |
| **Energy & SCADA → SCADA review** | Upload both `05-energy-scada/UPLOAD-SCADA-synthetic-meter-part-1.csv` and `05-energy-scada/UPLOAD-SCADA-synthetic-meter-part-2.csv` | Upload together as exports for the same synthetic meter; choose a 5-minute cadence. A timestamp gap is deliberately included for the coverage visualization. |
| **Assumptions** | `06-assumptions/UPLOAD-Assumptions-costs.csv` | Upload the CSV in the assumptions page to edit, validate, download, and reopen cost assumptions. |
| **Fall dashboard** | `07-scenario-library/UPLOAD-Fall-dashboard-complete-scenario.json` | Upload as the complete scenario JSON; it includes synthetic actual/expected energy and editable costs. |
| **Maintenance options** | `03-decisions/UPLOAD-Maintenance-options-scenario.json` | Upload as maintenance scenario JSON; demonstrates inspect/clean/repair/replace/wait and a missing replacement downtime value. |
| **Scenario library** | `07-scenario-library/UPLOAD-Scenario-library-Fall-example.json` or `UPLOAD-Scenario-library-maintenance-example.json` | Scenario library currently documents the examples. Open each from its matching workspace. Unified import/compare is not implemented yet. |

## Naming convention

`UPLOAD-<workspace>-<data-purpose>.<extension>` identifies a file intended for a workspace. The number prefix groups folders in the order used during a presentation. The Overview/Findings/Work orders CSVs are clearly labeled sample/export schemas until import controls are implemented for those pages.

## Quick demonstration order

1. Open **Overview** and point out the synthetic label and generated farm schematic.
2. Open **Findings** and filter a fault type; select a panel to see its detail and time/cost scenario.
3. Open **Decisions**, change tariff or wait interval, and explain the act-versus-wait comparison.
4. Open **Work orders** and download the ranked queue.
5. Open **Energy & SCADA → Energy scenarios**, upload the actual and expected pair.
6. Open **Energy & SCADA → SCADA review**, upload both meter parts together and explain the deliberate gap.
7. Open **Assumptions** and upload the assumptions CSV.
8. Open **Fall dashboard** and upload the complete scenario JSON.
9. Open **Maintenance options** and upload the maintenance JSON.

