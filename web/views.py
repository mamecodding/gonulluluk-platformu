from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ilanlar.models import Ilan
from ilanlar.forms import BasvuruForm
from kullanici.forms import KullaniciKayitForm

def anasayfa(request):
    son_ilanlar = Ilan.objects.filter(aktif=True).order_by('-id')[:6]
    return render(request, 'web/anasayfa.html', {'son_ilanlar': son_ilanlar})

def ilanlar(request):
    ilanlar = Ilan.objects.filter(aktif=True)
    return render(request, 'web/ilanlar.html', {'ilanlar': ilanlar})

def ilan_detay(request, ilan_id):
    ilan = get_object_or_404(Ilan, id=ilan_id)
    if request.method == 'POST':
        form = BasvuruForm(request.POST)
        if form.is_valid():
            basvuru = form.save(commit=False)
            basvuru.ilan = ilan
            basvuru.gonullu = request.user.gonullu
            basvuru.save()
            messages.success(request, 'Başvurunuz başarıyla alındı.')
            return redirect('ilan_detay', ilan_id=ilan.id)
    else:
        form = BasvuruForm()
    
    return render(request, 'web/ilan_detay.html', {
        'ilan': ilan,
        'form': form
    })

def giris(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yaptınız.')
            return redirect('anasayfa')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
    return render(request, 'web/giris.html')

def kayit(request):
    if request.method == 'POST':
        form = KullaniciKayitForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Başarıyla kayıt oldunuz.')
            return redirect('anasayfa')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = KullaniciKayitForm()
    return render(request, 'web/kayit.html', {'form': form})

@login_required
def cikis(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız.')
    return redirect('anasayfa')
