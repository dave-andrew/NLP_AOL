import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Linear SVC",
    page_icon="3️⃣"
)
st.title('3️⃣ Linear SVC')


formula1 = r'\min_{w, b, \xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \xi_i'
formula2 = r'''y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \forall i \\ 
              \xi_i \geq 0, \quad \forall i'''
formula3 = r'f(x) = w^T x + b'
formula4 = r'''
      \text{class} = \begin{cases} 
      +1 & \text{if } f(x) \geq 0 \\
      -1 & \text{if } f(x) < 0
      \end{cases}
      '''

formula5 = '''
      \max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i,j=1}^n y_i y_j \alpha_i \alpha_j x_i^T x_j \\
      \text{subject to } 0 \leq \alpha_i \leq C, \quad \forall i \\
      \sum_{i=1}^n \alpha_i y_i = 0
      '''
      
st.image('assets/confusion_matrix/Confusion_Linear_SVC.png', caption='Linear SVC Confusion Matrix')
st.markdown(
  '''**Linear SVC (Support Vector Classification)** adalah algoritma klasifikasi yang digunakan untuk memisahkan data menjadi dua kelas atau lebih. Algoritma ini bekerja dengan mencari hyperplane linier yang memisahkan data dengan margin maksimum.

  **Cara Kerja:**
  1. Pencarian Hyperplane: Algoritma mencari hyperplane linier yang memisahkan data *"hate-speech"* dan *"non-hate-speech"* dengan margin maksimum. Margin adalah jarak minimum antara hyperplane dan data poin terdekat dari setiap kelas.
  2. Klasifikasi Teks Baru: Untuk mengklasifikasikan teks baru, algoritma menghitung jaraknya dari hyperplane. Jika teks baru berada di satu sisi hyperplane, maka diklasifikasikan ke kelas di sisi tersebut.
  
  **LinearSVC Formula:**
  Goal dari LinearSVC adalah untuk menemukan hyperplane yang memisahkan data dengan margin maksimum. Hyperplane ini didefinisikan sebagai:
  '''
)
st.latex(formula1)
      
st.markdown('''dengan batasan:''')
st.latex(formula2)

st.markdown('''
            Optimisasi dari fungsi ini akan menghasilkan nilai w dan b 
            yang akan digunakan untuk mengklasifikasikan 
            teks baru dengan rumus dual form of optimization 
            problem dan quadratic programming, dengan contoh sebagai berikut:
            ''')
st.latex(formula5)
st.markdown('''
            Fungsi decision akan menghasilkan kelas dari teks baru:
            ''')
st.latex(formula3)

st.markdown('''
            Terakhir, klasifikasi ditentukan dari tanda dari fungsi decision. (e.g. jika positif maka hateful, dst)
            ''')
st.latex(formula4)

st.markdown(
  '''
  **Kelebihan:**
  - Efisien dalam ruang dan waktu
  - Efektif dalam dimensi tinggi
  - Tidak terpengaruh oleh data yang tidak relevan
  
  **Kekurangan:**
  - Tidak efektif dalam dataset yang besar
  - Sensitif terhadap noise
  - Tidak cocok untuk data yang tidak linier
  
  **Hasil Evaluasi:**
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