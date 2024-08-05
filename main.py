import pandas as pd
import numpy as np
from database.connectordb import create_connection, close_connection
import matplotlib.pyplot as plt

db_connection = create_connection()
if db_connection:
    query = "SELECT * FROM EmployeePerformance"
    df = pd.read_sql(query, db_connection)

    pd.set_option('display.max_rows', None)
    
    #Estadísticas por departamento
    stats = df.groupby('department').agg({
        'performance_score': ['mean', 'median', 'std'],
        'salary': ['mean', 'median', 'std'],
        'employee_id': 'count'
    }).rename(columns={'employee_id': 'total_employees'})
    
    stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
    
    #Correlaciones
    correlations = df.groupby('department').apply(lambda x: pd.Series({
        'corr_years_performance': x['years_with_company'].corr(x['performance_score']),
        'corr_salary_performance': x['salary'].corr(x['performance_score'])
    }))
    
    #Unir estadísticas y correlaciones
    result = stats.join(correlations)
    
    print(result)

    #histograma del performance_score para cada departamento
    departments = df['department'].unique()
    for department in departments:
        subset = df[df['department'] == department]
        plt.hist(subset['performance_score'], bins=10, alpha=0.5, label=department)
    plt.xlabel('Performance score')
    plt.ylabel('Frequency')
    plt.title('Histogram of Performance Score by Department')
    plt.legend()
    plt.show()
    
    #gráfico de dispersión de years_with_company vs performance_score
    plt.scatter(df['years_with_company'], df['performance_score'])
    plt.xlabel('Years with Company')
    plt.ylabel('Performance Score')
    plt.title('Scatter Plot of Years with company vs. Performance Score')
    plt.show()
    
    #gráfico de dispersión de salary vs performance_score
    plt.scatter(df['salary'], df['performance_score'])
    plt.xlabel('Salary')
    plt.ylabel('Performance Score')
    plt.title('Scatter Plot of Salary vs. Performance Score')
    plt.show()

    #media y desviacion estandar de performance_score usando NUMPY
    performance_scores = df['performance_score'].values
    mean_performance = np.mean(performance_scores)
    std_performance = np.std(performance_scores)
    
    print(f"Mean performance Score: {mean_performance}")
    print(f"Standard Deviation of Performance Score: {std_performance}")
    
    close_connection()


else:
    print("No se pudo establecer la conexión a la base de datos")
