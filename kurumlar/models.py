from django.db import models

class Kurum(models.Model):
    KURUM_TURU_CHOICES = [
        ('devlet', 'Devlet Kurumu'),
        ('ozel', 'Özel Kurum'),
    ]

    ad = models.CharField(max_length=200)
    kurum_turu = models.CharField(max_length=10, choices=KURUM_TURU_CHOICES)
    adres = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    web_sitesi = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.ad
