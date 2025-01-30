from connection import connect
from sqlite3 import Error


# Insertar contacto
def insert_contact(nombre, apellidos, empresa, telefono, email, direccion):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = """INSERT INTO contacto(nombre, apellidos, empresa, telefono, email, direccion)
            VALUES (?,?,?,?,?,?)"""
        data = (nombre, apellidos, empresa, telefono, email, direccion)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        return 'Contacto registrado'
    except Error as err:
        return f'Error al registrar contacto: {err}'

# Obtener todos los contactos 
def get_contacts():
    data = []
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT * FROM contacto"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    except Error as err:
        return f'Error al buscar los contactos: {err}'
    
# Obtener un contacto
def get_contact(id):
    data = []
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT * FROM contacto WHERE id=?"
        cursor.execute(query,(id,))
        data.append(cursor.fetchone())
        conn.close()
        return data
    except Error as err:
        return f'Error al buscar contacto: {err}'
    
def update_contact(nombre, apellidos, empresa, telefono, email, direccion, id):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = """UPDATE contacto set nombre=?, apellidos=?, empresa=?, telefono=?, email=?, direccion=? 
        where id=?"""
        data = (nombre, apellidos, empresa, telefono, email, direccion, id)
        cursor.execute(query,data)
        conn.commit()
        conn.close()
        return 'Contacto actualizado'
    except Error as err:
        return f'Error al actualizar contacto {err}'
        
def delete_contact(id):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "DELETE FROM contacto WHERE id=?"
        cursor.execute(query,(id,))
        conn.commit()
        conn.close()
        return 'Contacto eliminado'
    except Error as err:
        return f'Error al eliminar usuario'