import streamlit as st
import pickle
import numpy as np

#Load the Model
with open('sustainability_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
#Tile for your Application
st.title('Sustainability Prediction App')

#Input fields for the prediction
carbon_emmisions=st.number_input('Carbon Emission Amount: ',min_value=0.0,format="%f")
energy_output=st.number_input('Energy Output Amount: ',min_value=0.0,format="%f")
renewability_index=st.number_input('Renewability Index (0-100): ',min_value=0.0,format="%f")
cost_efficiency=st.number_input('Cost Efficiency (0-100): ',min_value=0.0,format="%f")



#Prediction Button
if st.button('Predict Sustanability'):
    #Prepare the inputs for prediction
    input_data=np.array([[carbon_emmisions, energy_output, renewability_index, cost_efficiency]])
    prediction=model.predict(input_data)
    
#Diplay the result
    if prediction[0]==1:
        st.success('The energy source is Sustainable')
    else:
        st.info('The energy source is Not Sustainable,Need To Improve')
