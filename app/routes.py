from flask import (
    Flask,
    request
)

app = Flask(__name__)

@app.get("/")
def index():
    pass

@app.get("/integers")
def integers():
    out = data_types.select_by_type(type="int")
    return out

@app.get("/floats")
def floats():
    out = data_types.select_by_type(type="float")
    return out

@app.get("/booleans")
def booleans():
    out = data_types.select_by_type(type="bool")
    return out