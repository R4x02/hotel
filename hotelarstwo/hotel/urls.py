# hotel/hotelarstwo/hotel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dodawanie/', views.dodawanie, name='dodawanie'),
    path('logowanie/', views.WidokLogowania.as_view(), name='logowanie'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('strona_glowna/', views.strona_glowna, name='strona_glowna'),
    path('rezerwacja/', views.rezerwacja, name='rezerwacja'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    path('join_room/', views.join_room, name='join_room'),
    path('room_detail/<int:room_id>/', views.room_detail, name='room_detail'),
    path('leave_room/<int:room_id>/', views.leave_room, name='leave_room'),
]