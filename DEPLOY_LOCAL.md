# UzASBO 2.0 AI Assistant — Ubuntu Server Deploy (CPU, Docker siz)

## Arxitektura

```
Foydalanuvchi → Nginx (80/443) → AI Service (8100) → Ollama (11434) [LOCAL]
                                                   → ChromaDB (8000) [LOCAL]
                                                   → Redis (6379) [LOCAL]
```

Hammasi local ishlaydi — Docker kerak emas. Eng tez variant.

---

## 1-Bosqich: Serverni Tayyorlash

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git wget htop python3.12 python3.12-venv python3-pip
```

---

## 2-Bosqich: Ollama Local O'rnatish

```bash
# Ollama o'rnatish (bitta buyruq)
curl -fsSL https://ollama.com/install.sh | sh

# Ollama xizmatini ishga tushirish
sudo systemctl enable ollama
sudo systemctl start ollama

# Tekshirish
ollama --version
systemctl status ollama

# Modellarni yuklash (CPU uchun kichik model — tezroq ishlaydi)
ollama pull qwen2.5:3b
ollama pull nomic-embed-text

# Tekshirish — modellar ro'yxati
ollama list
```

### Ollama sozlamalari (CPU tezlik uchun):
```bash
sudo mkdir -p /etc/systemd/system/ollama.service.d
sudo tee /etc/systemd/system/ollama.service.d/override.conf << 'EOF'
[Service]
Environment="OLLAMA_NUM_PARALLEL=2"
Environment="OLLAMA_MAX_LOADED_MODELS=2"
Environment="OLLAMA_HOST=0.0.0.0:11434"
EOF

sudo systemctl daemon-reload
sudo systemctl restart ollama
```

---

## 3-Bosqich: ChromaDB O'rnatish (Local)

```bash
# ChromaDB ni pip orqali o'rnatish
sudo pip install chromadb

# Ma'lumotlar papkasi
sudo mkdir -p /var/lib/chromadb
sudo chown $USER:$USER /var/lib/chromadb
```

### ChromaDB systemd service yaratish:

```bash
sudo tee /etc/systemd/system/chromadb.service << 'EOF'
[Unit]
Description=ChromaDB Vector Database
After=network.target

[Service]
Type=exec
User=ubuntu
Group=ubuntu
Environment="ANONYMIZED_TELEMETRY=FALSE"
Environment="IS_PERSISTENT=TRUE"
Environment="PERSIST_DIRECTORY=/var/lib/chromadb"
ExecStart=/usr/local/bin/chroma run --host 127.0.0.1 --port 8000 --path /var/lib/chromadb
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable chromadb
sudo systemctl start chromadb

# Tekshirish
curl http://127.0.0.1:8000/api/v2/heartbeat
```

---

## 4-Bosqich: Redis O'rnatish (Local)

```bash
# Redis o'rnatish
sudo apt install -y redis-server

# Sozlash
sudo sed -i 's/^# maxmemory <bytes>/maxmemory 512mb/' /etc/redis/redis.conf
sudo sed -i 's/^# maxmemory-policy noeviction/maxmemory-policy allkeys-lru/' /etc/redis/redis.conf
sudo sed -i 's/^appendonly no/appendonly yes/' /etc/redis/redis.conf

# Faqat localhost dan ulanish (xavfsizlik)
sudo sed -i 's/^bind .*/bind 127.0.0.1 ::1/' /etc/redis/redis.conf

# Ishga tushirish
sudo systemctl enable redis-server
sudo systemctl restart redis-server

# Tekshirish
redis-cli ping
# Kutilgan javob: PONG
```

---

## 5-Bosqich: AI Service O'rnatish

```bash
# Loyiha papkasi
sudo mkdir -p /opt/uzasbo2-ai
sudo chown $USER:$USER /opt/uzasbo2-ai
cd /opt/uzasbo2-ai

# Kodni ko'chirish (git yoki scp)
git clone https://your-repo-url/uzasbo2_ai_assistant.git .
# yoki: scp -r user@local-pc:/path/to/uzasbo2_ai_assistant/* .

# Virtual environment yaratish
python3.12 -m venv venv
source venv/bin/activate

# Kutubxonalarni o'rnatish
pip install --upgrade pip
pip install -r requirements.txt
```

### .env fayl yaratish:

```bash
cat > /opt/uzasbo2-ai/.env << 'EOF'
# --- Ollama (LOCAL) ---
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=qwen2.5:3b
OLLAMA_EMBED_MODEL=nomic-embed-text

# --- ChromaDB (LOCAL) ---
CHROMA_HOST=127.0.0.1
CHROMA_PORT=8000
CHROMA_COLLECTION=uzasbo2_knowledge

# --- Redis (LOCAL) ---
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_DB=0

# --- FastAPI ---
APP_PORT=8100
APP_DEBUG=False
CORS_ORIGINS=http://localhost:3000,http://your-domain.uz

