import streamlit as st
import pandas as pd

bayes_formula = r"P(c|x) = \frac{P(x|c) \cdot P(c)}{P(x)}"

st.set_page_config(
    page_title="Naive Bayes",
    page_icon="🧠"
)

st.title('🧠 Naive Bayes')

st.image('assets/confusion_matrix/Confusion_Naive.png', caption='Naive Bayes Confusion Matrix')
st.markdown(
  '''**Naive Bayes** adalah algoritma klasifikasi probabilistik yang sederhana dan efektif untuk klasifikasi teks. Algoritma ini didasarkan pada **teorema Bayes** dan asumsi sederhana yang disebut sebagai ***naive***, yaitu semua fitur saling independen.

  **Cara Kerja:**
  1. Pelatihan Model: Hitung probabilitas kemunculan kata-kata dalam setiap kelas ujaran kebencian.
  2. Klasifikasi Teks Baru: Gunakan teorema Bayes untuk menghitung probabilitas teks baru di setiap kelas ujaran kebencian dan prediksi kelas dengan probabilitas tertinggi.'''
)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
  '''**Teorema Bayes** memberikan cara untuk menghitung probabilitas dari suatu kejadian berdasarkan pengetahuan sebelumnya. Teorema Bayes dinyatakan sebagai berikut:'''
)
st.latex(bayes_formula)
st.markdown(
  '''- P(c|x) adalah probabilitas kelas c jika teks x, disebut sebagai probabilitas posterior
  - P(x|c) adalah probabilitas teks x jika kelas c, disebut sebagai probabilitas likelihood
  - P(c) adalah probabilitas kelas c, disebut sebagai probabilitas prior
  - P(x) adalah probabilitas teks x, disebut sebagai probabilitas evidence
  
  Teorema Bayes memungkinkan kita untuk menghitung probabilitas kelas ujaran kebencian berdasarkan kemunculan kata-kata dalam teks tersebut.

  :green-background[Accuracy: 81.73%]'''
)

nb_data = {
    '': ['non-hateful', 'hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'precision': [0.64, 0.85, '', 0.75, 0.80],
    'recall': [0.44, 0.93, '', 0.68, 0.82],
    'f1-score': [0.52, 0.89, 0.82, 0.70, 0.81],
    'support': [333, 1167, 1500, 1500, 1500]
}
nb_df = pd.DataFrame(nb_data)
st.table(nb_df)