from flask import Flask, jsonify, request

import centros
app = Flask(__name__)

@app.route('/api/v1/centros',methods=['GET'])
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

@app.route('/api/v1/anadircentros',methods=['POST'])
def anadir_centro():
    data = request.get_json()

    keys = ('nombre','comuna','direccion','capacidad','instalaciones','contacto')
    for key in keys:
        if key not in data:
            return jsonify({'error':f'Falta el dato {key}'}), 400
        
    try:
        centros.anadir_centro(data)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
    return jsonify(data), 201
    
@app.route('/api/v1/centros/<int:comuna>', methods=['GET'])
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

@app.route('/api/v1/centros/<string:nombre>', methods=['GET'])
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

@app.route('/api/v1/centros/<int:capacidad>', methods=['GET'])
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

@app.route('/api/v1/centros/<string:direccion>', methods=['GET'])
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