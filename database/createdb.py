from connectordb import create_connection, close_connection

db_connection = create_connection()
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
    close_connection()
else:
    print("No se pudo establecer la conexión a la base de datos")


