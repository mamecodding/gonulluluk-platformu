from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('kayit/', views.kayit, name='kayit'),
    path('giris/', views.giris, name='giris'),
    path('cikis/', views.cikis, name='cikis'),
]
