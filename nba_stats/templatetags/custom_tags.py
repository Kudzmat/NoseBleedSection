from django import template

register = template.Library()


#  This custom filter will change a decimal figure into a percentage
@register.filter
def percentage(value):
    return format(value, ".2%")  # at 2 decimal places
