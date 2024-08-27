from connectordb import MySQLConnector

class DatabaseInitializer:
    def __init__(self, connector):
        self.connector = connector

    def initialize_database(self):
        db_connection = self.connector.create_connection()
        if db_connection:
            cursor = db_connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData")
            cursor.execute("USE CompanyData")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS EmployeePerformance (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    employee_id INT,
                    department VARCHAR(255),
                    performance_score DECIMAL(5,2),
                    years_with_company INT,
                    salary DECIMAL(10,2)
                )
            """)
            db_connection.commit()
            cursor.close()
            self.connector.close_connection()
        else:
            print("No se pudo establecer la conexión a la base de datos")

if __name__ == "__main__":
    connector = MySQLConnector()
    initializer = DatabaseInitializer(connector)
    initializer.initialize_database()
