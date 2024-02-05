import streamlit as st
st.set_page_config(page_title="Charlie Doherty")

with st.form(key="email_form"):
    st.text_input("Enter Email", placeholder="your_email@gmail.com")
    st.text_area("Enter Message", placeholder="I'd like to set up an interview with you!")
    st.form_submit_button("Submit")
