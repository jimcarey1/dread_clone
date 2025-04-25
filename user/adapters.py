from allauth.account.adapter import DefaultAccountAdapter
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class CustomAccountAdapter(DefaultAccountAdapter):
    def generate_unique_username(self, txts, regex=None):
        base_username = slugify(txts[0])[:30] if txts else "user"
        username = base_username
        i = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{random.randint(100, 999)}"
            i += 1
        return username
