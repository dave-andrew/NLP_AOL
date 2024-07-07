
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Decision Tree",
    page_icon="2️⃣"
)

st.title('2️⃣ Decision Tree')

st.image('assets/confusion_matrix/Confusion_Decision.png', caption='Decision Tree Confusion Matrix')
st.markdown(
  '''**Decision Tree** adalah algoritma klasifikasi yang bekerja dengan cara membagi data menjadi subset-subset berdasarkan aturan tertentu, menghasilkan struktur pohon yang bercabang.

  **Cara Kerja:**
  1. Pemilihan Atribut: Memilih atribut yang paling informatif untuk membagi data.
  2. Pembuatan Pohon: Membangun struktur pohon dengan membagi data secara berulang berdasarkan atribut yang dipilih.
  3. Klasifikasi Teks Baru: Mengikuti cabang-cabang pohon berdasarkan nilai atribut teks baru untuk mencapai daun dan menggunakan label daun sebagai prediksi kelas.
  
  :green-background[Accuracy: 90%]'''
)
dt_data = {
    'Class': ['hateful', 'non-hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.77, 0.95, '', 0.86, 0.91],
    'Recall': [0.82, 0.93, '', 0.87, 0.90],
    'F1-Score': [0.79, 0.94, '', 0.87, 0.91],
    'Support': [336, 1164, 1500, 1500, 1500]
}
dt_df = pd.DataFrame(dt_data)
st.table(dt_df)
st.markdown("<hr>", unsafe_allow_html=True)