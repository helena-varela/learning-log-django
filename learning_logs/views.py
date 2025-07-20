from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    """Página principal do Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adiciona uma nova entrada."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}    
    return render(request, 'learning_logs/new_entry.html',context) 

def edit_entry(request, entry_id):
    """Editar uma entrada"""
    entry = Entry.objects.get(id=entry_id)
    if request.method == 'POST':
        entry_text = request.POST.get("entry-text")
        entry.text = entry_text
        entry.save()
        return HttpResponseRedirect(reverse('topic', args =[entry.topic.id]))

    context = {'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)

def delete_entry(request, entry_id):
    """Deletar uma entrada"""
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return HttpResponseRedirect(reverse('topic', args = [entry.topic.id]))
    