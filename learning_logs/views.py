from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import utils
# Create your views here.

def index(request):
    """Página principal do Learning Log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    utils.verificar_user(request, topic)
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    else:
        form = TopicForm()
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada."""
    topic = Topic.objects.get(id=topic_id)
    utils.verificar_user(request, topic)

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

@login_required
def edit_entry(request, entry_id):
    """Editar uma entrada"""
    entry = Entry.objects.get(id=entry_id)
    utils.verificar_user(request, entry.topic)

    if request.method == 'POST':
        entry_text = request.POST.get("entry-text")
        entry.text = entry_text
        entry.save()
        return HttpResponseRedirect(reverse('topic', args =[entry.topic.id]))

    context = {'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def edit_topic(request, topic_id):
    """Editar tópico"""
    topic = Topic.objects.get(id=topic_id)
    utils.verificar_user(request, topic)
    if request.method == 'POST':
        topic_text = request.POST.get("topic-text")
        topic.text = topic_text
        topic.save()
        return HttpResponseRedirect(reverse('topic', args =[topic.id]))

    context = {'topic': topic}
    return render(request, 'learning_logs/edit_topic.html', context)

@login_required
def delete_entry(request, entry_id):
    """Deletar uma entrada"""
    entry = Entry.objects.get(id=entry_id)
    utils.verificar_user(request, entry.topic, "Não apague a entrada dos outros usuários")
    entry.delete()
    return HttpResponseRedirect(reverse('topic', args = [entry.topic.id]))

@login_required  
def delete_topic(request, topic_id):
    """Deleta um tópico"""
    topic = Topic.objects.get(id=topic_id)
    utils.verificar_user(request, topic, "Você não pode apagar o tópico de outro usuário")
    topic.delete()  
    return HttpResponseRedirect(reverse('topics'))