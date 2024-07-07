import streamlit as st

st.set_page_config(
    page_title="Data and Preprocessing",
    page_icon="📊"
)
st.title('📊 Data and Preprocessing')

st.subheader('Dataset')
st.markdown(
  '''Dataset yang digunakan diambil dari Kaggle untuk mengklasifikasikan apakah suatu teks merupakan ***hate-speech*** atau ***non-hate-speech***.
  
  **Link dataset:**
  https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv'''
)
st.image('assets/dataset/dataset_1.png')
st.image('assets/dataset/dataset_2.png')
st.markdown("<hr>", unsafe_allow_html=True)

# st.components.v1.iframe("https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset?select=HateSpeechDataset.csv", height=400, scrolling=True)

st.subheader('Preprocessing')
st.markdown(
  '''Tahapan **preprocessing** yang dilakukan berupa:
  1. Compress: mengkompres tiga atau lebih karakter yang berulang dengan menggunakan regular expression :blue-background[re.sub].
  2. Tokenization: memecah kalimat menjadi kata terpisah dengan menggunakan :blue-background[word_tokenize] dari :blue-background[nltk].
  3. Lowercasing: mengubah semua kata menjadi huruf kecil.
  4. Stopwords and Punctuation: menghilangkan stopwords yang sering digunakan dalam bahasa tertentu dan simbol-simbol atau tanda baca.5. Alphabetical: menghilangkan karakter non alfabet.
  6. Stemming: menggunakan :blue-background[PorterStemmer] untuk mengubah kata yang ada ke bentuk dasar sehingga mengurangi variasi.
  7. Lemmatization: menggunakan :blue-background[WordNetLemmatizer] untuk mengubah kata menjadi bentuk kamusnya.'''
)
st.markdown("<hr>", unsafe_allow_html=True)

st.subheader('Source Code')
st.markdown(
  '''Link .ipynb:
  https://colab.research.google.com/drive/1r8rkNERa4kD-bCl7mXM4oKLb87EnX38d?usp=sharing'''
)