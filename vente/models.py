from django.db import models

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    unite = models.CharField(max_length=31)
    quantite = models.FloatField(editable=False, null=True)
    prix_vente = models.FloatField()
   

    def __str__(self):
        return f"{self.nom} igurishwa {self.prix_vente}"
    


class Stock(models.Model):
    id=models.AutoField(primary_key=True)
    Produit=models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_initiale=models.FloatField(editable=False,null=True)
    quantite_actuelle=models.FloatField(editable=False,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    delai_expiration=models.PositiveIntegerField()
    prix=models.FloatField()


class Commande(models.Model):
    id=models.AutoField(primary_key=True)
    prix_total=models.FloatField()
    created_at =models.DateTimeField
    client=models.CharField(max_length=32,null=True)

class Paiement(models.Model):
    id=models.AutoField(primary_key=True)
    montant=models.FloatField()
    received_by=models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    Commande=models.ForeignKey(Commande,on_delete=models.CASCADE)



