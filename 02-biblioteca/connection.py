import mysql.connector as mysql;

def connection():
    try:
        conn = mysql.connect(
            host='localhost',
            user='root',
            password='1582',
            database='libros'
            )
        print('Se ha conectado a la base de datos ...')
        return conn
    except mysql.Error as err:
        print('Ha ocurrido un error al conectarse a la DB: ' + err)