import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Training Models",
    page_icon="📚"
)
st.title('📚 Training Models')
st.subheader('Decision Tree')
st.image('Confusion_Decision.png', caption='Decision Tree Confusion Matrix', width=400)
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

st.subheader('Naive Bayes')
st.image('Confusion_Naive.png', caption='Naive Bayes Confusion Matrix')
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

st.subheader('Linear SVC')
st.image('Confusion_Linear_SVC.png', caption='Linear SVC Confusion Matrix')
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

st.subheader('ADA Boost')
st.image('Confusion_ADA.png', caption='ADA Boost Confusion Matrix')
st.markdown(
  '''**AdaBoost (Adaptive Boosting)** adalah algoritma klasifikasi yang meningkatkan kinerja *weak learner* (algoritma klasifikasi sederhana).

  **Cara Kerja:**
  1. Memfokuskan pada data yang sulit: Memberikan bobot lebih tinggi pada data yang salah diklasifikasikan untuk melatih *weak learner* selanjutnya.
  2. Menggabungkan *weak learner*: Menggabungkan prediksi dari beberapa *weak learner* untuk mendapatkan hasil klasifikasi yang lebih akurat.
  
  :green-background[Accuracy: 84.06%]'''
)
ada_data = {
    'Class': ['hateful', 'non-hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.79, 0.85, '', 0.82, 0.83],
    'Recall': [0.38, 0.97, '', 0.68, 0.84],
    'F1-Score': [0.52, 0.90, '', 0.71, 0.82],
    'Support': [333, 1167, 1500, 1500, 1500]
}
ada_df = pd.DataFrame(ada_data)
st.table(ada_df)