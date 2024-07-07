import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ADA Boost",
    page_icon="⚡"
)
st.title('⚡ ADA Boost')

st.image('assets/confusion_matrix/Confusion_ADA.png', caption='ADA Boost Confusion Matrix')

formula_1 = r'weight = \frac{1}{2} \times \ln \left( \frac{1 - error}{error} \right)'
formula_2 = r'weight = weight \times e^{weight}'
formula_3 = r'sample weight = \frac{sample weight}{total sample weight}'

st.markdown(
  '''
  **AdaBoost (Adaptive Boosting)** adalah algoritma klasifikasi yang meningkatkan kinerja *weak learner* (algoritma klasifikasi sederhana).

  **Cara Kerja:**
  1. Memfokuskan pada data yang sulit: Memberikan bobot lebih tinggi pada data yang salah diklasifikasikan untuk melatih *weak learner* selanjutnya.
  2. Menggabungkan *weak learner*: Menggabungkan prediksi dari beberapa *weak learner* untuk mendapatkan hasil klasifikasi yang lebih akurat.''')

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('''Pertama-tama, semua data diberi bobot yang sama. Yaitu setiap data memiliki bobot 1/N, di mana N adalah jumlah total data.\n
  Kemudian, model *weak learner* pertama dibuat dan diuji pada data. \n
  Dengan menggunakan rumus error sebagai berikut:
  '''
)

st.latex(formula_1)

st.markdown(
  '''
  Weight pada data yang salah akan dikalkulasi kembali dengan rumus:
  '''
)

st.latex(formula_2)

st.markdown(
  '''
  Kalau dikalkulasikan, total sample weight terkadang tidak sama dengan 1. 
  Maka, sample weight akan dinormalisasi dengan rumus:
  '''
)

st.latex(formula_3)

st.markdown(
  '''
  Proses ini diulang hingga mencapai jumlah *weak learner* yang diinginkan.
  Untuk prediksinya, bobot dari *weak learner* akan dijumlahkan.
  
  :green-background[Accuracy: 84.06%]
  '''
)

ada_data = {
    'Class': ['hateful', 'non-hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.79, 0.85, '', 0.82, 0.83],
    'Recall': [0.38, 0.97, '', 0.68, 0.84],
    'F1-Score': [0.52, 0.90, 0.84, 0.71, 0.82],
    'Support': [333, 1167, 1500, 1500, 1500]
}
ada_df = pd.DataFrame(ada_data)
st.table(ada_df)
