from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quartos', views.quartos, name='quartos'),
    path('reserva', views.reserva, name='reserva'),
    
]