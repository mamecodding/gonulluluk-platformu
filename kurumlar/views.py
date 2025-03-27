from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ilanlar.models import Ilan
from ilanlar.forms import IlanForm
from kullanici.models import KullaniciProfil

@login_required
def kurum_panel(request):
    kullanici = request.user
    profil = KullaniciProfil.objects.get(user=kullanici)
    if not profil.kurum:
        return render(request, 'kurumlar/panel.html', {'ilanlar': []})
    ilanlar = Ilan.objects.filter(kurum=profil.kurum)
    return render(request, 'kurumlar/panel.html', {'ilanlar': ilanlar})

@login_required
def ilan_ekle(request):
    kullanici = request.user
    profil = KullaniciProfil.objects.get(user=kullanici)
    
    if not profil.kurum:
        messages.error(request, 'Önce kurum profilinizi oluşturmalısınız.')
        return redirect('kurum_panel')

    if request.method == 'POST':
        form = IlanForm(request.POST)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.kurum = profil.kurum
            ilan.save()
            messages.success(request, 'İlan başarıyla eklendi.')
            return redirect('kurum_panel')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = IlanForm()

    return render(request, 'kurumlar/ilan_ekle.html', {'form': form})

@login_required
def ilan_duzenle(request, ilan_id):
    kullanici = request.user
    profil = KullaniciProfil.objects.get(user=kullanici)
    ilan = get_object_or_404(Ilan, id=ilan_id, kurum=profil.kurum)

    if request.method == 'POST':
        form = IlanForm(request.POST, instance=ilan)
        if form.is_valid():
            form.save()
            messages.success(request, 'İlan başarıyla güncellendi.')
            return redirect('kurum_panel')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = IlanForm(instance=ilan)

    return render(request, 'kurumlar/ilan_duzenle.html', {'form': form, 'ilan': ilan})

@login_required
def ilan_sil(request, ilan_id):
    kullanici = request.user
    profil = KullaniciProfil.objects.get(user=kullanici)
    ilan = get_object_or_404(Ilan, id=ilan_id, kurum=profil.kurum)

    if request.method == 'POST':
        ilan.delete()
        messages.success(request, 'İlan başarıyla silindi.')
        return redirect('kurum_panel')

    return render(request, 'kurumlar/ilan_sil.html', {'ilan': ilan})
