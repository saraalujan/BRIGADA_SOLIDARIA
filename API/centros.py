from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql://root:1234@localhost:3306/IDS")

QUERY_TODOS_LOS_CENTROS = "SELECT * FROM centros"

QUERY_ANADIR_CENTRO = "INSERT INTO centros (nombre,comuna,direccion,capacidad, instalaciones,contacto) VALUES (:nombre, :comuna, :direccion, :capacidad, :instalaciones, :contacto)"

QUERY_POR_COMUNA ="SELECT * FROM centros WHERE comuna = :comuna"

QUERY_POR_NOMBRE = "SELECT * FROM centros WHERE nombre = :nombre"

QUERY_POR_CAPACIDAD = "SELECT * FROM centros WHERE capacidad >= :capacidad"

QUERY_POR_DIRECCION = "SELECT * FROM centros WHERE direccion = :direccion"

QUERY_DIRECCIONES = "SELECT nombre, direccion FROM centros"

def run_query(query,parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query),parameters)
        conn.commit()

    return result

def direcciones():
    return run_query(QUERY_DIRECCIONES,).fetchall()

def anadir_centro(data):
    run_query(QUERY_ANADIR_CENTRO, data)

def todos_los_centros():
    return run_query(QUERY_TODOS_LOS_CENTROS).fetchall()

def por_comuna(comuna):
    return run_query(QUERY_POR_COMUNA, {'comuna':comuna}).fetchall()

def por_nombre(nombre):
    return run_query(QUERY_POR_NOMBRE, {'nombre':nombre}).fetchall()
    
def por_capacidad(capacidad):
    return run_query(QUERY_POR_CAPACIDAD, {'capacidad':capacidad}).fetchall()

def por_direccion(direccion):
    return run_query(QUERY_POR_DIRECCION, {'direccion':direccion}).fetchall()
