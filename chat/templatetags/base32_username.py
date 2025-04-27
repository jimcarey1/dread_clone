from django import template
from utils.chat import to_base32

register = template.Library()

@register.filter
def username_to_base32(username:str) -> str:
    return to_base32(username)
