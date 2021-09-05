import json
from database import *

def extract_route(req):
    if req.startswith("GET") or req.startswith("POST"):
        lista1 = req.split(" /")
        lista2 = lista1[1].split(" ")
        return lista2[0]
    return ''

def read_file(path):
    list = str(path).split(".")
    if list[-1] == "txt" or list[-1] == "html" or list[-1] == "css" or list[-1] == "js":
        with open(path,"rt") as file:
            text = file.read()
            return text
    else:
        with open(path,"rb") as file:
            binary = file.read()
            return binary

def load_data(fileName):
    path = 'data/' + fileName
    with open(path, 'r', encoding='UTF-8') as jsonFile:
        data = json.load(jsonFile)
    return(data)

def load_template(fileName):
    path = 'templates/' + fileName
    with open(path, 'r', encoding='UTF-8') as htmlFile:
        read = htmlFile.read()
    return read

def addToJson(dict):
    # with open('data/notes.json', 'r') as jsonFile:
    #     jsonObject = json.load(jsonFile)
    
    # jsonObject.append(dict)

    # with open('data/notes.json', 'w', encoding='UTF-8') as jsonFile:
    #     json.dump(jsonObject, jsonFile)
    db = Database('note')
    newData = Note(title=dict['titulo'], content=dict['detalhes'])
    db.add(newData)


def build_response(body='', code=200, reason='OK', headers=''):
    defaultResponse = "HTTP/1.1 " + str(code) + " " + reason
    
    if headers != '':
        defaultResponse += f"\n{headers}"
    
    defaultResponse+=f"\n\n{body}"

    return (defaultResponse).encode()
    
    