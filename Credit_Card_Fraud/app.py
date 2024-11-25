import streamlit as st
import pandas as pd

# Results from the previous code
model_results = {
    'RandomForest': {
        'ROC AUC': 0.9902798315363146,
        'Classification Report': """
              precision    recall  f1-score   support

           0       1.00      1.00      1.00    103099
           1       0.94      0.78      0.86      1536

    accuracy                           1.00    104635
   macro avg       0.97      0.89      0.93    104635
weighted avg       1.00      1.00      1.00    104635
        """
    },
    'GradientBoosting': {
        'ROC AUC': 0.9934767644448539,
        'Classification Report': """
              precision    recall  f1-score   support

           0       1.00      1.00      1.00    103099
           1       0.91      0.75      0.82      1536

    accuracy                           1.00    104635
   macro avg       0.95      0.88      0.91    104635
weighted avg       1.00      1.00      1.00    104635
        """
    },
    'LogisticRegression': {
        'ROC AUC': 0.8695410289806401,
        'Classification Report': """
              precision    recall  f1-score   support

           0       0.99      1.00      0.99    103099
           1       0.70      0.21      0.33      1536

    accuracy                           0.99    104635
   macro avg       0.84      0.61      0.66    104635
weighted avg       0.98      0.99      0.98    104635
        """
    }
}

# Streamlit Frontend
st.title("Model Performance Comparison")

# Dropdown menu to select model
model_name = st.selectbox('Select a Model:', list(model_results.keys()))

# Display the selected model's ROC AUC score and classification report
st.write(f"### {model_name} - ROC AUC: {model_results[model_name]['ROC AUC']}")
st.write(f"### Classification Report:")
st.text_area("Classification Report", model_results[model_name]['Classification Report'], height=200)

# Show which model has the best ROC AUC score
best_model_name = max(model_results, key=lambda model: model_results[model]['ROC AUC'])
st.write(f"### Best Model (based on ROC AUC): {best_model_name}")
st.write(f"Best ROC AUC: {model_results[best_model_name]['ROC AUC']}")

