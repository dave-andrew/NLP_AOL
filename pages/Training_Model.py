import streamlit as st

st.set_page_config(
    page_title="Models",
)
st.title('Models')
st.subheader('Decision Tree')
st.markdown(
  '''Decision Tree adalah algoritma klasifikasi yang bekerja dengan cara membagi data menjadi subset-subset berdasarkan aturan tertentu, menghasilkan struktur pohon yang bercabang.

  Cara Kerja:
  1. Pemilihan Atribut: Memilih atribut yang paling informatif untuk membagi data.
  2. Pembuatan Pohon: Membangun struktur pohon dengan membagi data secara berulang berdasarkan atribut yang dipilih.
  3. Klasifikasi Teks Baru: Mengikuti cabang-cabang pohon berdasarkan nilai atribut teks baru untuk mencapai daun dan menggunakan label daun sebagai prediksi kelas.'''
)

st.subheader('Linear Regression')

st.subheader('Naive Bayes')

st.subheader('Linear SVC')

st.subheader('ADA Boost')

st.subheader('Random Forest')