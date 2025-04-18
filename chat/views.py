from django.shortcuts import render

def chat_view(request, username):
    return render(request, 'chat/chat.html', {'username': username})
