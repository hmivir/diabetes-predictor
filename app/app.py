import streamlit as st
import requests

#FastAPI URL

url= 'http://127.0.0.1:8000/dbt_predict_probability'

st.title("Probability Diabetes disease")

#Create input fields
Age = st.number_input('Age', min_value= 0, step=1)
Glucose = st.number_input('Glucose Level (UI/L)', min_value=34)
Insulin = st.number_input('Insulin Level (UI/L)', min_value= 0.4)
BMI = st.number_input('Body Mass Index (BMI= Kg/cm2)', min_value= 13)
Pregnancies = st.number_input('Pregnancies', min_value = 0, step=1)

#Create the button to do the prediction
if st.button("Predict DBT Probability"):
    data = {
        "Age": Age,
        "Glucose": Glucose,
        "Insulin": Insulin,
        "BMI": BMI,
        "Pregnancies": Pregnancies
    }
    #send the data to the API
    try:
        response= requests.post(url, json=data)
        response.raise_for_status()
        prob = response.json()
        st.write(f"Diabetes Probability: {prob['Probability of having diabetes']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error with API request: {e}")