from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def subtract(a, b):
    return int(a) - int(b)

@register.simple_tag
@stringfilter
def lower(a):
    return a.lower()


@register.simple_tag
def cap_one(str, lim, lim2):
    return str + lim + lim2

@register.inclusion_tag("inclus_tag_temp.html")
def inc_test():
    choises = ["hello", "bye"]

    return {"choices": choises}