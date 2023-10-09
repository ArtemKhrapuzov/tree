from django.urls import path

from tree.views import *

urlpatterns = [
     path('', TreeView.as_view(), name='home'),
]