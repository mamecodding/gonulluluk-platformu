from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('kullanici/', include('kullanici.urls')),
    path('kurum/', include('kurumlar.urls')),  # sadece burada include kullanılır
]
