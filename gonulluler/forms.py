from django import forms
from django.contrib.auth.models import User
from .models import Gonullu

class GonulluProfilForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-Posta Adresi")

    class Meta:
        model = Gonullu
        fields = ['ad', 'soyad', 'telefon', 'dogum_tarihi']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'user') and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profil = super().save(commit=False)
        if commit:
            profil.save()
            if 'email' in self.cleaned_data:
                profil.user.email = self.cleaned_data['email']
                profil.user.save()
        return profil

# 💡 BURAYA EKLİYORSUN
class GonulluKayitForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-Posta Adresi")
    password = forms.CharField(widget=forms.PasswordInput, label="Parola")

    class Meta:
        model = Gonullu
        fields = ['ad', 'soyad', 'telefon', 'dogum_tarihi']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        gonullu = super().save(commit=False)
        gonullu.user = user
        if commit:
            user.save()
            gonullu.save()
        return gonullu
