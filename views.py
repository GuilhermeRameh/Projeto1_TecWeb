from utils import *
from database import Database, Note
import urllib

db = Database('data/note')

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[chave] = urllib.parse.unquote_plus(valor, encoding='utf-8', errors='replace')     


        if params["method"] == "POST":
            writeNote(params)
        elif params['method'] == 'DELETE':
            db.delete(params['id'])
        elif params['method'] == 'UPDATE': 
            note = Note(id=params["id"], title=params["title"], content=params["details"])
            print(f'\n\n\n{note}\n\n\n')
            db.update(note)
            

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))

