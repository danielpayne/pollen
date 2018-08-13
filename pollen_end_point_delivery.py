import pandas as pd

district_table = pd.read_csv('district_pollen.csv')
district_table = district_table.set_index('Postcode District')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/postcode_lookup/<string:name>/")
def getMember(name):
    pollen_count = 'None'
    try:
        pollen_count = district_table.loc[name, 'pollen_count']
    except:
        pollen_count = "This Postcode doesn't appear to exist.  Please check or contact an administrator"
    return pollen_count
