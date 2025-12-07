# Ankara Kültür & Sanat - Temel Flask Projesi

Bu repo, proje ödevi için hızlı bir Flask iskeleti sağlar: etkinlik listesi, kategori filtreleme, takvim API'si ve basit admin CRUD.

Hızlı başlatma

1. Python sanal ortam oluşturun ve aktif edin (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Bağımlılıkları yükleyin:

```powershell
pip install -r requirements.txt
```

3. Çevresel değişkenleri ayarlayın (örnek: `.env.example`):

```powershell
copy .env.example .env
# Düzenleyin .env içinde ADMIN_PASSWORD ve SECRET_KEY
```

4. Veritabanını başlatın ve örnek veri ekleyin:

```powershell
python init_db.py
```

5. Uygulamayı çalıştırın:

```powershell
python app.py
```

Admin paneli: `http://127.0.0.1:5000/admin/login` (şifre `.env` içinde `ADMIN_PASSWORD`).

Geliştirme notları:
- `templates/` içinde basit Jinja2 şablonları var.
- Takvim verisi: `/api/calendar` (ISO tarih ile filtreleme desteklenir).
- Bu temel iskeleti isteklerinize göre genişletebiliriz (e-posta bildirimleri, API auth, front-end takvim entegrasyonu vb.).

## Deploying to Render.com

This project is ready to deploy to Render as a Web Service. Changes added:

- `wsgi.py` — exposes the WSGI app for Gunicorn.
- `Procfile` — tells Render to run Gunicorn with `wsgi:app`.
- `requirements.txt` — now includes `gunicorn`.

Quick steps to deploy:

1. Push this repository to GitHub.
2. On Render (https://render.com) create a new Web Service and connect the GitHub repo.
3. Use the default build command (Render will run `pip install -r requirements.txt`).
4. Set environment variables on Render as needed (e.g. `SECRET_KEY`, `DATABASE_URL` if you want to use Postgres). By default the app uses a local SQLite DB at `instance/events.db`.

Notes:

- The SQLite database is stored on the instance filesystem — it will be created on deploy but is not shared between instances and will be lost on redeploys. For production persistence configure a managed database (Postgres) and set `DATABASE_URL`.
- To run migrations or seed data on Render, you can add a one-off job or run `init_db.py` locally and populate a managed DB.
