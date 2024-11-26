from flask import Flask, jsonify, request
import requests 
from flask_cors import CORS
import centros
import casos

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/centros', methods=['GET'])
def todos_los_centros():
    try:
        result = centros.todos_los_centros()
    except Exception as e:
        return jsonify({'error':str(e)}), 500

    response = []

    for row in result:
        response.append({'nombre': row[0],
        'comuna' : row[1] , 
        'direccion' : row[2] , 
        'capacidad' : row[3] , 
        'instalaciones' : row[4] , 
        'contacto' : row[5]})

    return jsonify(response), 200

@app.route('/api/v1/casos', methods=['GET'])
def todos_los_casos():
    try:
        result = casos.todos_los_casos()
    except Exception as e:
        return jsonify({'error':str(e)}), 500
        
    response = []

    for row in result:
        response.append({'direccion': row[0],  # Dependiendo del formato de tu resultado
        'adultos': row[1],
        'menores': row[2]
        })
    return jsonify(response), 200

@app.route('/api/v1/anadircaso', methods=['POST'])
def anadir_caso():
    # Asegúrate de que se esté recibiendo JSON
    if request.is_json:
        data = request.get_json()
        print(f"Datos recibidos: {data}")

        direccion = data.get('direccion')
        adultos = data.get('adultos')
        menores = data.get('menores')

        try:
            casos.anadir_caso(data)  # Llamada a la función para agregar el caso
            return jsonify({'message': 'Caso añadido correctamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Se esperaba un contenido de tipo JSON'}), 415

    
@app.route('/api/v1/centros/direcciones', methods=['GET'])
def direcciones():
    try:
        result = centros.todos_los_centros()
    except Exception as e:
        return jsonify({'error':str(e)}), 500

    response = []

    for row in result:
        response.append({'direccion' : row[2]})

    return jsonify(response), 200

@app.route('/api/v1/anadircentros',methods=['GET','POST'])
def anadir_centro():
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        comuna = request.args.get('comuna')
        direccion = request.args.get('direccion')
        capacidad = request.args.get('capacidad')
        contacto = request.args.get('contacto')
        instalaciones = request.args.get('instalaciones')

    # Si es una solicitud POST, obtenemos los parámetros del cuerpo (JSON)
    elif request.method == 'POST':
        centro = request.get_json()  
        nombre = centro.get('nombre')
        comuna = centro.get('comuna')
        direccion = centro.get('direccion')
        capacidad = centro.get('capacidad')
        contacto = centro.get('contacto')
        instalaciones = centro.get('instalaciones')

    data = [{
        'nombre': nombre,
        'comuna': comuna,
        'direccion': direccion,
        'capacidad': capacidad,
        'contacto': contacto,
        'instalaciones': instalaciones
    }]


    try:
        centros.anadir_centro(data)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
    return jsonify(data), 201
    
@app.route('/api/v1/centros/comuna/<int:comuna>', methods=['GET'])
def por_comuna(comuna):
    try:
        result = centros.por_comuna(comuna)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    response = []
    for row in result:
        response.append({'nombre': row[0],
        'comuna' : row[1] , 
        'direccion' : row[2] , 
        'capacidad' : row[3] , 
        'instalaciones' : row[4] , 
        'contacto' : row[5]})

    return jsonify(response), 200

@app.route('/api/v1/centros/nombre/<string:nombre>', methods=['GET'])
def por_nombre(nombre):
    try:
        result = centros.por_nombre(nombre)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    response = []
    for row in result:
        response.append({'nombre': row[0],
        'comuna' : row[1] , 
        'direccion' : row[2] , 
        'capacidad' : row[3] , 
        'instalaciones' : row[4] , 
        'contacto' : row[5]})

    return jsonify(response), 200

@app.route('/api/v1/centros/capacidad/<int:capacidad>', methods=['GET'])
def por_capacidad(capacidad):
    try:
        result = centros.por_capacidad(capacidad)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    response = []
    for row in result:
        response.append({'nombre': row[0],
        'comuna' : row[1] , 
        'direccion' : row[2] , 
        'capacidad' : row[3] , 
        'instalaciones' : row[4] , 
        'contacto' : row[5]})

    return jsonify(response), 200

@app.route('/api/v1/centros/direccion/<string:direccion>', methods=['GET'])
def por_direccion(direccion):
    try:
        result = centros.por_direccion(direccion)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    response = []
    for row in result:
        response.append({'nombre': row[0],
        'comuna' : row[1] , 
        'direccion' : row[2] , 
        'capacidad' : row[3] , 
        'instalaciones' : row[4] , 
        'contacto' : row[5]})

    return jsonify(response), 200


if __name__=='__main__':
    app.run(debug=True)