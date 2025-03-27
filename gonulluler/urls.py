from django.urls import path
from . import views

app_name = 'gonulluler'

urlpatterns = [
    path('panel/', views.gonullu_panel, name='gonullu_panel'),
    path('profil/duzenle/', views.profil_duzenle, name='profil_duzenle'),
    path('basvuru/<int:basvuru_id>/iptal/', views.basvuru_iptal, name='basvuru_iptal'),
]
