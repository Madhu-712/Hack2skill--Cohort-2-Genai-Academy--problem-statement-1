import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="IntelliTravel Nexus", layout="wide", page_icon="🌐")

# --- Persona Configuration ---
PERSONA_DATA = {
    "Traveler": {"icon": "✈️", "prompt": "Find me the best rated hotels in Paris for under $200."},
    "Hospitality Provider": {"icon": "🏨", "prompt": "Show me occupancy trends for Q3 compared to last year."},
    "Government Planner": {"icon": "🏛️", "prompt": "Provide a summary of tourism impact on infrastructure by region."}
}

# --- Sidebar Persona Selection ---
with st.sidebar:
    st.title("IntelliTravel Nexus")
    selected_role = st.radio("Select your persona:", list(PERSONA_DATA.keys()))
    role_info = PERSONA_DATA[selected_role]
    st.info(f"Viewing as: **{selected_role}** {role_info['icon']}")
    
    st.markdown("### Suggested Query")
    st.code(role_info['prompt'], language="text")

# --- Main Interface ---
st.title(f"{role_info['icon']} {selected_role} Dashboard")
st.markdown("---")

# Embedding the Agent
AGENT_URL = "https://lookerstudio.google.com/conversation?agent=projects/notebooklm-491108/locations/us/dataAgents/agent_3ef6798f-065b-41d4-99c9-1a984d8d2076"

# Wrap iframe in a clean container
with st.container(border=True):
    components.iframe(AGENT_URL, height=650, scrolling=True)

st.caption("Powered by BigQuery Data Agents")