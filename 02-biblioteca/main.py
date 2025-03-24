from os import system
from tabulate import tabulate

from connection import connection
from book import insert_book, get_books, get_book, update_book, delete_book
conn = connection()


def init():
    menu = """
Seleccione una de las opciones:
1.\tAñadir un libro
2.\tVer todos los libros
3.\tBuscar un libro
4.\tModificar un libro
5.\tEliminar un libro
6.\tSalir
"""
    estado = True
    while estado:
        # clear_console()
        print(menu)
        option = input("Elije un opcion: ")
        estado = process_option(option)

# Validate the option user
def process_option(option):
    clear_console()
    match option:
        case '1':
            new_book()
        case '2':
            show_books()
        case '3':
            show_book()
        case '4':
            upt_book()
        case '5':
            del_book()
        case '6':
            return False
        case '_':
            print('Opcion no valida')
    return True


# clear the console
def clear_console():
    system('cls')

# insert book
def new_book():
    print("Registrar libro: ")
    nombre = input("Ingrese el nombre del libro: ").strip().lower()
    autor = input("Author del libro: ").strip().lower()
    estado = input("Estado del libro: ").strip().lower()

    if nombre and autor and estado:
        print(insert_book(nombre, autor, estado))
        show_books()
    else:
        print("Debes completar todos los campos")

# show alll books
def show_books():
    print('Biblioteca: ')
    books = get_books()

    if books:
        print(create_visual_table(books))
    else:
        print('La biblioteca esta vacia :(')

# show book
def show_book():
    print('Buscar libro: ')
    id_book = input('Que libros deseas buscar ? id: ')
    book = get_book(id_book)
    if book:
        print(create_visual_table(book))
    else:
        print('Vaya, no se encontro ese libro')

# update book
def upt_book():

    id_book = input('Ingresa el id del libro a modifcar: #')

    if valide_book(id_book):
        print("""
    Actulizar informacion

    Que campo deseas actualizar ?
    1.Titulo
    2.Autor
    3.Estado
    """)
        option = input('Campo: #')
        new_value = ''

        match option:
            case '1':
                new_value = input('Ingresa el nuevo titulo: ')
            case '2':
                new_value = input('Ingresa el nuevo autor: ')
            case '3':
                new_value = input('Ingresa el nuevo estado: ')
            case '_':
                print('Opcion no valida')
                return
        print(update_book(id_book ,option, new_value))
    else:
        print('Vaya, parece que ese libro no existe')

# Delete book
def del_book():
    get_books()
    id_book = input('Ingresa el id del libro a eliminar: #')
    if valide_book(id_book):
        print(delete_book(id_book))
    else:
        print('Parece que ese libro no existe')




# validate if a book exists
def valide_book(id):
    if get_book(id)[0]:
        return True
    else:
        return False
# table
def create_visual_table(data):
    headers = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    return table




init()