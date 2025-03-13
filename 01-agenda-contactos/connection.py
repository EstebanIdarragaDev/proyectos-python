import sqlite3

# Database connection
def connection():
    try:
        conn = sqlite3.connect("contactos.db")
        return conn
    except sqlite3.Error as err:
        print(f"Ha oucrrido un error al conectarse a la DB. ${err}")


# Initial table
def create_table(conn):
    try:
        cursor = conn.cursor()
        query = """ CREATE TABLE IF NOT EXISTS contacto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres VARCHAR(50) NOT NULL,
            apellidos VARCHAR(50) NOT NULL,
            empresa VARCHAR(50) NOT NULL,
            telefono VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            direccion VARCHAR(20) NOT NULL
        )"""
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        print(f"Error al crear la tabla contactos ... {err}")