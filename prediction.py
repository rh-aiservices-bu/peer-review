import pandas as pd
import logging
import joblib
import json

biomarkers = None
pipeline = None
model = None

def transformAndPredict(raw, pipeline, model, dropNonBioMarkers = True) :

    if dropNonBioMarkers :
        dropped = raw.drop(
        ["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"],
          axis=1)
    else :
        dropped = raw

    # perform inference and predict
    transformed = pipeline.transform(dropped)
    prediction = model.predict(transformed)
    return prediction

def predict(data):
   
    # Dictionary to interpret results
    dictionary = {0: 'No Sepsis',1:'Sepsis detected'}

    #Load the data to run prediction on, model and pipeline
    jsondata = json.loads("[" + json.dumps(data) + "]")
    raw = pd.DataFrame(jsondata)
    pipeline = joblib.load("data/transform/pipeline.pkl")
    model = joblib.load("models/experiment/xgbc_model.pkl")
    
    # Run prediction
    prediction = transformAndPredict(raw, pipeline, model, dropNonBioMarkers = False )
    result = dictionary[prediction[0]]

    return {'prediction': result}

    