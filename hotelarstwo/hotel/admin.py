from django.contrib import admin
from .models import Profile, Pokoje

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefon')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Pokoje)