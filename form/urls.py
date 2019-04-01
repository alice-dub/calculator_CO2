from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('video', views.video, name='video'),
    path('augm_vie', views.augm_vie, name='augm_vie'),
    path('box', views.box, name='box')
]