from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from user.models import User 
from .models import Chat
from utils.chat import base32_to_original

@login_required
def chat_view(request, base32_username:str):
    username = base32_to_original(base32_username)
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    messages = Chat.objects.filter(
        Q(sender=sender, recipient=receiver) |
        Q(sender=receiver, recipient=sender)
    ).order_by('sent_on')
    return render(request, 'chat/chat.html', {'messages':messages, 'username':username, 'receiver':receiver})
