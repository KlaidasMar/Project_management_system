from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita


# Register your models here.
class ProjektasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'klientas', 'pradzia', 'pabaiga')
    list_filter = ('pavadinimas', 'klientas')


class KlientasAdmin(admin.ModelAdmin):
    list_display = ('imone', 'vardas', 'pavarde')


class DarbuotojasAdmin(admin.ModelAdmin):
    list_display = ('vardas', 'pavarde', 'pareigos')


class SaskaitaAdmin(admin.ModelAdmin):
    list_display = ('suma', 'israsymo_data')


admin.site.register(Projektas, ProjektasAdmin)
admin.site.register(Klientas, KlientasAdmin)
admin.site.register(Darbuotojas, DarbuotojasAdmin)
admin.site.register(Darbas)
admin.site.register(Saskaita, SaskaitaAdmin)