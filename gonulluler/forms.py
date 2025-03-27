from django import forms
from django.contrib.auth.models import User
from .models import GonulluProfil

class GonulluProfilForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-Posta Adresi")

    class Meta:
        model = GonulluProfil
        fields = ['ad', 'soyad', 'telefon', 'dogum_tarihi', 'adres']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Eğer kullanıcı nesnesi varsa e-posta bilgisini forma yerleştir
        if hasattr(self.instance, 'user') and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profil = super().save(commit=False)
        if commit:
            profil.save()
            # Kullanıcının e-postasını da güncelle
            if 'email' in self.cleaned_data:
                profil.user.email = self.cleaned_data['email']
                profil.user.save()
        return profil
