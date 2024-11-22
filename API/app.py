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

@app.route('/api/v1/centros/direcciones', methods=['GET'])
def direcciones():
    try:
        result = centros.direcciones()
    except Exception as e:
        return jsonify({'error':str(e)}), 500

    response = []

    for row in result:
        response.append({'direccion' : row[2] })
        
    return jsonify(response), 200




@app.route('/api/v1/anadircentros',methods=['GET','POST'])
def anadir_centro():
    nombre = request.args.get('nombre')
    comuna = request.args.get('comuna')
    direccion = request.args.get('direccion')
    capacidad = request.args.get('capacidad')
    contacto = request.args.get('contacto')
    instalaciones = request.args.get('instalaciones')

    if nombre is None or comuna is None or direccion is None or capacidad is None or contacto is None or instalaciones is None:
        return jsonify({"error":"Faltan datos"}), 400

    data = (nombre,comuna,direccion,capacidad,contacto,instalaciones)
        
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