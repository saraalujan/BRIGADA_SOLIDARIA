from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Configuración de la conexión a la base de datos
engine = create_engine("mysql://root:1234@localhost:3306/IDS")

QUERY_ANADIR_CASO = "INSERT INTO casos (direccion, adultos, menores) VALUES (:direccion, :adultos, :menores)"
QUERY_TODOS_LOS_CASOS = "SELECT * FROM casos"

# Función genérica para ejecutar cualquier consulta SQL
def run_query(query, parameters=None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), parameters)
            conn.commit()  # Esto solo es necesario si haces un INSERT o UPDATE
            return result
    except SQLAlchemyError as e:
        print(f"Error ejecutando la consulta: {e}")
        return None

# Función para añadir un caso
def anadir_caso(data):
    run_query(QUERY_ANADIR_CASO, data)

# Función para obtener todos los casos
def todos_los_casos():
    result = run_query(QUERY_TODOS_LOS_CASOS)  # Ejecuta la consulta sin parámetros
    if result:
        return result.fetchall()  # Devuelve todos los resultados
    else:
        return []  # Retorna una lista vacía si no hubo resultados

