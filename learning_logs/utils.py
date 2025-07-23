from django.http import Http404

def verificar_user(request, topic, mensagem = ''):
    """Função que verifica se o tópico pertence ao usuário"""
    if topic.owner != request.user:
        raise Http404(mensagem)