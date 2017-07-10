from django.template import Library

register=Library()

@register.filter
def desc_handle(value):
    if value is None:
        return 1
    return int(value)*(-1)