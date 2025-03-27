from django.db import models
from kurumlar.models import Kurum
from gonulluler.models import Gonullu

class Ilan(models.Model):
    kurum = models.ForeignKey(Kurum, on_delete=models.CASCADE, related_name='ilanlar')
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    konum = models.CharField(max_length=200)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    kontenjan = models.PositiveIntegerField()
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.baslik} - {self.kurum.ad}"

class Basvuru(models.Model):
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='basvurular')
    gonullu = models.ForeignKey(Gonullu, on_delete=models.CASCADE, related_name='basvurular')
    basvuru_tarihi = models.DateTimeField(auto_now_add=True)
    durum = models.CharField(max_length=20, choices=[
        ('beklemede', 'Beklemede'),
        ('kabul', 'Kabul Edildi'),
        ('red', 'Reddedildi')
    ], default='beklemede')

    def __str__(self):
        return f"{self.gonullu} → {self.ilan}"
