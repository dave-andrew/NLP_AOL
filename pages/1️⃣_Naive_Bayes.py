import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Naive Bayes",
    page_icon="1️⃣"
)

st.title('1️⃣ Naive Bayes')

st.image('assets/confusion_matrix/Confusion_Naive.png', caption='Naive Bayes Confusion Matrix')
st.markdown(
  '''**Naive Bayes** adalah algoritma klasifikasi probabilistik yang sederhana dan efektif untuk klasifikasi teks.

  **Cara Kerja:**
  1. Pelatihan Model: Hitung probabilitas kemunculan kata-kata dalam setiap kelas ujaran kebencian.
  2. Klasifikasi Teks Baru: Gunakan teorema Bayes untuk menghitung probabilitas teks baru di setiap kelas ujaran kebencian dan prediksi kelas dengan probabilitas tertinggi.
  
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
st.markdown("<hr>", unsafe_allow_html=True)