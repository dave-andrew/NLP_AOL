import streamlit as st

st.set_page_config(
    page_title="Data and Preprocessing",
)
st.title('Data and Preprocessing')

st.subheader('Dataset')
st.components.v1.iframe("https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv", height=400, scrolling=True)

st.subheader('Preprocessing')