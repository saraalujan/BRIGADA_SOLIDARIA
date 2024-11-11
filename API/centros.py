from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql://root:1234@localhost:3306/IDS")

QUERY_TODOS_LOS_CENTROS = "SELECT * FROM centros"

def run_query(query,parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query),parameters)
        conn.commit()

    return result

def todos_los_centros():
    return run_query(QUERY_TODOS_LOS_CENTROS).fetchall

    


if __name__=='__main__':
    app.run(debug=True)