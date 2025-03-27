from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gonullu

class GonulluKayitForm(UserCreationForm):
    email = forms.EmailField(required=True)
    ad = forms.CharField(max_length=30)
    soyad = forms.CharField(max_length=30)
    telefon = forms.CharField(max_length=20)
    aday_turu = forms.ChoiceField(choices=Gonullu.ADAY_TURU_SECENEKLERI)
    dogum_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sehir = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'ad', 'soyad', 'telefon', 'aday_turu', 'dogum_tarihi', 'sehir')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Gonullu.objects.create(
                user=user,
                ad=self.cleaned_data['ad'],
                soyad=self.cleaned_data['soyad'],
                email=self.cleaned_data['email'],
                telefon=self.cleaned_data['telefon'],
                aday_turu=self.cleaned_data['aday_turu'],
                dogum_tarihi=self.cleaned_data['dogum_tarihi'],
                sehir=self.cleaned_data['sehir']
            )
        return user

class GonulluProfilForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-Posta", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Gonullu
        fields = ('ad', 'soyad', 'telefon', 'aday_turu', 'dogum_tarihi', 'sehir')
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'aday_turu': forms.Select(attrs={'class': 'form-control'}),
            'dogum_tarihi': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sehir': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            if 'email' in self.cleaned_data:
                instance.user.email = self.cleaned_data['email']
                instance.user.save()
        return instance 