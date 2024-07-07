
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
  '''
)

st.markdown(
  '''
  **Decision Tree** selalu diawali dengan pembuatan root node.\n
  Setiap node dalam pohon akan membagi data berdasarkan atribut yang paling informatif. Pembagian ini dapat dilakukan dengan menggunakan beberapa rumus berikut:\n
  '''
)

st.text('Gini Impurity Formula')
gini_formula = r"Gini(p) = 1 - \sum_{i=1}^{C} p_i^2"
st.latex(gini_formula)
st.text('Mengukur seberapa sering elemen akan diklasifikasikan salah.')

st.text("Entropy Formula")
entropy_formula = r"Entropy(p) = - \sum_{i=1}^{C} p_i \log_2(p_i)"
st.latex(entropy_formula)
st.text('Mengukur seberapa tidak teratur data.')

st.text("Information Gain Formula")
info_gain_formula = r"IG(A) = Entropy(parent) - \sum_{k=1}^{K} \frac{N_k}{N} \cdot Entropy(k)"
st.latex(info_gain_formula)
st.text('Mengukur seberapa banyak informasi yang diperoleh setelah membagi data berdasarkan atribut tertentu.')

st.text("Mean Squared Error Formula")
mse_formula = r"MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \bar{y})^2"
st.latex(mse_formula)
st.text('Mengukur seberapa dekat prediksi dengan nilai sebenarnya.')

st.markdown(
  '''
  :green-background[Accuracy: 90%]
  '''
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