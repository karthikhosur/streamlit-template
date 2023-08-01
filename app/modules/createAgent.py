import streamlit as st
from data.db import create_agent
def app():
    options = ['Rapid City', 'Dallas', 'Faneuil', 'OKC', 'Deerfield Beach', 'Senture', 'MCI BPO', 'ME Special Projects',
               'ME Customer Service', 'NetOps', 'QA-Training-Admin']

    # Create a dictionary to store the form responses
    form_responses = {
        'Location': st.selectbox('Select Location', options, index=0),
        'Full Name': st.text_input('Full Name', value=''),
        'First Name': st.text_input('First Name', value=''),
        'Last Name': st.text_input('Last Name', value=''),
        'Team': st.text_input('Team', value=''),
        'Role': st.text_input('Role', value=''),
        'Manager': st.text_input('Manager', value=''),
        'Manager Email': st.text_input('Manager Email', value=''),
        'Employment Status': st.selectbox('Employment Status', ['Active', 'Inactive'], index=0),
        'Hire Date': st.date_input('Hire Date', value=None),
        'Term Date': st.date_input('Term Date', value=None),
        'Email': st.text_input('Email', value=''),
        'Alternate Email': st.text_input('Alternate Email', value=''),
        'Position ID': st.text_input('Position ID', value=''),
        'Five9 Station ID': st.text_input('Five9 Station ID', value=''),
        'TCPA Username': st.text_input('TCPA Username', value=''),
        'TCPA Station ID': st.text_input('TCPA Station ID', value=''),
        'Status 02': st.selectbox('Status 02', ['Full-Time', 'Part-Time'], index=0),
        'Sr. Manager': st.text_input('Sr. Manager', value=''),
        'Spanish Bilingual': st.checkbox('Spanish Bilingual'),
    }

    # Calculate the percentage of form fields filled
    form_fields_filled = sum([1 for field in form_responses.values() if field])
    total_form_fields = len(form_responses)
    percentage_filled = int((form_fields_filled / total_form_fields) * 100)

    # Display the progress bar
    st.sidebar.subheader('Completed : ')
    st.sidebar.progress(percentage_filled)

    # Submit button
    submit_button = st.button('Submit')

    # Form submission handling
    if submit_button:
        # Perform necessary actions with the form data
        # You can access the values of the form inputs through the form_responses dictionary
        # Example: st.writeing the values
        for key, value in form_responses.items():
            st.write(f'{key}: {value}')
        form_responses_dict = dict(form_responses.items())
        
        create_agent(form_responses_dict)
    
