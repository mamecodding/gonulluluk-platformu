from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def gonullu_panel(request):
    return render(request, 'gonulluler/panel.html')
