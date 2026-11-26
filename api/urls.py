from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.connexion, name='connexion'),
    path('inscription', view=views.inscription, name='inscription'),
    path('joueurs', views.joueurs, name='joueurs'),
    path('matchs', views.matchs, name='matchs'),
    path('utilisateurs', views.utilisateurs, name='utilisateurs'),
    path('ligues', views.ligues, name='ligues'),
    path('pronos', views.pronos, name='pronos'),
]