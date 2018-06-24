from django import template
register = template.Library()


@register.filter(name="add_str")
def add_str(value, arg):
    return "{} {}".format(value,arg)


@register.filter(name="add_diy_str")
def add_diy_str(value):
    return "{} add_diy_str".format(value)