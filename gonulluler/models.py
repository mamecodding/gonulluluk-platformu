from django.db import models

class Gonullu(models.Model):
    ADAY_TURU_CHOICES = [
        ('ogrenci', 'Öğrenci'),
        ('bireysel', 'Bireysel'),
    ]

    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    aday_turu = models.CharField(max_length=10, choices=ADAY_TURU_CHOICES)
    dogum_tarihi = models.DateField(blank=True, null=True)
    sehir = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
