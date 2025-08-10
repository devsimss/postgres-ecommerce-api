
# PostgreSQL E‑Commerce API (FastAPI + SQLAlchemy)

## Türkçe
Bu küçük proje, ürün ve sipariş yönetimini yalın bir şekilde göstermek için yazıldı. Kodun amacı “gerçek bir projede nasıl başlanır” fikrini vermek; ayrıntılarda kusursuzluk aramıyor. Veritabanı olarak PostgreSQL, servis tarafında FastAPI ve ORM olarak SQLAlchemy kullanıldı. Docker Compose ile veritabanı ayağa kalkıyor.

### Özellikler
- Ürün oluşturma, listeleme, güncelleme
- Kullanıcı oluşturma
- Sipariş oluşturma (stoktan düşme ve satır fiyatını sipariş anında sabitleme)
- Basit ödeme onayı (durum değişimi)
- Swagger ile hızlı deneme

### Hızlı Kurulum
1. Docker ile PostgreSQL’i başlatın:
   ```bash
   docker compose up -d
   ```
2. Sanal ortam ve paketler:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
3. API’yi çalıştırın:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Tarayıcı:
   - Swagger: http://localhost:8000/docs

### Notlar
- Ücret/para hassasiyeti için örnekte kuruş tutarı integer olarak tutuluyor (`*_cents`). Gerçek uygulamada `decimal` tercih edilebilir.
- Migration yok; tablolar başlangıçta `create_all` ile oluşuyor. Alembic eklemek mantıklı olur.
- Kimlik doğrulama eklenmedi. Amacımız temel veritabanı akışını görmek.

---

## English
This is a compact example to demonstrate a clean starting point for product and order management. It uses PostgreSQL, FastAPI, and SQLAlchemy. The database runs via Docker Compose.

### Features
- Create/list/update products
- Create users
- Create orders (reduce stock and snapshot unit price at order time)
- Simple payment confirmation (status flip)
- Handy Swagger docs

### Quick Start
1. Start PostgreSQL with Docker:
   ```bash
   docker compose up -d
   ```
2. Virtualenv and packages:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
3. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Browser:
   - Swagger: http://localhost:8000/docs

### Notes
- Amounts are stored as integer cents to dodge floating‑point quirks; `decimal` is also fine in real systems.
- No migrations; tables are created on startup for brevity. Add Alembic in real life.
- Authentication is not included. The goal is to keep the focus on database flows.
