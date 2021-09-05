from database import *

db = Database('note')

# db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
# db.add(Note(title=None, content='Lembrar de tomar água'))

# notes = db.get_all()
# for note in notes:
#     print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

# update = notes[1]
# update.title = 'Pão salgado'
# update.content = 'ha, thats pog champ'
# db.update(update)