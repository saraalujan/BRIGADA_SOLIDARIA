from flask import Flask,render_template,request,jsonify
import requests

API_URL = 'http://root:1234@localhost:5001/api/v1/centros'

app = Flask(__name__)

@app.route("/sobre_nosotros")
def sobre_nosotros():
    return render_template("sobre_nosotros.html")

@app.route("/nuevos_centros")
def nuevos_centros():
    return render_template("nuevos_centros.html")

@app.route("/centros")
def centros():
    return render_template("centros.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formato_centros")
def formato_centros():
    nombre = request.args.get('nombre')
    comuna = request.args.get('comuna')
    direccion = request.args.get('direccion')
    capacidad = request.args.get('capacidad')

    url = API_URL
    if nombre is not None:
        url =f"{API_URL}/nombre/{nombre}"
    elif comuna is not None:
        url =f"{API_URL}/comuna/{comuna}"
    elif direccion is not None:
        url =f"{API_URL}/direccion/{direccion}"
    elif capacidad is not None:
        url =f"{API_URL}/capacidad/{capacidad}"
    
    response = requests.get(url)
    if response is not None and response.status_code == 200:
        centros=response.json()
    else:
        centros = []  

    return render_template("formato_centros.html", centros=centros)

@app.route("/buscar_centros")
def buscar_centros():
    return render_template("buscar_centros.html")

if __name__=="__main__":
    app.run(debug=True)