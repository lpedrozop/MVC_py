import conversion as conversion

from controller import *

view: Flask = Flask(__name__)
bootstrap = Bootstrap(view)

def main():
    EntrarDatos()
    print('Console')
    while True:
        conversion(lista)
        if len(lista) == 0:
            opcion = int(input("Menu\n [1] Añadir\n [2] Exit\nDigite la opcion: "))
            if opcion == 1:
                insertar()
            elif opcion == 2:
                break
            else:
                print("Opcion errada")
        else:
            opcion = int(input("Menú\n 1.Datos\n 2.Entrar datos\n 3.Editar datos digitados\n"
                               " 4.Eliminar datos digitados\n 5. Salir \nEscoja opción: "))
            if opcion == 1:
                visualizar()
            elif opcion == 2:
                insertar()
            elif opcion == 3:
                modificar(input("Digite el codigo de la persona que desea modificar: "))
            elif opcion == 4:
                eliminar(input("Digite el codigo de la persona que desea eliminar: "))
            elif opcion == 5:
                break
            else:
                print("Opcion errada")

def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')




def end_view():
    print('Goodbye!')