# --- RAG ---
RAG_TOP_K=5
RAG_TEMPERATURE=0.2
RAG_CHUNK_SIZE=800
RAG_CHUNK_OVERLAP=200
EOF
```

---

## 6-Bosqich: Knowledge Base Yuklash

```bash
cd /opt/uzasbo2-ai
source venv/bin/activate

# Backend parse qilish (agar kerak bo'lsa)
python scripts/parse_backend.py --backend-path /path/to/uzasbo2_backend

# ChromaDB ga yuklash
python scripts/load_knowledge_base.py --force
```

---

## 7-Bosqich: Systemd Service Yaratish (avtomatik ishga tushish)

```bash
sudo tee /etc/systemd/system/uzasbo2-ai.service << 'EOF'
[Unit]
Description=UzASBO 2.0 AI Assistant
After=network.target ollama.service chromadb.service redis-server.service
Wants=ollama.service chromadb.service redis-server.service

[Service]
Type=exec
User=ubuntu
Group=ubuntu
WorkingDirectory=/opt/uzasbo2-ai
Environment="PATH=/opt/uzasbo2-ai/venv/bin:/usr/local/bin:/usr/bin"
EnvironmentFile=/opt/uzasbo2-ai/.env
ExecStart=/opt/uzasbo2-ai/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8100 --workers 4
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# Xizmatni yoqish va ishga tushirish
sudo systemctl daemon-reload
sudo systemctl enable uzasbo2-ai
sudo systemctl start uzasbo2-ai

# Tekshirish
sudo systemctl status uzasbo2-ai
curl http://localhost:8100/health
```

---

## 8-Bosqich: Nginx Reverse Proxy

```bash
sudo apt install -y nginx

sudo tee /etc/nginx/sites-available/uzasbo2-ai << 'EOF'
server {
    listen 80;
    server_name ai.your-domain.uz;

    location / {
        proxy_pass http://127.0.0.1:8100;
        proxy_http_version 1.1;

        # WebSocket
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # LLM javob uchun timeout
        proxy_read_timeout 120s;
        proxy_send_timeout 120s;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/uzasbo2-ai /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx

# SSL (ixtiyoriy)
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d ai.your-domain.uz
```

---

## 9-Bosqich: Firewall

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

---

## 10-Bosqich: Tekshirish

```bash
# 1. Ollama ishlayaptimi?
ollama list
ollama ps

# 2. ChromaDB va Redis ishlayaptimi?
sudo systemctl status chromadb
redis-cli ping

# 3. AI Service ishlayaptimi?
sudo systemctl status uzasbo2-ai

# 4. Health check
curl http://localhost:8100/health
# Kutilgan natija:
# {"status":"ok","ollama_connected":true,"chroma_connected":true,
#  "redis_connected":true,"knowledge_base_chunks":15487}

# 5. Test savol
curl -X POST http://localhost:8100/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message": "To'\''lov topshiriqnomasi nima?", "session_id": "test", "language": "uz_latn"}'
```

---

## Tezkor Buyruqlar

```bash
# --- Ollama ---
sudo systemctl start ollama
sudo systemctl stop ollama
sudo systemctl restart ollama
ollama ps                          # Model holati

# --- AI Service ---
sudo systemctl start uzasbo2-ai
sudo systemctl stop uzasbo2-ai
sudo systemctl restart uzasbo2-ai
journalctl -u uzasbo2-ai -f        # Loglar

# --- ChromaDB ---
sudo systemctl start chromadb
sudo systemctl stop chromadb
sudo systemctl restart chromadb
journalctl -u chromadb -f

# --- Redis ---
sudo systemctl start redis-server
sudo systemctl stop redis-server
sudo systemctl restart redis-server
redis-cli ping

# --- Hammasini bir vaqtda ishga tushirish ---
sudo systemctl start ollama chromadb redis-server uzasbo2-ai

# --- Hammasini bir vaqtda to'xtatish ---
sudo systemctl stop uzasbo2-ai chromadb redis-server ollama

# --- Knowledge Base yangilash ---
cd /opt/uzasbo2-ai && source venv/bin/activate
python scripts/load_knowledge_base.py --force

# --- Yangilash (update) ---
cd /opt/uzasbo2-ai
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart uzasbo2-ai
```

---

## CPU da Tezlik Oshirish Maslahatlar

| Model | RAM | Javob vaqti (CPU) |
|-------|-----|-------------------|
| llama3.1:8b | 5 GB | 30-60 sek |
| **qwen2.5:3b** | **2 GB** | **10-20 sek** |
| phi3:mini (3.8B) | 2.3 GB | 12-25 sek |

Hozirgi konfiguratsiyada `qwen2.5:3b` ishlatiladi — CPU da eng tez variant.

Agar javob sifati yetarli bo'lmasa, modelni kattaroqqa almashtirish mumkin:
```bash
ollama pull llama3.1:8b
# .env da OLLAMA_MODEL=llama3.1:8b ga o'zgartiring
sudo systemctl restart uzasbo2-ai
```
