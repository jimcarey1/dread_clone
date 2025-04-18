from django.db import models

# Create your models here.
from user.models import User

class Chat(models.Model):
    message = models.CharField(max_length=100)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.DO_NOTHING)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_messages'

