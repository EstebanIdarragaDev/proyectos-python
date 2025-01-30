import sqlite3

# 
def connect():
    try:
        conn = sqlite3.connect('contactos.db')
        print("Se ha conectado a la base de datos ...")
        return conn
    except sqlite3.Error as err:
        print(f"Ha ocurrido un error al conectarse a la bd: {err}")

def create_table(conn):
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS contacto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        apellidos VARCHAR(50) NOT NULL,
        empresa VARCHAR(50) NOT NULL,
        telefono VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        direccion VARCHAR(50) NOT NULL
    )"""
    cursor.execute(query)
    conn.commit()
