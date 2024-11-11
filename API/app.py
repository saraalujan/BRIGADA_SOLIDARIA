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
        response.append({'nombre': row[0],'comuna' : row[1] , 'direccion' : row[2] , 'capacidad' : row[3] , 'instalaciones' : row[4] , 'contacto' : row[5]})

    return jsonify(response), 200

if __name__=='__main__':
    app.run(debug=True)