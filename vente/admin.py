from django.contrib import admin
from .models import  Produit,Stock,Commande,Paiement


admin.site.register( Produit)
admin.site.register(Stock) 
admin.site.register( Commande)
admin.site.register( Paiement)