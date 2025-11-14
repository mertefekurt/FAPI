# FastAPI Auth & Role Management

Basit bir kimlik doğrulama ve rol yönetimi sistemi.

## Kurulum

```bash
pip install -r requirements.txt
```

## Çalıştırma

```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /auth/register` - Yeni kullanıcı kaydı
- `POST /auth/login` - Giriş yap
- `GET /auth/me` - Mevcut kullanıcı bilgileri
- `POST /roles` - Yeni rol oluştur (admin gerekli)
- `GET /roles` - Tüm rolleri listele
- `GET /roles/{role_id}` - Rol detayı
- `POST /roles/{role_id}/assign/{user_id}` - Kullanıcıya rol ata (admin gerekli)
- `DELETE /roles/{role_id}/remove/{user_id}` - Kullanıcıdan rol kaldır (admin gerekli)

