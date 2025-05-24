# DDNS-Cloudflare-Updater

A lightweight, Dockerized Dynamic DNS (DDNS) updater for Cloudflare A-records.
It automatically checks your current external IP and updates the A-record on Cloudflare if it has changed—running every hour via cron.

## 🚀 Features

- ✅ Periodic IP checks via cron 
- ✅ Updates A-record if your IP has changed

- ---

## ⚙️ Environment Variables

These are injected via `docker-compose.yml` and used at runtime:

| Variable     | Description                       |
|--------------|-----------------------------------|
| `API_TOKEN`  | Cloudflare API token              |
| `NAME`       | DNS record to update (e.g. `home.example.com`) |
| `ZONE`       | Cloudflare zone ID                |

---

## 📄 Sample `docker-compose.yml`

```yaml
services:
  app:
    container_name: ddns-cloudflare
    build:
      dockerfile: dockerfile
    environment:
      - API_TOKEN=YOURAPITOKEN
      - NAME=NAMETOUPDATE
      - ZONE=CLOUDFLAREZONEID
    restart: unless-stopped
```
