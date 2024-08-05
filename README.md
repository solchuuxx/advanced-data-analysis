# Práctica de Librerías - Python

## Objetivo
Desarrollar un script en Python que permita realizar operaciones de análisis de datos avanzados utilizando `numpy` y `pandas`, extrayendo información de una base de datos MySQL, y visualizando los resultados con `matplotlib`.

## Desarrollo

1. Crear, Configurar y Activar un Entorno Virtual

Para mantener las dependencias del proyecto aisladas, se recomienda crear y activar un entorno virtual.

```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar Dependencias

Instalar las siguientes dependencias necesarias para el proyecto:

```sh
pip install mysql-connector-python
pip install pandas
pip install matplotlib
pip install numpy
```

3. Crear y Configurar la Base de Datos

Ejecutar el siguiente script para establecer la conexión con la base de datos:

```sh
py ./database/connectordb.py
```

4. Crear la Base de Datos y Poblar Datos

Crear una base de datos llamada “CompanyData” y ejecutar los siguientes scripts para crear las tablas necesarias y poblarlas con datos:

```sh
py ./database/createdb.py
py ./database/populatedb.py
```

5. Ejecutar el Script Principal

Por último, ejecutar el archivo main.py para leer y visualizar los datos estadísticos de los empleados:

```sh
py main.py
```
