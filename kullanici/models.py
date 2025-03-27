from django.contrib.auth.models import User
from django.db import models
from kurumlar.models import Kurum

class KullaniciProfil(models.Model):
    ROL_SECENEKLERI = [
        ('kurum', 'Kurum'),
        ('gonullu', 'Gönüllü'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=ROL_SECENEKLERI)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    sehir = models.CharField(max_length=100, blank=True, null=True)
    kurum = models.OneToOneField(Kurum, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.rol})"
