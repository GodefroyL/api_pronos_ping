from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
@api_view(['POST'])
def inscription(requete):
    token = 0
    return Response({"token": token})

@api_view(['POST'])
def connexion(requete):
    token = 0
    return Response({"token": token})

@api_view(['GET'])
def joueurs(requete):
    """Retour: [{id_joueur, nom, pays}]"""
    joueur = {"id_joueur": 0, "nom": "Miwa Harimoto", "pays": "japon"}
    return Response(joueur)

def matchs(requete):
    """Retour: [{id_match, championnat, tour, sexe, id_joueur_1, id_joueur_2, resultat}]"""
    pass

def utilisateurs(requete):
    """Retour: [{id_utilisateur, pseudo, pays, points_victoire, points_score}]"""
    pass

def ligues(requete):
    """Retour: [{id_ligue, nom, utilisateurs: [id_utilisateur, ...]}]"""
    pass

@api_view(['GET','POST'])
def pronos(requete):
    """
    Retour:
    - Si GET: liste des pronos de l'utilisateur connecté
    - Si POST: Crée ou met à jour les pronos de l'utilisateur connecté"""
    if requete.method == 'POST':
        return Response({"etat": "OK"})
    liste_pronos = []
    return liste_pronos
