from django.urls import path
from . import views

app_name = 'kurumlar'

urlpatterns = [
    path('', views.ilan_listesi, name='ilanlar'),  # İlan listesi ana sayfa
    path('ilan/<int:ilan_id>/', views.ilan_detay, name='ilan_detay'),  # İlan detay sayfası
    path('panel/', views.kurum_panel, name='kurum_panel'),
    path('profil/duzenle/', views.profil_duzenle, name='profil_duzenle'),
    path('ilan/ekle/', views.ilan_ekle, name='ilan_ekle'),
    path('ilan/<int:ilan_id>/duzenle/', views.ilan_duzenle, name='ilan_duzenle'),
    path('ilan/<int:ilan_id>/sil/', views.ilan_sil, name='ilan_sil'),
    path('ilan/<int:ilan_id>/basvurular/', views.basvuru_listesi, name='basvuru_listesi'),
    path('basvuru/<int:basvuru_id>/durum-guncelle/', views.basvuru_durum_guncelle, name='basvuru_durum_guncelle'),
]
