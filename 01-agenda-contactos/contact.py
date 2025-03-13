from sqlite3 import Error
import sqlite3


# insert contact
def insert_contact(nombres, apellidos, empresa, telefono, email, direccion):
    try:

        with sqlite3.connect('./contactos.db') as conn:
            cursor = conn.cursor()
            query = """INSERT INTO contacto(nombres, apellidos, empresa, telefono, email, direccion)
                VALUES(?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (nombres, apellidos, empresa, telefono, email, direccion))
            conn.commit() # se usa commint dentro del with para asegurar que se guarden los cambios

        return f"Contacto registrado"
    except Error as err:
        return f"Error al registrar contacto: {err}"

# get all contacts 
def get_contacts():
    try:
        with sqlite3.connect('./contactos.db') as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM contacto"
            cursor.execute(query)
            return cursor.fetchall()
    except Error as err:
        return f"Erro al traer todos los contactos: {err}"
    
# get one contact
def get_contact(id):
    try:
        with sqlite3.connect('./contactos.db') as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM contacto WHERE id = ?"
            cursor.execute(query, (id,))
            return cursor.fetchone()
    except Error as err:
        return(f"Error al buscar el contacto: {err}")
    
# update contact
def update_contact(id, nombres, apellidos, empresa, telefono, email, direccion):
    try:
        with sqlite3.connect('./contactos.db') as conn:
            cursor = conn.cursor()
            query = """ UPDATE contacto SET nombres=?, apellidos=?, empresa=?, telefono=?, email=?, direccion=?
            WHERE id=?"""
            cursor.execute(query, (nombres, apellidos, empresa, telefono, email, direccion, id))
            conn.commit()
        return "Contacto actualizado"
    except Error as err:
        return f"Error al actualizar usuario: {err}"
    
# delete contact
def delete_contact(id):
    try:
        with sqlite3.connect('./contactos.db') as conn:
            cursor = conn.cursor()
            query = "DELETE FROM contacto WHERE id=?"
            cursor.execute(query, (id,))
        return "Contacto eliminado"
    except Error as err:
        return f"Error al eliminar el contacto: {err}"