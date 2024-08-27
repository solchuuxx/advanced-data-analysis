import pandas as pd
from connectordb import MySQLConnector

class DatabasePopulator:
    def __init__(self, connector, data_file):
        self.connector = connector
        self.data_file = data_file

    def populate_database(self):
        df = pd.read_csv(self.data_file)
        db_connection = self.connector.create_connection()
        if db_connection:
            cursor = db_connection.cursor()
            for i, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
                    VALUES (%s, %s, %s, %s, %s)
                """, (row['employee_id'], row['department'], row['performance_score'], row['years_with_company'], row['salary']))
            db_connection.commit()
            print("Datos insertados exitosamente")
            cursor.close()
            self.connector.close_connection()
        else:
            print("No se pudo establecer la conexión a la base de datos")

if __name__ == "__main__":
    connector = MySQLConnector()
    populator = DatabasePopulator(connector, './DATA.csv')
    populator.populate_database()
