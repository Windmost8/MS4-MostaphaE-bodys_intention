"""bagtools py for bag app"""
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """function to calculate subtotal"""
    return price * quantity
