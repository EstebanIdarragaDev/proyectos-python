from os import system
from tabulate import tabulate # pip install tabulate -> global
from connection import connection,create_table
from contact import insert_contact, get_contacts, get_contact, update_contact, delete_contact

# Initialization
conn = connection()
create_table(conn)


def start():

    menu = """ \nSeleccione una opcion:
    \t1.Añadir contacto
    \t2.Mostrar todos los contactos
    \t3.Buscar contacto
    \t4.Modificar contacto
    \t5.Eliminar contacto
    \t6.Salir\n"""

    estado = True
    while estado:
        # clear_terminal()
        print(menu)
        option = input("Ingrese una opcion: #")
        estado = process_option(option)



def process_option(option):
    clear_terminal()
    match option:
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
            return False
        case _:
            print('Opcion no valida')
    return True      


# option - new contact
def new_contact():
    print("Resgistrar Contacto : ")
    nombres = input("Ingrese los nombres: ").strip().lower()
    apellidos = input("Ingrese los apellidos: ").strip().lower()
    empresa = input("Ingrese la empresa: ").strip().lower()
    telefono = input("Ingrese el telefono: ").strip()
    email = input("Ingrese el email: ").strip().lower()
    direccion = input("Ingrese la direccion: ").strip().lower()

    print(insert_contact(nombres, apellidos, empresa, telefono, email, direccion))

# option - get contacts
def show_contacts():
    print("Todos los contactos: ")
    contacts = get_contacts()
    print(create_visual_table(contacts))

# option - get contact
def show_contact():
    print("Contacto: ")
    id_contact = input('Ingrese el id del contacto: ')
    contact = [get_contact(id_contact)]
    print(create_visual_table(contact))

# option - update
def upt_contact():
    print("Modificar Contacto : ")
    id_contact = input("Ingrese el id del contacto: ")
    nombres = input("Ingrese los nombres: ").strip().lower()
    apellidos = input("Ingrese los apellidos: ").strip().lower()
    empresa = input("Ingrese la empresa: ").strip().lower()
    telefono = input("Ingrese el telefono: ").strip()
    email = input("Ingrese el email: ").strip().lower()
    direccion = input("Ingrese la direccion: ").strip().lower() 

    print(update_contact(id_contact, nombres, apellidos, empresa, telefono, email, direccion))

# option - delete
def del_contact():
    print('Eliminar contacto: ')
    id_contact = input("Ingrese el id del contacto: ")
    resp = delete_contact(id_contact)
    print(resp)


# clear the terminal
def clear_terminal():
    system('cls')

# crete table with tabulate
def create_visual_table(data):
    headers = ['ID', 'NOMBRE', 'APELLIDOS', 'EMPRESA', 'TELEFONO', 'EMAIL', 'DIRECCION']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    return table


start()