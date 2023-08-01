from snowflake.snowpark import Session
import snowflake.snowpark as snowpark
import streamlit as st
from .utils import connection_parameters

session = Session.builder.configs(connection_parameters).create()


def create_agent( form_responses: dict):
    session.sql("USE ROLE ACCOUNTADMIN")
    session.sql("SELECT * FROM MEC_DATA").show()
    st.write("Session Used")
    # print()
#     session.sql('''INSERT INTO MEC_DATA (
#     FULL_NAME,
#     FIRST_NAME,
#     LAST_NAME,
#     LOCATION,
#     TEAM,
#     MANAGER,
#     MANAGER_EMAIL,
#     EMPLOYMENT_STATUS,
#     HIRE_DATE,
#     TERMINATION_DATE,
#     EMAIL,
#     POSITION_ID,
#     FIVE9_STATION_ID,
#     FILENAME,
#     ALT_EMAIL,
#     STATUS_02,
#     ROLE,
#     SR_MANAGER,
#     DBT_SCD_ID,
#     DBT_UPDATED_AT,
#     DBT_VALID_FROM,
#     DBT_VALID_TO
# )
# VALUES
# (
#     'John Doe',
#     'John',
#     'Doe',
#     'New York',
#     'Sales',
#     'Jane Smith',
#     'jane.smith@example.com',
#     'Active',
#     '2023-07-27 12:00:00',
#     '2023-07-27 13:30:00',
#     'john.doe@example.com',
#     'POS123',
#     '5001',
#     'file.csv',
#     'john_alt@example.com',
#     'Active',
#     'Sales Rep',
#     'Bob Johnson',
#     'SCD123',
#     '2023-07-27 13:30:00',
#     '2023-07-27 13:30:00',
#     '2023-07-27 13:30:00'
#     )''')
     

    sql_query = f'''INSERT INTO MEC_DATA (
            FULL_NAME,
            FIRST_NAME,
            LAST_NAME,
            LOCATION,
            TEAM,
            MANAGER,
            MANAGER_EMAIL,
            EMPLOYMENT_STATUS,
            HIRE_DATE,
            TERMINATION_DATE,
            EMAIL,
            POSITION_ID,
            FIVE9_STATION_ID,
            FILENAME,
            ALT_EMAIL,
            STATUS_02,
            ROLE,
            SR_MANAGER,
            DBT_SCD_ID,
            DBT_UPDATED_AT,
            DBT_VALID_FROM,
            DBT_VALID_TO
        )
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
    print(sql_query)
    session.sql(sql_query)
    # session.sql(sql_query)
    # session.close() 
    