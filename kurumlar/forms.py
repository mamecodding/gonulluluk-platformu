from django import forms
from .models import Kurum, Ilan, Basvuru

class KurumProfilForm(forms.ModelForm):
    class Meta:
        model = Kurum
        fields = ['ad', 'adres', 'telefon', 'email', 'website', 'aciklama']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ['baslik', 'aciklama', 'konum', 'son_basvuru', 'durum']
        widgets = {
            'baslik': forms.TextInput(attrs={'class': 'form-control'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'konum': forms.TextInput(attrs={'class': 'form-control'}),
            'son_basvuru': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'durum': forms.Select(attrs={'class': 'form-control'}),
        }

class BasvuruDurumForm(forms.ModelForm):
    class Meta:
        model = Basvuru
        fields = ['durum']
        widgets = {
            'durum': forms.Select(attrs={'class': 'form-control'}),
        } 