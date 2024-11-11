from flask import Flask,jsonfy,request

import centros

app = Flask(__name__)

@app.route('/api/v1/centros',methods=['GET'])
def todos_los_centros():
    try:
        result = centros.todos_los_centros()
    except Exception as e:
        return jsonify({'error':str(e)}),500

    response = []

    for row in result:
        response.append({'nombre':})