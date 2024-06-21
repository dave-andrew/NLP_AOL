import streamlit as st

st.set_page_config(
    page_title="Data and Preprocessing",
)
st.title('Data and Preprocessing')

st.subheader('Dataset')
st.markdown(
  '''Dataset yang digunakan diambil dari Kaggle untuk mengklasifikasikan apakah suatu teks merupakan hate-speech atau non-hate-speech.
  
  Link dataset: https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv'''
)
st.image('dataset_1.png')
st.image('dataset_2.png')

# st.components.v1.iframe("https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv", height=400, scrolling=True)

st.subheader('Preprocessing')
st.markdown(
  '''Tahapan preprocessing yang dilakukan berupa:
  1. Compress: mengkompres tiga atau lebih karakter yang berulang dengan menggunakan regular expression :blue-background[re.sub].
  2. Tokenization: memecah kalimat menjadi kata terpisah dengan menggunakan :blue-background[word_tokenize] dari :blue-background[nltk].
  3. Lowercasing: mengubah semua kata menjadi huruf kecil.
  4. Stopwords and Punctuation: menghilangkan stopwords yang sering digunakan dalam bahasa tertentu dan simbol-simbol atau tanda baca.5. Alphabetical: menghilangkan karakter non alfabet.
  6. Stemming: menggunakan :blue-background[PorterStemmer] untuk mengubah kata yang ada ke bentuk dasar sehingga mengurangi variasi.
  7. Lemmatization: menggunakan :blue-background[WordNetLemmatizer] untuk mengubah kata menjadi bentuk kamusnya.'''
)