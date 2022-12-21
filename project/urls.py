from django.urls import path
from .views import *

urlpatterns = [
    path("get-projets", get_projet),
    path('create-projet', create_projet)
]
