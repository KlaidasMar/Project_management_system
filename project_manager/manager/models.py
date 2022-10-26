from django.db import models
from datetime import datetime, date
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Projektas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=100)
    pradzia = models.DateField("Pradžios data", blank=True)
    pabaiga = models.DateField("Pabaigos data", blank=True)
    klientas = models.ForeignKey('Klientas', on_delete=models.SET_NULL, null=True)
    vadovas = models.CharField('Atsakingasis/vadovas', max_length=100)
    darbuotojai = models.ForeignKey('Darbuotojas', on_delete=models.SET_NULL, null=True)
    darbai = models.ForeignKey('Darbas', on_delete=models.SET_NULL, null=True)
    saskaitos = models.ForeignKey("Saskaita", on_delete=models.SET_NULL, null=True)
    cover = models.ImageField('Viršelis', upload_to='covers', null=True)
    description = HTMLField(null=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_over(self):
        if self.pabaiga and date.today() > self.pabaiga:
            return True
        return False


    def __str__(self):
        return f"{self.pavadinimas} {self.pradzia} {self.pabaiga}"

    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"

class Klientas(models.Model):
    logo = models.ImageField('Logotipas', upload_to='logos', null=True)
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    imone = models.CharField("Įmonė", max_length=100)
    kontaktai = models.TextField("Kontaktai", max_length=150)


    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.imone}"

    class Meta:
        verbose_name = "Klientas"
        verbose_name_plural = "Klientai"

class Darbuotojas(models.Model):
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    pareigos = models.CharField("Pareigos", max_length=100)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

    class Meta:
        verbose_name = "Darbuotojas"
        verbose_name_plural = "Darbuotojai"

class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=100)
    pastabos = models.TextField("Pastabos", max_length=300)

    def __str__(self):
        return f"{self.pavadinimas}"

    class Meta:
        verbose_name = "Darbas"
        verbose_name_plural = "Darbai"

class Saskaita(models.Model):
    israsymo_data = models.DateField("Išrašymo data", blank=True)
    suma = models.FloatField("Suma")

    def __str__(self):
        return f"{self.israsymo_data} {self.suma}"

    class Meta:
        verbose_name = "Saskaita"
        verbose_name_plural = "Saskaitos"