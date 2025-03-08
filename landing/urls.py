from django.urls import path
from . import views
from .views import adocao_view

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('adocao/', adocao_view, name='adocao'),
    path('contato/', views.contato, name='contato'),
]