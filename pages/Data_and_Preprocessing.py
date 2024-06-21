import streamlit as st

st.set_page_config(
    page_title="Data and Preprocessing",
)
st.title('Data and Preprocessing')

st.subheader('Dataset')
st.markdown(
  '''Dataset yang digunakan diambil dari Kaggle untuk mengklasifikasikan apakah suatu teks merupakan hate-speech atau non-hate-speech. Link dataset: https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv'''
)
st.image('dataset_1.png')
st.image('dataset_2.png')

# st.components.v1.iframe("https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv", height=400, scrolling=True)

st.subheader('Preprocessing')