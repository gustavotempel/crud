import os
import psycopg2

# configuracion de la base de datos Postgresql en heroku
# postgres://{user}:{password}@{hostname}:{port}/{database-name}
db_config = "postgres://wdkomuwjqgepfl:35cfd3946b5ca4336c9dda475fd7e0ccd39d2975882b162186f8e9a81f9aef91@ec2-34-237-89-96.compute-1.amazonaws.com:5432/dfrlvq3e2betas"

try:
    db_config = os.environ['DATABASE_URL']
except:
    pass

def select_query(query, config=db_config):
    cursor = None
    try:
        connection = psycopg2.connect(config, sslmode="require")
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as error:
        print("Error al conectar a la base de datos.", error)
    finally:
        if cursor:
            cursor.close()
            print("Cursor cerrado")
        if connection:
            connection.close()
            print("Conexión terminada")
    

def modify_query(query, config=db_config):
    cursor = None
    try:
        connection = psycopg2.connect(config, sslmode="require")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as error:
        print("Error al conectar a la base de datos.", error)
    finally:
        if cursor:
            cursor.close()
            print("Cursor cerrado")
        if connection:
            connection.close()
            print("Conexión terminada")
