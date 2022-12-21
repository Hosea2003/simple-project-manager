from django.db import models

# Create your models here.
class Projet(models.Model):

    #Numero du projet
    numero=models.CharField(max_length=15, unique=True)

    #Nom du projet
    nom = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return "%s-%s"%(self.numero, self.nom)
    
class Travail(models.Model):
    
    #projet qui a le travail
    projet =models.ForeignKey(Projet, related_name="travaux", on_delete=models.CASCADE)

    # Nom du travail
    nom = models.CharField(max_length=250)

class Bloc(models.Model):

    # Travail concerné
	travail = models.ForeignKey(Travail, related_name='blocs', on_delete=models.CASCADE)	
	
	# Nom du bloc
	nom = models.CharField(max_length=100)

class Tache(models.Model):
    """
        Différent de l'ERP
        Simple implémentation pour faire un test
    """

    #Travail concerné
    travail=models.ForeignKey(Travail, related_name="taches", on_delete=models.CASCADE)

    #Nom de la tache
    nom=models.CharField(max_length=15)


    
    
