import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

st.title(f"Welcome Recruiter, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View your notes', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Recruiter_Notes.py')

if st.button('Add new notes', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_New_RecNotes.py')

if st.button('View applicants', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Applicant_Data.py')

if st.button("What's new on the market?",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_New_Job_Trend.py')