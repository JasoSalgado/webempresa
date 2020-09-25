"""Pages pages_extras."""

# Django modules
from django import template
from pages.models import Page

# Method tag
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages