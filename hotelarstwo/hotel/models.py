from django.db import models
from django.contrib.auth.models import User

class Pokoje(models.Model):
    numer = models.CharField(max_length=50)
    pojemnosc_pokoju = models.PositiveIntegerField()
    czy_wolny = models.BooleanField()

    def __str__(self):
        return f"Pokój {self.numer}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Powiązanie z użytkownikiem
    telefon = models.CharField(max_length=15, null=True, blank=True)
    pokoj = models.ForeignKey(Pokoje, on_delete=models.CASCADE, default=None, null=True, blank=True)  # Domyślnie null

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"