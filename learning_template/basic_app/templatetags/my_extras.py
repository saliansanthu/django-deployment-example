from django import template

register = template.Library()

def s_c(value,arg):
    """
    This cuts out all values of 'arg' from the String!
    """
    return value.replace(arg, '')

register.filter('s_c',s_c)

@register.filter(name='l_n')
def l_n(value):
    return value+' salian'
