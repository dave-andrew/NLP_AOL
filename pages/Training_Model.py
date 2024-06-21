import streamlit as st

st.set_page_config(
    page_title="Training Models",
)
st.title('Training Models')
st.subheader('Decision Tree')
st.markdown(
  '''**Decision Tree** adalah algoritma klasifikasi yang bekerja dengan cara membagi data menjadi subset-subset berdasarkan aturan tertentu, menghasilkan struktur pohon yang bercabang.

  **Cara Kerja:**
  1. Pemilihan Atribut: Memilih atribut yang paling informatif untuk membagi data.
  2. Pembuatan Pohon: Membangun struktur pohon dengan membagi data secara berulang berdasarkan atribut yang dipilih.
  3. Klasifikasi Teks Baru: Mengikuti cabang-cabang pohon berdasarkan nilai atribut teks baru untuk mencapai daun dan menggunakan label daun sebagai prediksi kelas.'''
)

st.subheader('Naive Bayes')
st.markdown(
  '''**Naive Bayes** adalah algoritma klasifikasi probabilistik yang sederhana dan efektif untuk klasifikasi teks.

  **Cara Kerja:**
  1. Pelatihan Model: Hitung probabilitas kemunculan kata-kata dalam setiap kelas ujaran kebencian.
  2. Klasifikasi Teks Baru: Gunakan teorema Bayes untuk menghitung probabilitas teks baru di setiap kelas ujaran kebencian dan prediksi kelas dengan probabilitas tertinggi.'''
)

st.subheader('Linear SVC')
st.markdown(
  '''**Linear SVC (Support Vector Classification)** adalah algoritma klasifikasi yang digunakan untuk memisahkan data menjadi dua kelas atau lebih. Algoritma ini bekerja dengan mencari hyperplane linier yang memisahkan data dengan margin maksimum.

  **Cara Kerja:**
  1. Pencarian Hyperplane: Algoritma mencari hyperplane linier yang memisahkan data *"hate-speech"* dan *"non-hate-speech"* dengan margin maksimum. Margin adalah jarak minimum antara hyperplane dan data poin terdekat dari setiap kelas.
  2. Klasifikasi Teks Baru: Untuk mengklasifikasikan teks baru, algoritma menghitung jaraknya dari hyperplane. Jika teks baru berada di satu sisi hyperplane, maka diklasifikasikan ke kelas di sisi tersebut.'''
)