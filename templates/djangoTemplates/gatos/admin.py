from django.contrib import admin
from .models import Gato
# Register your models here.

@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('name', 'patas',)

    