
from django.urls import path, include
from . views import *
urlpatterns = [
    path("suscrito/<email>", suscrito),
    path("suscribir/<email>", suscribir),
]
