from snowflake.snowpark import Session
import snowflake.snowpark as snowpark
import streamlit as st
from .utils import connection_parameters
from snowflake.snowpark.functions import col
import pandas as pd
session = Session.builder.configs(connection_parameters).create()


def create_agent( form_responses: dict):
    session.sql("USE ROLE ACCOUNTADMIN")
    session.sql("SELECT * FROM MEC_DATA").show()
    st.write("Session Used")

    sql_query = f'''INSERT INTO MEC_DATA 
        VALUES
        (
            '{form_responses["Full Name"]}',
            '{form_responses["First Name"]}',
            '{form_responses["Last Name"]}',
            '{form_responses["Location"]}',
            '{form_responses["Team"]}',
            '{form_responses["Manager"]}',
            '{form_responses["Manager Email"]}',
            '{form_responses["Employment Status"]}',
            '{form_responses["Hire Date"]}',
            '{form_responses["Term Date"]}',
            '{form_responses["Email"]}',
            '{form_responses["Position ID"]}',
            '{form_responses["Five9 Station ID"]}',
            'file.csv',
            '{form_responses["Alternate Email"]}',
            '{form_responses["Status 02"]}',
            '{form_responses["Role"]}',
            '{form_responses["Sr. Manager"]}',
            'SCD123',
            '2023-07-27 13:30:00',
            '2023-07-27 13:30:00',
            '2023-07-27 13:30:00'
        )'''
    # print(sql_query)
    session.sql(str(sql_query)).collect()
        
    
    # session.sql(sql_query)
    # session.close() 
    
def get_agent_full_names():
    df = session.table("MEC_DATA").select(col("FULL_NAME"))
    return df

def assign_agent_team(agent_name,team_name):
    session.sql(f"UPDATE MEC_DATA SET TEAM = '{team_name}' WHERE FULL_NAME = '{agent_name}'").collect()
    
def all_agents():
    df = session.sql("SELECT * FROM MEC_DATA").collect()
    return df