from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql://root:1234@localhost:3306/IDS")

QUERY_TODOS_LOS_CENTROS = "SELECT * FROM centros"

QUERY_ANADIR_CENTRO = "INSERT INTO centro (nombre,comuna,direccion,capacidad,direccion,contacto) VALUES (:nombre,:comuna,:direccion,:capacidad,:direccion,:contacto)"

def run_query(query,parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query),parameters)
        conn.commit()

    return result

def anadir_centro(data):
    return run_query(QUERY_ANADIR_CENTRO, data)

def todos_los_centros():
    return run_query(QUERY_TODOS_LOS_CENTROS).fetchall

def por_comuna(comuna):
    query = QUERY_TODOS_LOS_CENTROS

    filtros.join([f"{key} = '{value}' " for key, value in comuna.items()])
    filtros = f"WHERE {filtros}" 

    query += filtros

    return run_query(query).fetchall

def por_nombre(nombre):
    query = QUERY_TODOS_LOS_CENTROS

    filtros.join([f"{key} = '{value}' " for key, value in nombre.items()])
    filtros = f"WHERE {filtros}" 

    query += filtros

    return run_query(query).fetchall
    
def por_capacidad(capacidad):
    query = QUERY_TODOS_LOS_CENTROS

    filtros.join([f"{key} = '{value}' " for key, value in capacidad.items()])
    filtros = f"WHERE {filtros}" 

    query += filtros

    return run_query(query).fetchall

def por_direccion(direccion):
    query = QUERY_TODOS_LOS_CENTROS

    filtros.join([f"{key} = '{value}' " for key, value in direccion.items()])
    filtros = f"WHERE {filtros}" 

    query += filtros

    return run_query(query).fetchall
