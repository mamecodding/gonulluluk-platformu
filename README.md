# Gönüllülük Platformu

Bu proje, gönüllüler ve kurumlar arasında köprü kuran bir web platformudur.

## Özellikler

- Gönüllü ve kurum kullanıcı kaydı
- İlan oluşturma ve yönetme
- İlanlara başvuru yapma
- Kullanıcı profilleri
- Responsive tasarım

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/gonulluluk_platformu.git
cd gonulluluk_platformu
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
venv\Scripts\activate     # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py migrate
```

5. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

6. Tarayıcınızda http://127.0.0.1:8000/ adresine gidin.

## Teknolojiler

- Python 3.12
- Django 5.1
- Bootstrap 5
- SQLite

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 