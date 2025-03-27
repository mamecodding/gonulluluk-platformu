from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('ilanlar/', views.ilanlar, name='ilanlar'),
    path('ilan/<int:ilan_id>/', views.ilan_detay, name='ilan_detay'),
    path('giris/', views.giris, name='giris'),
    path('kayit/', views.kayit, name='kayit'),
    path('cikis/', views.cikis, name='cikis'),
]
