from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gonulluler.models import Gonullu
from kurumlar.models import Kurum
from .models import KullaniciProfil

class KayitForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefon = forms.CharField(max_length=20, required=False)
    sehir = forms.CharField(max_length=100, required=False)
    kurum_adi = forms.CharField(max_length=200, required=False)
    kurum_adres = forms.CharField(widget=forms.Textarea, required=False)
    kurum_website = forms.URLField(required=False)
    kurum_aciklama = forms.CharField(widget=forms.Textarea, required=False)
    # Gönüllü bilgileri
    ad = forms.CharField(max_length=30, required=False)
    soyad = forms.CharField(max_length=30, required=False)
    dogum_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    def __init__(self, *args, **kwargs):
        # request parametresini kwargs'dan çıkar
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        # URL'den rol parametresini al
        if self.request:
            rol = self.request.GET.get('rol', 'gonullu')
        else:
            rol = args[0].get('rol', 'gonullu') if args else 'gonullu'

        if rol == 'kurum':
            # Kurum için gereken alanları zorunlu yap
            self.fields['kurum_adi'].required = True
            self.fields['kurum_adres'].required = True
            self.fields['telefon'].required = True
            # Gönüllü alanlarını gizle
            del self.fields['ad']
            del self.fields['soyad']
            del self.fields['dogum_tarihi']
        else:
            # Gönüllü için gereken alanları zorunlu yap
            self.fields['ad'].required = True
            self.fields['soyad'].required = True
            self.fields['telefon'].required = True
            self.fields['dogum_tarihi'].required = True
            # Kurum alanlarını gizle
            del self.fields['kurum_adi']
            del self.fields['kurum_adres']
            del self.fields['kurum_website']
            del self.fields['kurum_aciklama']

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # URL'den rol parametresini al
            if self.request:
                rol = self.request.GET.get('rol', 'gonullu')
            else:
                rol = self.data.get('rol', 'gonullu')

            if rol == 'kurum':
                kurum = Kurum.objects.create(
                    ad=self.cleaned_data['kurum_adi'],
                    adres=self.cleaned_data['kurum_adres'],
                    telefon=self.cleaned_data['telefon'],
                    email=self.cleaned_data['email'],
                    website=self.cleaned_data['kurum_website'],
                    aciklama=self.cleaned_data['kurum_aciklama']
                )
                KullaniciProfil.objects.create(
                    user=user,
                    rol='kurum',
                    telefon=self.cleaned_data['telefon'],
                    sehir=self.cleaned_data['sehir'],
                    kurum=kurum
                )
            else:
                gonullu = Gonullu.objects.create(
                    user=user,
                    ad=self.cleaned_data['ad'],
                    soyad=self.cleaned_data['soyad'],
                    email=self.cleaned_data['email'],
                    telefon=self.cleaned_data['telefon'],
                    dogum_tarihi=self.cleaned_data['dogum_tarihi'],
                    sehir=self.cleaned_data['sehir']
                )
                KullaniciProfil.objects.create(
                    user=user,
                    rol='gonullu',
                    telefon=self.cleaned_data['telefon'],
                    sehir=self.cleaned_data['sehir']
                )
        return user

class GirisForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'})
    )
