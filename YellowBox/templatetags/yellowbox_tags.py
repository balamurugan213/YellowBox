from django import template



register = template.Library()


@register.filter
def mod(ind,div):
    return ind % div