from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

import view
from model import *
from view import *

st_web: Flask = Flask(__name__)
bootstrap = Bootstrap(st_web)
model = []


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


@st_web.route("/")
def start_web():
    result = list()
    with open('db.json') as json_file:
        data = json.load(json_file)
        for p in data['employees']:
            person = Person(p['ID'], p['first_name'], p['last_name'])
            result.append(person)
    return render_template("people.html", value=result)


@st_web.route('/person_delete/<string:id>')
def person_delete(ID):
    for person in model:
        if person.id_person == ID:
            model.remove(person)

    return redirect('/people')


@st_web.route('/perupdate', methods=['POST'])
def perupdate():
    model.remove('ID')
    show_all()

    return render_template('person_detail.html', value=show_all())


@st_web.route('/person_update/<string:id>', methods=['GET'])
def person_update(id, get=None):
    data = 0
    data = get.all()

    return render_template('person_update.html', data=show_all())


def insertar():
    id = int(input("ID: "))
    nombre = input("First name: ")
    apellido = input("Last Name: ")
    p = Person(id_person=id, name=nombre, last_name=apellido)
    lista.append(p)
    print("Datos anexados con exito")


def modificar(id_modificar):
    for person in lista:
        if person.id_person == id_modificar:
            nombre = input('Digite el nombre modificado: ')
            apellido = input('Digite el apellido modificado: ')
            person.name = nombre
            person.last_name = apellido
            print('Nuevo dato \n Nombre: {person.name}\n Apellido: {person.last_name}')


def eliminar(id_eliminar):
    for persona in lista:
        if persona.id_person == id_eliminar:
            lista.remove(persona)
            print("[Datos eliminados con exito")


def menu():
    if int(input("\n [1] Vista por consola\n [2] Vista por Web\n Digite la opción que desee realizar: ")) == 1:
        main()

    st_web.run()


if __name__ == "__main__":
    # running controller function
    EntrarDatos()
    model = lista
    menu()
