import psycopg2

# configuracion de la base de datos Postgresql en heroku
db_config = {
    "database": "d5u56kni3um77a",
    "user": "ukchpuavegpheb",
    "password": "ad095992acb291af6fe26c1cd14dc9ede49be425d30c2477a244e2d575ede031",
    "host": "ec2-107-22-7-9.compute-1.amazonaws.com",
    "port": 5432
}

def select_query(query, config=db_config):
    cursor = None
    try:
        connection = psycopg2.connect(**config)
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
        connection = psycopg2.connect(**config)
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
