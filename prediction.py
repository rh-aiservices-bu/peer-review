import pandas as pd
import logging
import joblib
import json
import os
import shutil
import configparser
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

import numpy as np
biomarkers = None
pipeline = None
model = None
settings = None

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
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('config')
    settings.sections()

    #path to data folder
    version = settings.get('Run', 'version')

    #Prepare data directory for current run
    data_path = settings.get('Path', 'data') + "run_" + version
    transform_path = data_path + "/transform/"
    model_path = settings.get('Path', 'models') + "run_" + version

    
    #Load the data to run prediction on, model and pipeline
    pipeline = joblib.load(transform_path + "/pipeline.pkl")
    model = joblib.load(model_path + "/final/rfc_model.pkl")
    
    # Run prediction
    prediction = transformAndPredict(raw, pipeline, model, dropNonBioMarkers = False )
    result = dictionary[prediction[0]]

    return {'prediction': result}

