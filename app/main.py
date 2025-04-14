from fastapi import FastAPI
from pydantic import BaseModel
import  joblib
import numpy as np

#Load the model
model = joblib.load('dbt_model.joblib')

app=FastAPI()

#create a class for the input data
class Input_user_data(BaseModel):
    Age : int
    Glucose : float
    Insulin : float
    BMI: float
    Pregnancies: int

@app.post('/dbt_predict_probability')
#Create a function to predict the probability of diabetes
def dbt_predict_prob(data:Input_user_data):
    #Convert the input data to a numpy array
    input_data = np.array([data.Age, data.Glucose, data.Insulin, data.BMI, data.Pregnancies]).reshape(1,-1)
    #Predict the probability of diabetes
    prob = model.predict_proba(input_data)[:,1]
    #convert probability to percentage
    prob_percentage= round(prob[0]*100,2)
    return {'Probability of having diabetes': f"{prob_percentage}%"}