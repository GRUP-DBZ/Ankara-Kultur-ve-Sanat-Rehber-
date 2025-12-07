# Rapor: Ankara Kültür & Sanat - Proje Teslim Raporu

Bu rapor, projede yapılan işleri, kimin hangi katkıyı yaptığını kanıtlayacak Git verilerini ve sınav/ödev teslimi sırasında jürinin (hocanın) projeyi nasıl çalıştırıp doğrulayacağını adım adım açıklar.

Repository: https://github.com/GRUP-DBZ/Ankara-Kultur-ve-Sanat-Rehber-

## 1) Projenin özeti
- Kısa açıklama: Flask tabanlı küçük bir etkinlik rehberi uygulaması. Etkinlik listesi, admin CRUD, bilet isteği formu, tema toggle (light/dark) bulunmaktadır.
- Deployment hazır dosyalar: `wsgi.py`, `Procfile`, `requirements.txt`, `runtime.txt`, `.env.example`.

## 2) Yapılan adımlar (kısaca)
- Kod incelendi ve çalıştırılabilir hale getirildi.
- Satır sonu (EOL) uyumsuzlukları için `.gitattributes` eklendi ve renormalize edildi.
- Deploy için `gunicorn` ve `psycopg2-binary` `requirements.txt` içine eklendi.
- Render uyumluluğu için `runtime.txt` ve `.env.example` eklendi.
- Managed DB kullanımı için `seed_db.py` eklendi (idempotent, Postgres ile çalışır).
- `REPORT.md` ve `CONTRIBUTORS.md` (bu dosya) eklendi; ayrıca Git geçmişinden kanıtlar oluşturuldu.

## 3) Katkı kanıtı (Git geçmişi)
Aşağıda repository içindeki commit geçmişinden çıkarılmış kısa bir katkı özeti yer almaktadır (otomatik `git shortlog -sne` çıktısı). Bu dosya ayrıca `GIT_CONTRIBUTORS.txt` olarak repoda mevcuttur.

```
 21  Damla <s240307005@ankarabilim.edu.tr>
  5  Beyzaeo <s240307031@ankarabilim.edu.tr>
  2  Mustafa Tarık KILIÇ <kilicmustafatarik@gmail.com>
  1  Zeynep <s240307038@ankarabilim.edu.tr>
```

Bu çıktı, her kullanıcının repo içindeki commit sayısını ve commit yazar bilgisini gösterir — hocanız bu veriyi GitHub üzerinde de `Insights → Contributors` bölümünden veya `git shortlog -sne` komutunu çalıştırarak doğrulayabilir.

Ek kanıtlar:
- `GIT_RECENT_LOG.txt`: son 50 commit'in kısa bir listesi (commit hash, yazar, tarih, başlık).

## 4) Hocanın (veya sizin) projeyi yerel ortamda açıp doğrulaması (adım adım)

1) Repo'yu klonlayın:

```bash
git clone https://github.com/GRUP-DBZ/Ankara-Kultur-ve-Sanat-Rehber-.git
cd Ankara-Kultur-ve-Sanat-Rehber-
```

2) Python sanal ortam oluşturun ve aktif edin (PowerShell örneği):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Bağımlılıkları yükleyin:

```powershell
python -m pip install -U pip
pip install -r requirements.txt
```

4) (Opsiyonel: veritabanı seed) Eğer sadece demo görmek isterseniz SQLite ile çalıştırabilirsiniz (variables gerekmez). Eğer proje Postgres ile kullanmak istiyorsanız yönetici Postgres bilgilerini alın ve seed uygulayın.

PowerShell (örnek):
```powershell
$env:DATABASE_URL = "postgres://kullanici:parola@host:5432/dbadi"
python seed_db.py
```

5) Uygulamayı çalıştırın (geliştirme):

```powershell
python app.py
# veya production-örnek test için (gunicorn kuruluysa):
# gunicorn wsgi:app --bind 0.0.0.0:5000
```

6) Tarayıcıda açın: `http://127.0.0.1:5000/` — admin paneli: `/admin/login`.

## 5) Hocanın doğrulaması için alternatif hızlı kontroller
- GitHub üzerinde repo sayfasına gidip `Insights → Contributors` bölümünü açabilir.
- Ya da terminalde (klonlandıktan sonra):

```bash
git shortlog -sne
git log --pretty=format:"%h %an %ad %s" --date=short -n 50
```

Bu komutlar aynı verileri üretir; hocanız herhangi bir commit'e tıklayarak hangi dosyaları değiştirdiğini, commit mesajını ve tarihini görebilir.

## 6) Rapor teslimi için ekler (repo içinde)
- `REPORT.md` (bu dosya)
- `CONTRIBUTORS.md` (grup üyeleri kendi isimlerini/katkı özetlerini eklesinler)
- `GIT_CONTRIBUTORS.txt` (otomatik özet)
- `GIT_RECENT_LOG.txt` (son 50 commit listesi)

## 7) Neler öğrendik / kısa değerlendirme (grup tarafından doldurulacak)
- Her grup üyesi burada 1-3 cümle ile hangi görevleri üstlendiğini yazacaktır (coding, styling, deploy, dokümantasyon vs.).

---
Raporu hazırlayan: Proje deposu tarafından otomatik destek (ek dosyalar commit edildi). Detay/ekleme isterseniz ben `CONTRIBUTORS.md` içine grup üyelerinin kısa açıklamalarını ekleyebilirim.
