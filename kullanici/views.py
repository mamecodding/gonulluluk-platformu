from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import KayitForm, GirisForm
from .models import KullaniciProfil
from kurumlar.models import Kurum, Ilan, Basvuru
from gonulluler.models import Gonullu

def anasayfa(request):
    context = {
        'son_ilanlar': Ilan.objects.filter(durum='aktif').order_by('-olusturma_tarihi')[:5],
        'toplam_ilan': Ilan.objects.filter(durum='aktif').count(),
        'toplam_gonullu': Gonullu.objects.count(),
        'toplam_kurum': Kurum.objects.count(),
        'toplam_basvuru': Basvuru.objects.count(),
    }
    return render(request, 'kullanici/anasayfa.html', context)

# Kayıt olma
def kayit(request):
    rol = request.GET.get('rol', 'gonullu')
    if request.method == 'POST':
        form = KayitForm(request.POST, request=request)
        if form.is_valid():
            # Check if user with this email already exists
            email = form.cleaned_data.get('email')
            if KullaniciProfil.objects.filter(user__email=email).exists():
                messages.error(request, 'Bu e-posta adresi ile zaten bir hesabınız bulunmaktadır. Lütfen farklı bir e-posta adresi kullanın.')
                return render(request, 'kullanici/kayit.html', {'form': form, 'rol': rol})
            
            try:
                # Create user and related objects
                user = form.save(commit=True)
                
                login(request, user)
                messages.success(request, 'Kayıt işlemi başarılı!')
                if rol == 'kurum':
                    return redirect('kurumlar:kurum_panel')
                else:
                    return redirect('gonulluler:gonullu_panel')
            except Exception as e:
                messages.error(request, f'Kayıt işlemi sırasında bir hata oluştu: {str(e)}')
                return render(request, 'kullanici/kayit.html', {'form': form, 'rol': rol})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = KayitForm(request=request)
    return render(request, 'kullanici/kayit.html', {'form': form, 'rol': rol})

# Giriş yapma
def giris(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rol = request.POST.get('rol', 'gonullu')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                kullanici_profil = KullaniciProfil.objects.get(user=user)
                if kullanici_profil.rol == rol:
                    login(request, user)
                    messages.success(request, 'Giriş başarılı!')
                    if rol == 'kurum':
                        return redirect('kurumlar:kurum_panel')
                    else:
                        return redirect('gonulluler:gonullu_panel')
                else:
                    messages.error(request, 'Bu hesap türü için giriş yapamazsınız!')
            except KullaniciProfil.DoesNotExist:
                messages.error(request, 'Kullanıcı profili bulunamadı!')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    return render(request, 'kullanici/giris.html')

# Çıkış yapma
@login_required
def cikis(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız.')
    return redirect('anasayfa')
