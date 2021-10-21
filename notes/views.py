from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note, Tag
from .serializers import NoteSerializer


def index(request):
   
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')

        tag, create = Tag.objects.get_or_create(name=tag)

        if create:
            tag.save()

        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title=title, content=content, tag=tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):

    id = request.POST.get('id')
    note = Note.objects.filter(id=id)
    note_with_tag = Note.objects.filter(tag=note[0].tag)
    
    if len(note_with_tag) <= 1:
        note.delete()
        note_with_tag[0].tag.delete()
    else:
        note.delete()

    return redirect('index')

def update(request):
    
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    tag = request.POST.get('tag')
    note = Note.objects.filter(id=id)

    tag, create = Tag.objects.get_or_create(name=tag)

    if create:
        tag.save()

    note.update(title=title, content=content, tag=tag)

    return redirect('index')

def tagsPage(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tagsFilter(request, tagName=None):
    if tagName != None:
        tags = Tag.objects.filter(name=tagName)
        tag = tags[0]
        notes = Note.objects.filter(tag=tag)
        print(notes)
    return render(request, 'notes/tagsFilter.html', {'notes': notes, 'tags': tags})

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)