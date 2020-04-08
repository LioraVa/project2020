from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='center-home'),
    path('about/', views.about, name='center-about'),

]
