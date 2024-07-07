import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Linear SVC",
    page_icon="3️⃣"
)
st.title('3️⃣ Linear SVC')

st.image('assets/confusion_matrix/Confusion_Linear_SVC.png', caption='Linear SVC Confusion Matrix')
st.markdown(
  '''**Linear SVC (Support Vector Classification)** adalah algoritma klasifikasi yang digunakan untuk memisahkan data menjadi dua kelas atau lebih. Algoritma ini bekerja dengan mencari hyperplane linier yang memisahkan data dengan margin maksimum.

  **Cara Kerja:**
  1. Pencarian Hyperplane: Algoritma mencari hyperplane linier yang memisahkan data *"hate-speech"* dan *"non-hate-speech"* dengan margin maksimum. Margin adalah jarak minimum antara hyperplane dan data poin terdekat dari setiap kelas.
  2. Klasifikasi Teks Baru: Untuk mengklasifikasikan teks baru, algoritma menghitung jaraknya dari hyperplane. Jika teks baru berada di satu sisi hyperplane, maka diklasifikasikan ke kelas di sisi tersebut.
  
  :green-background[Accuracy: 82.53%]'''
)
svc_data = {
    'Class': ['hateful', 'non-hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.63, 0.86, '', 0.75, 0.81],
    'Recall': [0.46, 0.93, '', 0.69, 0.83],
    'F1-Score': [0.54, 0.89, '', 0.71, 0.82],
    'Support': [325, 1175, 1500, 1500, 1500]
}
svc_df = pd.DataFrame(svc_data)
st.table(svc_df)
st.markdown("<hr>", unsafe_allow_html=True)