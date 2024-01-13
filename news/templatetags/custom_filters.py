import re

from django import template


register = template.Library()
@register.filter(name='censor')
def censor(value):

    unwanted_words=['Заголовок_новости_2']
    for word in unwanted_words:
        value = re.sub(r'\b'+ re.escape(word)+r'\b','+'*len(word), value, flags=re.IGNORECASE)

    return {value}
