from os import system
from tabulate import tabulate # pip install tabulate
from connection import connect, create_table
from contact import insert_contact, get_contacts, get_contact, update_contact, delete_contact


# Inicializacion
conn = connect()
create_table(conn)


def start():
    estado = True

    while estado:
        menu = """Selecione una opcion: 
    \t1.Añadir contacto
    \t2.Mostrar todos los contactos
    \t3.Buscar contacto
    \t4.Modificar contacto
    \t5.Eliminar contacto
    \t6.Salir"""
        print(menu)
        opcion = input('Elije una opcion: ')
        
        match opcion:
            case '1':
                new_contact()
            case '2':
                show_contacts()
            case '3':
                show_contact()
            case '4':
                upt_contact()
            case '5':
                del_contact()
            case '6':
                estado = False
            case _:
                print('Opcion no valida')



# Ingresar un nuevo contacto
def new_contact():
    system('cls')
    print('Ingresa los siguiente datos')
    nombre = input('Ingresa el nombre del contacto: ')
    apellidos = input('Ingresa los apellidos del contacto: ')
    empresa = input('Ingresa la empresa del contacto: ')
    telefono = input('Ingresa el telefono del contacto: ')
    email = input('Ingresa el email del contacto: ')
    direccion = input('Ingresa el direccion del contacto: ')

    res = insert_contact(nombre, apellidos, empresa, telefono, email, direccion)
    print(res)

# Mostrar todos los contactos
def show_contacts():
    system('cls')
    contacts = get_contacts()
    headers = ['ID', 'NOMBRE', 'APELLIDOS', 'EMPRESA', 'TELEFONO', 'EMAIL', 'DIRECCION']
    table = tabulate(contacts, headers, tablefmt='fancy_grid')
    print(table)

# Mostrar un contacto
def show_contact():
    system('cls')
    id_contact = input('Ingresa el id del contacto: ')
    contact = get_contact(id_contact)
    headers = ['ID', 'NOMBRE', 'APELLIDOS', 'EMPRESA', 'TELEFONO', 'EMAIL', 'DIRECCION']
    table = tabulate(contact, headers, tablefmt='fancy_grid')
    print(table)

# Modificar un contacto
def upt_contact():
    system('cls')
    print('Ingresa los siguientes datos')
    nombre = input('Ingresa el nombre del contacto: ')
    apellidos = input('Ingresa los apellidos del contacto: ')
    empresa = input('Ingresa la empresa del contacto: ')
    telefono = input('Ingresa el telefono del contacto: ')
    email = input('Ingresa el email del contacto: ')
    direccion = input('Ingresa el direccion del contacto: ')
    id_contact = input('Ingresa el id del contacto: ')
    res = update_contact(nombre, apellidos, empresa, telefono, email, direccion,id_contact)
    print(res)
    show_contacts()

# Eliminar contacto
def del_contact():
    system('cls')
    id_contact = input('Ingrese el id del contacto: ')
    res = delete_contact(id_contact)
    show_contacts()
start()