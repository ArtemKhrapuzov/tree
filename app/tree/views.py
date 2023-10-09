from django.views.generic import ListView

from tree.models import MenuItem


class TreeView(ListView):
    model = MenuItem
    template_name = 'tree/main_menu.html'


