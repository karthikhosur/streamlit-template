import streamlit as st
from data.db import get_agent_full_names,assign_agent_team
import pandas as pd
def app():
    team_list = ['Team 1','Team 2','Team 3']
    df = get_agent_full_names()
    agent_name = st.selectbox("Select Agent",df)
    new_team = st.selectbox("Select Team",team_list)
    if st.button("Assign Agent"):
        assign_agent_team(agent_name,new_team)
        st.write("Agent Assigned")