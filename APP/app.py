from flask import Flask,render_template
import requests

API_URL = 'http://root:1234@localhost:5000/api/v1/'

app = Flask(__name__)

@app.route("/sobre_nosotros")
def sobre_nosotros():
    return render_template("sobre_nosotros.html")

@app.route("/nuevos_centros")
def nuevos_centros():
    return render_template("nuevos_centros.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar_centros")
def buscar_centros():
    return render_template("buscar_centros.html")

@app.route("/centros")
def centros():
    return render_template("centros.html")

if __name__=="__main__":
    app.run(debug=True,port=8080)