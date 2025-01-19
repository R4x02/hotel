from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views import View
from .models import *

def dodawanie(request):
    if request.method == 'POST':
        form = tworzeniepokoju(request.POST)
        if form.is_valid():
            form.save()
            return redirect('strona_glowna')
    else:
        form = tworzeniepokoju()
    return render(request, 'dodawanie_pokoi.html', {'form': form})

class WidokLogowania(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'logowanie.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('strona_glowna')
        return render(request, 'logowanie.html', {'form': form})

def rejestracja(request):
    if request.method == 'POST':
        formularz_uzytkownika = FormularzRejestracji(request.POST)
        if formularz_uzytkownika.is_valid():
            uzytkownik = formularz_uzytkownika.save()
            Profile.objects.create(
                user=uzytkownik
            )
            login(request, uzytkownik)
            return redirect('strona_glowna')
    else:
        formularz_uzytkownika = FormularzRejestracji()

    return render(request, 'rejestracja.html', {'formularz_uzytkownika': formularz_uzytkownika})

@login_required
def strona_glowna(request):
    if request.user.is_superuser:
        pokoje = Pokoje.objects.all()
        return render(request, 'baza.html', {'pokoje': pokoje})
    else:
        profile = Profile.objects.get(user=request.user)
        pokoj = profile.pokoj
        return render(request, 'nie_admin.html', {'pokoj': pokoj})

def rezerwacja(request):
    # pokoje = Pokoje.objects.all()
    return render(request, template_name='rezerwacja.html', context={'Pokoje': Pokoje.objects.all()})

def wylogowanie(request):
    logout(request)
    return redirect('logowanie')

@login_required
def join_room(request):
    if request.method == 'POST':
        form = dolacz(request.POST)
        if form.is_valid():
            room = form.cleaned_data['pokoj']
            profile = Profile.objects.get(user=request.user)
            if room.liczba_osob < room.pojemnosc_pokoju:
                profile.pokoj = room
                profile.save()
                room.liczba_osob += 1
                if room.liczba_osob == room.pojemnosc_pokoju:
                    room.czy_wolny = False  # Ustaw jako pełny
                room.save()
                return redirect('room_detail', room_id=room.id)
            else:
                return render(request, 'dolacz.html', {
                    'form': form,
                    'error': 'Pokój jest pełny, nie możesz dołączyć.'
                })
    else:
        form = dolacz()
    return render(request, 'dolacz.html', {'form': form})

def room_detail(request, room_id):
    room = get_object_or_404(Pokoje, id=room_id)
    return render(request, 'room_detail.html', {'room': room})

def leave_room(request, room_id):
    profile = Profile.objects.get(user=request.user)
    room = Pokoje.objects.get(id=room_id)
    if profile.pokoj == room:
        print(f"Przed opuszczeniem pokoju: liczba osób = {room.liczba_osob}, czy_wolny = {room.czy_wolny}")
        profile.pokoj = None
        profile.save()
        room.liczba_osob -= 1
        if room.liczba_osob < room.pojemnosc_pokoju:
            room.czy_wolny = True
        room.save()
        print(f"Po opuszczeniu pokoju: liczba osób = {room.liczba_osob}, czy_wolny = {room.czy_wolny}")
    return redirect('strona_glowna')