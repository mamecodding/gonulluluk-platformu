from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kurum, Ilan, Basvuru
from .forms import KurumProfilForm, IlanForm, BasvuruDurumForm
from django.utils import timezone

def ilan_listesi(request):
    aktif_ilanlar = Ilan.objects.filter(
        son_basvuru__gte=timezone.now()
    ).order_by('-olusturma_tarihi')
    return render(request, 'kurumlar/ilan_listesi.html', {'ilanlar': aktif_ilanlar})

def ilan_detay(request, ilan_id):
    ilan = get_object_or_404(Ilan, id=ilan_id)
    context = {
        'ilan': ilan,
        'today': timezone.now().date()
    }
    return render(request, 'kurumlar/ilan_detay.html', context)

@login_required
def ilan_ekle(request):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    if request.method == 'POST':
        form = IlanForm(request.POST)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.kurum = kurum
            ilan.save()
            messages.success(request, 'İlan başarıyla oluşturuldu.')
            return redirect('kurumlar:kurum_panel')
    else:
        form = IlanForm()
    return render(request, 'kurumlar/ilan_ekle.html', {'form': form})


@login_required
def kurum_panel(request):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    ilanlar = Ilan.objects.filter(kurum=kurum).order_by('-olusturma_tarihi')
    return render(request, 'kurumlar/panel.html', {'kurum': kurum, 'ilanlar': ilanlar})

@login_required
def profil_duzenle(request):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    if request.method == 'POST':
        form = KurumProfilForm(request.POST, instance=kurum)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla güncellendi.')
            return redirect('kurumlar:kurum_panel')
    else:
        form = KurumProfilForm(instance=kurum)
    return render(request, 'kurumlar/profil_duzenle.html', {'form': form})

@login_required
def ilan_ekle(request):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    if request.method == 'POST':
        form = IlanForm(request.POST)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.kurum = kurum
            ilan.save()
            messages.success(request, 'İlan başarıyla oluşturuldu.')
            return redirect('kurumlar:kurum_panel')
    else:
        form = IlanForm()
    return render(request, 'kurumlar/ilan_ekle.html', {'form': form})

@login_required
def ilan_duzenle(request, ilan_id):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    ilan = get_object_or_404(Ilan, id=ilan_id, kurum=kurum)
    if request.method == 'POST':
        form = IlanForm(request.POST, instance=ilan)
        if form.is_valid():
            form.save()
            messages.success(request, 'İlan başarıyla güncellendi.')
            return redirect('kurumlar:kurum_panel')
    else:
        form = IlanForm(instance=ilan)
    return render(request, 'kurumlar/ilan_duzenle.html', {'form': form})

@login_required
def ilan_sil(request, ilan_id):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    ilan = get_object_or_404(Ilan, id=ilan_id, kurum=kurum)
    if request.method == 'POST':
        ilan.delete()
        messages.success(request, 'İlan başarıyla silindi.')
        return redirect('kurumlar:kurum_panel')
    return render(request, 'kurumlar/ilan_sil.html', {'ilan': ilan})

@login_required
def basvuru_listesi(request, ilan_id):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    ilan = get_object_or_404(Ilan, id=ilan_id, kurum=kurum)
    basvurular = Basvuru.objects.filter(ilan=ilan).order_by('-basvuru_tarihi')
    return render(request, 'kurumlar/basvuru_listesi.html', {'ilan': ilan, 'basvurular': basvurular})

@login_required
def basvuru_durum_guncelle(request, basvuru_id):
    kurum = get_object_or_404(Kurum, kullaniciprofil__user=request.user)
    basvuru = get_object_or_404(Basvuru, id=basvuru_id, ilan__kurum=kurum)
    if request.method == 'POST':
        form = BasvuruDurumForm(request.POST, instance=basvuru)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başvuru durumu başarıyla güncellendi.')
            return redirect('kurumlar:basvuru_listesi', ilan_id=basvuru.ilan.id)
    else:
        form = BasvuruDurumForm(instance=basvuru)
    return render(request, 'kurumlar/basvuru_durum_guncelle.html', {'form': form, 'basvuru': basvuru})
