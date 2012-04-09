from django import template
import types

register = template.Library()

@register.filter
def startswith(value, arg):
    if type(value) is types.NoneType:
        return False
    return value.startswith(arg)
