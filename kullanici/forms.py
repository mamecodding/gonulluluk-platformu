from django import forms
from django.contrib.auth.models import User
from .models import KullaniciProfil

class KullaniciKayitForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rol = forms.ChoiceField(choices=KullaniciProfil.ROL_SECENEKLERI)
    telefon = forms.CharField(required=False)
    sehir = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profil = KullaniciProfil.objects.create(
                user=user,
                rol=self.cleaned_data['rol'],
                telefon=self.cleaned_data['telefon'],
                sehir=self.cleaned_data['sehir']
            )
        return user
