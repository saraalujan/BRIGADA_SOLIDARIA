from flask import Flask, jsonify,json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("mysql://root@localhost:3306/IDS")

session = scoped_session(sessionmaker(bind=engine))

QUERY_TODOS_LOS_CENTROS = "SELECT * FROM centros"

app = Flask(__name__)

@app.route("/api/v1/centros", methods=['GET'])
def get_todos_los_centros():
    try:
        return jsonify(centros),200
    except:
        pass

if __name__=='__main__':
    app.run(debug=True)