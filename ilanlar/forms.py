from django import forms
from .models import Ilan, Basvuru  # ← eğer Basvuru modelin varsa

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        exclude = ['kurum']  # kurum alanını formdan çıkarıyoruz
        widgets = {
            'baslangic_tarihi': forms.DateInput(attrs={'type': 'date'}),
            'bitis_tarihi': forms.DateInput(attrs={'type': 'date'}),
            'aciklama': forms.Textarea(attrs={'rows': 4}),
        }

# BU SATIRI EKLEYİN EĞER BASVURU MODELİNİZ VARSA:
class BasvuruForm(forms.ModelForm):
    class Meta:
        model = Basvuru
        fields = ['ilan', 'gonullu', 'durum']
