from django import template
import books.views as views

register = template.Library()

register.inclusion_tag('header_and_footer/header.html')
def menu():
    return