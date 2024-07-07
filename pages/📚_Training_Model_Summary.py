import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Training Model Summary",
    page_icon="📚"
)
st.title('📚 Training Model Summary')

# Naive Bayes
st.subheader('1️⃣ Naive Bayes')
st.image('assets/confusion_matrix/Confusion_Naive.png', caption='Naive Bayes Confusion Matrix')
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

# Decision Tree
st.subheader('2️⃣ Decision Tree')
st.image('assets/confusion_matrix/Confusion_Decision.png', caption='ADA Boost Confusion Matrix')
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

# Linear SVC
st.subheader('3️⃣ Linear SVC')
st.image('assets/confusion_matrix/Confusion_Linear_SVC.png', caption='Linear SVC Confusion Matrix')
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

# ADA Boost
st.subheader('4️⃣ ADA Boost')
st.image('assets/confusion_matrix/Confusion_ADA.png', caption='ADA Boost Confusion Matrix')
ada_data = {
    'Class': ['hateful', 'non-hateful', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.79, 0.85, '', 0.82, 0.83],
    'Recall': [0.38, 0.97, '', 0.68, 0.84],
    'F1-Score': [0.52, 0.90, '', 0.71, 0.82],
    'Support': [333, 1167, 1500, 1500, 1500]
}
ada_df = pd.DataFrame(ada_data)
st.table(ada_df)

st.markdown("<hr>", unsafe_allow_html=True)


# Acccuracy Result Comparison
st.subheader('Accuracy Result Comparison')
st.image('assets/accuracy/Accuracy.png', caption='Accuracy Result Comparison')