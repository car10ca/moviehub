#this is used to format the numbers from the budget and gross of movies

from django import template

register = template.Library()

@register.filter
def currency(value):
    return "${:,.2f}".format(value)
