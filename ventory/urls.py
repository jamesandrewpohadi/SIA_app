from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<statio>/', views.station, name='station'),
]
