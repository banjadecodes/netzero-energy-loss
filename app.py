"""Solar Operations Console — Streamlit application entry point."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title='Solar Operations Console', page_icon='☼', layout='wide', initial_sidebar_state='expanded')

from ui_components import inject_theme
inject_theme()
from sample_downloads import render_sidebar_downloads
from scenario_library import DEFAULTS
for scenario_key, default in DEFAULTS.items():
    st.session_state[scenario_key] = st.session_state.get(scenario_key, default)

with st.sidebar:
    st.markdown('<div class="console-kicker">Student 3 · Solar operations</div>', unsafe_allow_html=True)
    st.markdown('## Sunward')
    st.caption('Maintenance & energy decisions')
    st.markdown('<span class="status-pill">● SYNTHETIC DEMO</span>', unsafe_allow_html=True)
    st.markdown('')
    destinations = {
        'Overview': 'Overview',
        'Findings': 'Findings',
        'Decisions': 'Decisions',
        'Work orders': 'Work orders',
        'Energy & SCADA': 'Energy & SCADA',
        'Assumptions': 'Assumptions',
        'Maintenance options': 'Maintenance options',
        'Scenario library': 'Scenario library',
        'Fall dashboard': 'Fall dashboard',
    }
    page = st.radio('WORKSPACE', list(destinations), key='console_page', label_visibility='visible')
    st.divider()
    st.caption('DEMO SITE')
    st.caption('North Field · 96 synthetic panels')
    if st.button('↻ Reset demo view', use_container_width=True, help='Restore default synthetic assumptions and panel selection'):
        for key in ['farm_tariff','farm_persist','farm_replace','farm_wait','farm_panel','find_search','find_severity','find_fault','find_inverter']:
            st.session_state.pop(key, None)
        st.rerun()
    render_sidebar_downloads(st)
    st.markdown('<div class="muted-small">All panel findings and scenarios are illustrative synthetic examples.</div>', unsafe_allow_html=True)


if page == 'Overview':
    from farm_page import render_overview
    render_overview()
elif page == 'Findings':
    from farm_page import render_findings
    render_findings()
elif page == 'Decisions':
    from farm_page import render_decisions
    render_decisions()
elif page == 'Work orders':
    from farm_page import render_work_orders
    render_work_orders()
elif page == 'Energy & SCADA':
    page2 = st.segmented_control('Workspace', ['Energy scenarios', 'SCADA review'], default='Energy scenarios', key='energy_scada_subpage')
    if page2 == 'SCADA review':
        from scada_page import render
    else:
        from energy_page import render
    render()
elif page == 'Assumptions':
    st.title('Operating assumptions')
    st.caption('Edit rates, costs, source descriptions, and assumption flags. Unknown values must remain blank.')
    uploaded = st.file_uploader('Open a saved assumptions CSV', type='csv')
    raw = uploaded.getvalue() if uploaded else Path(__file__).with_name('sample-assumptions.csv').read_bytes()
    try:
        from assumptions import loads, dumps, validate
        rows = loads(raw.decode('utf-8-sig'))
    except (ValueError, UnicodeError) as exc:
        st.error(str(exc)); st.stop()
    st.info('Starting values are illustrative. Replace them with approved values when available.')
    edited = st.data_editor(rows, num_rows='fixed', disabled=['parameter','unit'], key='assumptions_editor')
    errors = validate(edited)
    if errors:
        for error in errors: st.error(error)
    else:
        st.success('Inputs are valid. Download and reopen this file to restore the scenario.')
        st.download_button('Save assumptions CSV', dumps(edited), 'cost-assumptions.csv', 'text/csv', type='primary')
elif page == 'Scenario library':
    from scenario_library import render
    render()
elif page == 'Fall dashboard':
    from dashboard_page import render
    render()
elif page == 'Maintenance options':
    from maintenance_page import render
    render()

