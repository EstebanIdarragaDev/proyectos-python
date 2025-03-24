from connection import connection
from mysql.connector import Error

def insert_book(titulo, autor, estado):
    try:
        conn = connection()
        cursor = conn.cursor()
        query = """INSERT INTO libro(titulo, autor, estado)
                   VALUES(%s, %s, %s)
                """
        cursor.execute(query, (titulo, autor, estado))
        conn.commit()
        conn.close()
        return "Libro resgistrado..."
    except Error as err:
        print('Error al registrar el libro: ' + err)


def get_books():
    datos = []
    try:
        conn = connection()
        cursor = conn.cursor()
        query = "SELECT * FROM libro"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        return datos
    except Error as err:
        print("Error al obtener todos los libros: " + err)

def get_book(id):
    datos = []
    try:
        conn = connection()
        cursor = conn.cursor()
        query = "SELECT * FROM libro WHERE id=%s"
        cursor.execute(query, (id,))
        datos.append(cursor.fetchone())
        conn.close()
        return datos
    except Error as err:
        print('Error al obtener el libro: ' + err)


def update_book(id,campo, nuevo_valor):
    try:
        conn = connection()
        cursor = conn.cursor()
        query = ''

        match campo:
            case '1':
                query = "UPDATE libro SET titulo=%s WHERE id=%s"
            case '2':
                query = "UPDATE libro SET autor=%s WHERE id=%s"
            case '3':
                query = "UPDATE libro SET estado=%s WHERE id=%s"

        cursor.execute(query, (nuevo_valor,id))
        conn.commit()
        conn.close()
        return 'Libro actualizado'
    except Error as err:
        print('Error al actualizar el libro')

def delete_book(id):
    try:
        conn = connection()
        cursor = conn.cursor()
        query = "DELETE FROM libro WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return 'Libro eliminado...'
    except Error as err:
        print('Error al eliminar el libro: ' + err)