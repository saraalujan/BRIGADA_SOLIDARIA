from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql://root:1234@localhost:3306/IDS")

QUERY_ANADIR_CASO = "INSERT INTO casos (direccion, adultos, menores) VALUES (:direccion, :adultos, :menores)"

QUERY_CASOS = "SELECT * FROM casos"

def run_query(query,parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query),parameters)
        conn.commit()

    return result

def anadir_caso(data):
    run_query(QUERY_ANADIR_CASO, data)

def casos():
    run_query(QUERY_CASOS).fetchall()