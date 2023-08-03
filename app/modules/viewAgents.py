import streamlit as st
from data.db import all_agents
import pandas as pd

def app():
    df = all_agents()
    locations = ["All"]
    for i in df:
        locations.append(i['LOCATION'])
    locations = list(set(locations))
    selected_location = st.selectbox("Select Location",locations)
    display_df = []
    for i in df:
        if selected_location == "All":
            display_df = df
            break
        elif selected_location == i['LOCATION']:
            display_df.append(i)

    st.table(display_df)
