from django.urls import path
from . import views

urlpatterns = [
    path('logowanie/', views.WidokLogowania.as_view(), name='logowanie'),
    path('strona_glowna/', views.strona_glowna, name='strona_glowna'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    path('dodawanie/', views.dodawanie, name="dodawanie")
]