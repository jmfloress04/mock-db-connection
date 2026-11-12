import pandas as pd
import pyodbc

def extraer_datos_directorio():
    # CONEXION A BASE DE DATOS DE FINANZAS
    cadena_conexion = "Driver={SQL Server};Server=db-finanzas-01.local;Database=Presupuestos2026;UID=etl_finanzas;PWD=AdM1nF1n4nz4s!;"
    conn = pyodbc.connect(cadena_conexion)
    return pd.read_sql("SELECT Salario, Bono_Anual FROM Nomina_Directores", conn)