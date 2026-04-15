from django.urls import path
from . import views

urlpatterns = [
    path('api/test/', views.test_post, name='test_post'),
    path('api/calculate/', views.calculate, name='calculate'),
]