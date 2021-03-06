from sklearn.externals import joblib
import json
import numpy as np
import requests
from urllib.request import urlopen
import sys

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    url = requests.get("https://raw.githubusercontent.com/zuhairabs/housing-api/main/artifacts/columns.json")
    __data_columns = url.json()['data_columns']
    __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    print(__locations)
    sys.stdout.flush()

    global __model
    if __model is None:
        __model = joblib.load(urlopen("https://github.com/zuhairabs/housing-api/blob/main/artifacts/banglore_home_prices_model.pickle?raw=true"))
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

load_saved_artifacts()