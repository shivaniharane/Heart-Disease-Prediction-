# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('D:/MachineLearning/HeartDisease/trained_model.sav', 'rb'))

input_data = (50,0,2,120,219,0,1,158,0,1.6,1,0,2)

#change the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for one value
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1);

prediction = loaded_model.predict(input_data_reshaped)

print(prediction)

if(prediction[0] == 0):
    print('Person is Healthy')
else:
    print('Person is unealthy')
    


