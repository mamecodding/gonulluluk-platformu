from django.contrib import admin
from .models import Kurum, Ilan, Basvuru

@admin.register(Kurum)
class KurumAdmin(admin.ModelAdmin):
    list_display = ('ad', 'email', 'telefon', 'website')
    search_fields = ('ad', 'email', 'telefon')

@admin.register(Ilan)
class IlanAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kurum', 'konum', 'son_basvuru', 'durum')
    list_filter = ('durum', 'kurum', 'son_basvuru')
    search_fields = ('baslik', 'aciklama', 'konum')
    date_hierarchy = 'son_basvuru'

@admin.register(Basvuru)
class BasvuruAdmin(admin.ModelAdmin):
    list_display = ('ilan', 'gonullu', 'basvuru_tarihi', 'durum')
    list_filter = ('durum', 'basvuru_tarihi')
    search_fields = ('ilan__baslik', 'gonullu__ad', 'gonullu__soyad')
    date_hierarchy = 'basvuru_tarihi'
