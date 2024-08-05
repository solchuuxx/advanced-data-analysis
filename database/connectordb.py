import mysql.connector
from mysql.connector import Error

db_connection = None

def create_connection():
    global db_connection
    try:
        if db_connection is None or not db_connection.is_connected():
            db_connection = mysql.connector.connect(
                host='localhost',
                database='CompanyData',
                user='root',
                password=''
            )
            if db_connection.is_connected():
                db_info = db_connection.get_server_info()
                print("Conectado al servidor MySQL versión ", db_info)
                cursor = db_connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Conectado a la base de datos: ", record)
        return db_connection
    except Error as e:
        print("Error durante la conexión a MySQL", e)
        return None

def close_connection():
    global db_connection
    if db_connection is not None and db_connection.is_connected():
        db_connection.close()
        print("Conexión a MySQL cerrada")





