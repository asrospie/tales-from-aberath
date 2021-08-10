from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter
@stringfilter
def markdown(value):
    return md.markdown(value)

@register.inclusion_tag('blog/include/post_list.html')
def post_list(posts):
    return { 'posts': posts }