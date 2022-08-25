import json


lista = []


def EntrarDatos():
    try:
        db = open('db.json', 'r')
        info = db.read()
        diccionario = json.loads(info)
        for key, value in diccionario.items():
            person = Person(key, value['name'], value['last_name'])
            lista.append(person)
    except json.decoder.JSONDecodeError:
        return

def conversion(data: list = lista):
    datos = {}
    for item in data:
        datos[item.id_person] = {'name': item.name, 'last_name': item.last_name}

    with open('db.json', 'w') as file:
        json.dump(datos, file)
        file.close()

def visualizar():
    for person in lista:
        print(person)



class Person(object):

    def __init__(self, ID=None, first_name=None, last_name=None):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name



    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1} {2}".format(self.ID, self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                person = Person(p['ID'], p['first_name'], p['last_name'])
                result.append(person)
        return result






