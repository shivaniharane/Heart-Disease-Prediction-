# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:55:35 2023

@author: lenovo
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:/MachineLearning/HeartDisease/trained_model.sav', 'rb'))


#Creating function for prediction
def heartDisease_Prediction(input_data):
    
   
    #change the input data to numpy array
    input_data_as_numpy_array = np.array(input_data)

    #reshape the numpy array as we are predicting for one value
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1);

    prediction = loaded_model.predict(input_data_reshaped)


    if(prediction[0] == 0):
        return('Person is Healthy')
    else:
        return('Person is unhealthy')
        
def main():
    
    #Giving title
    st.title('Heart Disease Perdiction Model')
    
    #Getting the input data from user
    Age = st.text_input('Age')
    
    
    sex_mapping = {'Male': 0, 'Female': 1}
    Sex = st.selectbox('Sex', ['Male', 'Female'], format_func=lambda x: x)
    
    Cp = st.text_input('Cp')
    
    Trestbps = st.text_input('Trestbps')
    
    Chol = st.text_input('Chol')
    
    Fbs = st.text_input('Fbs')
    
    Restecg = st.text_input('Restecg')
    
    Thalach = st.text_input('Thalach')
    
    Exang = st.text_input('Exang')
    
    Oldpeak = st.text_input('Oldpeak')
    
    Slope = st.text_input('Slope')
    
    Ca = st.text_input('Ca')

    Thal = st.text_input('Thal')
    
    
   # Validate and convert input data to numeric types
    
    input_data = [
            float(Age) if Age else 0.0,
            float(sex_mapping[Sex]),
            float(Cp) if Cp else 0.0,
            float(Trestbps) if Trestbps else 0.0,
            float(Chol) if Chol else 0.0,
            float(Fbs) if Fbs else 0.0,
            float(Restecg) if Restecg else 0.0,
            float(Thalach) if Thalach else 0.0,
            float(Exang) if Exang else 0.0,
            float(Oldpeak) if Oldpeak else 0.0,
            float(Slope) if Slope else 0.0,
            float(Ca) if Ca else 0.0,
            float(Thal) if Thal else 0.0]

    
   # Creating button for prediction
    if st.button('Heart Disease Result'):
        diagnosis = heartDisease_Prediction(input_data)
        st.success(diagnosis)
        
if __name__ == '__main__':
    main()













