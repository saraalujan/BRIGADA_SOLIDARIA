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

@app.route("/centros")
def centros():
    nombre = requests.args.get('nombre')
    comuna = requests.args.get('comuna')
    direccion = requests.args.get('direccion')
    capacidad = requests.args.get('capacidad')

    params = None

    if nombre is not None:
        params = {'nombre':nombre}
        response = requests.get(API_URL+'/nombre',params=params)

    if comuna is not None:
        params = {'comuna':comuna}
        response =requests.get(API_URL+'/comuna',params=params)

    if direccion is not None:
        params={'direccion':direccion}
        response=requests.get(API_URL+'/direccion',params=params)

    if capacidad is not None:
        params={'capacidad':capacidad}
        response=requests.get(API_URL+'/capacidad',params=params)

    json_response=response.json()
    centros=json_response.get("data",[])

    print(centros)
    
    return render_template("formato_centros.html",centros=centros)

@app.route("/buscar_centros")
def centros():
    return render_template("buscar_centros.html")

if __name__=="__main__":
    app.run(debug=True,port=8080)