import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Charlie Doherty")

with st.form(key="email_form"):
    email = st.text_input("Enter Email", placeholder="your_email@gmail.com", key="email_area")
    message = st.text_area("Enter Message", placeholder="Hi, I'd like to connect with you!", key="message_area")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: Email From Portfolio Webapp
{message}

From: {email}
"""
    if button:
        send_email(f"{message}")
        st.info("Your email was sent successfully!")
