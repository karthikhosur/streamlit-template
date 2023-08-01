import streamlit as st
from multiapp import MultiApp
from modules import home, about, createAgent  # Import your custom page modules here

app = MultiApp()

# Add all the pages to the app using their respective function names
app.add_app("Home", home.app)
app.add_app("About", about.app)
app.add_app("Create Agent", createAgent.app)

app.run()
