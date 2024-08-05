import pandas as pd
from connectordb import create_connection, close_connection

df = pd.read_csv('./DATA.csv')

db_connection = create_connection()
if db_connection:
    cursor = db_connection.cursor()
    
    #Insertar datos del dataframe a la base de datos
    for i, row in df.iterrows():
        cursor.execute("""
            INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['employee_id'], row['department'], row['performance_score'], row['years_with_company'], row['salary']))
    
    db_connection.commit()
    print("Datos insertados exitosamente")

    cursor.close()
    close_connection()
else:
    print("No se pudo establecer la conexión a la base de datos")
