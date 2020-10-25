from django import template



register = template.Library()


@register.filter
def mod(ind,div):
    return ind % div


@register.filter
def vala(ind,total):
    if(ind < len(total)/4 ):
        return 1
    else:
        return 1