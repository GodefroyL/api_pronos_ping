from django.db import models


class Joueur(models.Model):
    nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=10)

class Match(models.Model):
    championnat = models.CharField(max_length=20)
    tour = models.CharField(max_length=6)
    joueur_1 = models.ForeignKey('Joueur', on_delete=models.CASCADE, related_name='match_joueur_1')
    joueur_2 = models.ForeignKey('Joueur', on_delete=models.CASCADE, related_name='match_joueur_2')
    resultat = models.JSONField()

class Prono(models.Model):
    id_match = models.ForeignKey('Match', on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    score_joueur_1 = models.IntegerField()
    score_joueur_2 = models.IntegerField()
    reussi_victoire = models.BooleanField()
    reussi_score = models.BooleanField()

class Utilisateur(models.Model):
    pronos = models.ManyToManyField('Prono')
    points_victoire = models.IntegerField()
    points_score = models.IntegerField()
    membre_ligue = models.ManyToManyField('Ligue')
    pays = models.CharField(max_length=10)
    pseudo = models.CharField(max_length=50)
    mail = models.EmailField()
    # mdp à voir avec auth managment

class Ligue(models.Model):
    nom = models.CharField(max_length=100)
    utilisateurs = models.ManyToManyField('Utilisateur')
    # à voir pour mdp

