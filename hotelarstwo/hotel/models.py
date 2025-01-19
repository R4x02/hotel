from django.db import models
from django.contrib.auth.models import User

class Pokoje(models.Model):
    numer = models.CharField(max_length=50)
    pojemnosc_pokoju = models.PositiveIntegerField()
    liczba_osob = models.PositiveIntegerField(default=0)  # Nowe pole
    czy_wolny = models.BooleanField(default=True)

    def __str__(self):
        return f"Pokój {self.numer}"

    def dodaj_uzytkownika(self):
        """Dodaje użytkownika do pokoju, jeśli jest miejsce."""
        if self.liczba_osob < self.pojemnosc_pokoju:
            self.liczba_osob += 1
            if self.liczba_osob == self.pojemnosc_pokoju:
                self.czy_wolny = False  # Pokój pełny
            self.save()
        else:
            raise ValueError("Pokój jest już pełny!")

    def usun_uzytkownika(self):
        """Usuwa użytkownika z pokoju, jeśli ktoś w nim jest."""
        if self.liczba_osob > 0:
            self.liczba_osob -= 1
            if self.liczba_osob < self.pojemnosc_pokoju:
                self.czy_wolny = True  # Pokój znowu ma wolne miejsce
            self.save()
        else:
            raise ValueError("Pokój jest już pusty!")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Powiązanie z użytkownikiem
    telefon = models.CharField(max_length=15, null=True, blank=True)
    pokoj = models.ForeignKey(Pokoje, on_delete=models.CASCADE, default=None, null=True, blank=True)  # Domyślnie null

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"