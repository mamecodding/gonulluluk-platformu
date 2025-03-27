from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.kurum_panel, name='kurum_panel'),
    path('ilan-ekle/', views.ilan_ekle, name='ilan_ekle'),
    path('ilan-duzenle/<int:ilan_id>/', views.ilan_duzenle, name='ilan_duzenle'),
    path('ilan-sil/<int:ilan_id>/', views.ilan_sil, name='ilan_sil'),
]
