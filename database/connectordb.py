import mysql.connector
from mysql.connector import Error

#Encapsulamiento
class DatabaseConnector:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def create_connection(self):
        raise NotImplementedError("")

    def close_connection(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

#Herencia
class MySQLConnector(DatabaseConnector):
    def __init__(self, host='localhost', database='CompanyData', user='root', password=''):
        super().__init__(host, database, user, password)

    def create_connection(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                if self.connection.is_connected():
                    db_info = self.connection.get_server_info()
                    print("Conectado al servidor MySQL versión ", db_info)
                    cursor = self.connection.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("Conectado a la base de datos: ", record)
            return self.connection
        except Error as e:
            print("Error durante la conexión a MySQL", e)
            return None
