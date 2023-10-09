from django import template
from tree.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(parent=None, name=menu_name).prefetch_related('children__children__children')
    current_url = request.path_info
    return _render_menu(menu_items, current_url)


def _render_menu(menu_items, current_url):
    result = '<ul>'
    for item in menu_items:
        active = ''
        if item.get_url() == current_url or (item.get_url() == '/' and current_url == ''):
            active = 'active'
        result += f'<li class="{active}"><a href="{item.get_url()}">{item.name}</a>'
        if item.children.count():
            result += _render_menu(item.children.all(), current_url)
        result += '</li>'
    result += '</ul>'
    return result
