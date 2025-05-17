# templatetags/translate_text.py
from django import template
from .models import TranslatableText
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag
def trans_text(key):
    lang = get_language()[:2]
    try:
        return TranslatableText.objects.get(key=key, lang=lang).text
    except TranslatableText.DoesNotExist:
        return f"[{key}]"
