from django.urls import path
from app.views import home, endereco

urlpatterns = [
    path(route='', view=home, name='index'),
    path(route='endereco/', view=endereco, name='endereco'),
]
