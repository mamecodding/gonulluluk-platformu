from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GonulluKayitForm, GonulluProfilForm
from kurumlar.models import Basvuru
from .models import Gonullu

@login_required
def gonullu_panel(request):
    basvurular = Basvuru.objects.filter(gonullu__user=request.user).order_by('-basvuru_tarihi')
    return render(request, 'gonulluler/panel.html', {'basvurular': basvurular})

@login_required
def profil_goruntule(request):
    gonullu = get_object_or_404(Gonullu, user=request.user)
    return render(request, 'gonulluler/profil.html', {'gonullu': gonullu})

@login_required
def profil_duzenle(request):
    gonullu = get_object_or_404(Gonullu, user=request.user)
    if request.method == 'POST':
        form = GonulluProfilForm(request.POST, instance=gonullu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('gonulluler:gonullu_panel')
    else:
        form = GonulluProfilForm(instance=gonullu)
    return render(request, 'gonulluler/profil_duzenle.html', {'form': form})

@login_required
def basvuru_iptal(request, basvuru_id):
    basvuru = get_object_or_404(Basvuru, id=basvuru_id, gonullu__user=request.user)
    if request.method == 'POST':
        basvuru.delete()
        messages.success(request, 'Başvurunuz başarıyla iptal edildi.')
        return redirect('gonulluler:gonullu_panel')
    return render(request, 'gonulluler/basvuru_iptal.html', {'basvuru': basvuru})
