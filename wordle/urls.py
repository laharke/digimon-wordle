from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_guess/', views.check_guess, name="check_guess"),
]
