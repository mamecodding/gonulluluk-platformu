from django.db import models
from django.contrib.auth.models import User

class Kurum(models.Model):
    ad = models.CharField(max_length=200)
    adres = models.TextField()
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    aciklama = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ad

class Ilan(models.Model):
    DURUM_SECENEKLERI = [
        ('aktif', 'Aktif'),
        ('pasif', 'Pasif'),
        ('kapali', 'Kapalı'),
    ]

    kurum = models.ForeignKey(Kurum, on_delete=models.CASCADE, related_name='ilanlar')
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    konum = models.CharField(max_length=200)
    son_basvuru = models.DateField()
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLERI, default='aktif')
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.baslik} - {self.kurum.ad}"

class Basvuru(models.Model):
    DURUM_SECENEKLERI = [
        ('beklemede', 'Beklemede'),
        ('kabul', 'Kabul Edildi'),
        ('red', 'Reddedildi'),
    ]

    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='basvurular')
    gonullu = models.ForeignKey('gonulluler.Gonullu', on_delete=models.CASCADE, related_name='basvurular')
    basvuru_tarihi = models.DateTimeField(auto_now_add=True)
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLERI, default='beklemede')
    notlar = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.gonullu.ad} {self.gonullu.soyad} - {self.ilan.baslik}"
