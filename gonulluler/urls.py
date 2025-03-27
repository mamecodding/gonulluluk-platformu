from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.gonullu_panel, name='gonullu_panel'),
]
