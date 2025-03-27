from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import KullaniciKayitForm
from .models import KullaniciProfil

# Kayıt olma
def kayit_ol(request):
    if request.method == 'POST':
        form = KullaniciKayitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giris')
    else:
        form = KullaniciKayitForm()
    return render(request, 'kullanici/kayit.html', {'form': form})


# Giriş yapma
def giris_yap(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                profil = KullaniciProfil.objects.get(user=user)
                if profil.rol == 'kurum':
                    return redirect('kurum_panel')
                elif profil.rol == 'gonullu':
                    return redirect('gonullu_panel')
            except KullaniciProfil.DoesNotExist:
                return redirect('anasayfa')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
    return render(request, 'kullanici/giris.html')


# Çıkış yapma
def cikis_yap(request):
    logout(request)
    return redirect('giris')
