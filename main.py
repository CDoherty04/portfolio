import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    portrait = st.image("images\\charlie.png", width=500)

with col2:
    content = ("I am an aspiring software engineer teaching myself development in VR, Blockchain, and other interesting"
               " fields while taking classes at KU.")
    st.title("Charlie Doherty")
    st.info(content)

content2 = ("Below you can find some of the projects I have created and/or am working on."
            " Feel free to contact me about any of them!")
st.write(content2)

st.markdown("***")

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images\\" + row["image"])
        st.subheader(row["description"])
        st.info(row["url"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image("images\\" + row["image"])
        st.subheader(row["description"])
        st.info(row["url"])

