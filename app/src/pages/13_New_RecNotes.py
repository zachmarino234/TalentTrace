import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import datetime
import json

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

# set the header of the page
st.header('Add New Interview Record')




with st.form("Add New Note"):
    job_ID = st.number_input("Job ID", placeholder="Enter ID", label_visibility="visible", step = 1, format = "%d")
    app_ID = st.number_input("App ID", placeholder="Enter ID", label_visibility="visible", step = 1, format = "%d")
    recruiter_ID = st.number_input("recruiterID", placeholder="Enter ID", label_visibility="visible", step = 1, format = "%d")
    date = st.date_input('Interview Date')
    datetime_obj = datetime.datetime.combine(date, datetime.datetime.min.time())
    datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    
    
    added_note = st.form_submit_button("Add New Interview Record")

    if added_note:

        recruiternote = {}
        recruiternote['jobID'] = job_ID
        recruiternote['appID'] = app_ID
        recruiternote['recruiterID'] = recruiter_ID
        recruiternote['date']= datetime_str
        

        response = requests.post('http://api:4000/rn/recruiterNotes', json = recruiternote)

        if response.status_code == 200:
            st.toast('Success')
        else:
            st.toast('Failed - Please try again')

