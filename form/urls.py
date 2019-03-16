from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('video', views.video, name='video'),
]