from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('login/', views.login, name='login'),
]