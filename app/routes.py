from flask import (
    Flask,
    request
)

from app.database import data_types

app = Flask(__name__)

@app.get("/data_types")
def index():
    out = data_types.scan()
    return out

@app.get("/data_types/integers")
def integers():
    out = data_types.select_by_type(name="Integers")
    return out

@app.get("/data_types/floats")
def floats():
    out = data_types.select_by_type(name="Float")
    return out

@app.get("/data_types/booleans")
def booleans():
    out = data_types.select_by_type(name="Booleans")
    return out


@app.post("/data_types")
def create_data_type():
    dt_body = request.json
    data_types.create(dt_body)

    return "", 204

@app.put("/data_types/<int:pk>")
def update_data_type(pk):
    dt_body = request.json
    data_types.update(dt_body, pk)

    return "", 204

@app.delete("/data_types/<int:pk>")
def delete_data_type(pk):
    data_types.delete(pk)
    
    return "", 204