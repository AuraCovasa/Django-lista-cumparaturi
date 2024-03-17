from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adauga', views.adauga, name='adauga'),
    path('cumpara/<int:produs_id>', views.cumpara, name='cumpara'),
    path('sterge/<int:produs_id>', views.sterge, name='sterge'),
]