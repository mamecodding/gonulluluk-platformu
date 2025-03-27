from django.db import models
from django.contrib.auth.models import User

class Gonullu(models.Model):
    ADAY_TURU_SECENEKLERI = [
        ('ogrenci', 'Öğrenci'),
        ('bireysel', 'Bireysel'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gonullu')
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    aday_turu = models.CharField(max_length=10, choices=ADAY_TURU_SECENEKLERI)
    dogum_tarihi = models.DateField(null=True, blank=True)
    sehir = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
