# UzASBO 2.0 AI Assistant — Ubuntu Serverga Deploy Qilish

## Tizim Talablari

| Komponent | Minimal | Tavsiya etilgan |
|-----------|---------|-----------------|
| OS | Ubuntu 22.04 LTS | Ubuntu 24.04 LTS |
| CPU | 4 core | 8+ core |
| RAM | 16 GB | 32 GB |
| Disk | 50 GB SSD | 100 GB NVMe SSD |
| GPU | - | NVIDIA RTX 3060+ (12GB VRAM) |

> GPU bo'lsa — javob 2-3 sekundda. CPU da — 30-60 sekund.

---

## 1-Bosqich: Serverni Tayyorlash

```bash
# Tizimni yangilash
sudo apt update && sudo apt upgrade -y

# Kerakli paketlarni o'rnatish
sudo apt install -y curl git wget htop net-tools
```

---

## 2-Bosqich: Docker O'rnatish

```bash
# Docker GPG kaliti
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Docker repository qo'shish
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Docker o'rnatish
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Docker ni sudo siz ishlatish
sudo usermod -aG docker $USER
newgrp docker

# Tekshirish
docker --version
docker compose version
```

---

## 3-Bosqich: NVIDIA GPU Driver (GPU bo'lsa)

> GPU yo'q bo'lsa — bu bosqichni o'tkazib yuboring, 4-bosqichga o'ting.

```bash
# NVIDIA driver o'rnatish
sudo apt install -y nvidia-driver-535

# Qayta yuklash
sudo reboot

# Driver tekshirish (qayta ulanganingizdan keyin)
nvidia-smi
```

### NVIDIA Container Toolkit (Docker ichida GPU ishlatish uchun)

```bash
# Repository qo'shish
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# O'rnatish
sudo apt update
sudo apt install -y nvidia-container-toolkit

# Docker ni GPU bilan sozlash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Tekshirish — GPU Docker ichida ko'rinishi kerak
docker run --rm --gpus all nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi
```

---

## 4-Bosqich: Loyihani Serverga Ko'chirish

### Variant A: Git orqali (tavsiya etiladi)

```bash
# Loyiha uchun papka
sudo mkdir -p /opt/uzasbo2-ai
sudo chown $USER:$USER /opt/uzasbo2-ai
cd /opt/uzasbo2-ai

# Git dan klonlash (o'zingizning repo URL ni yozing)
git clone https://your-repo-url/uzasbo2_ai_assistant.git .
```

### Variant B: SCP bilan ko'chirish (git ishlatmasangiz)

```bash
# Lokal kompyuterdan serverga ko'chirish (Windows PowerShell da)
scp -r D:\Projects\IVC\UZASBO\uzasbo2_ai_assistant user@SERVER_IP:/opt/uzasbo2-ai
```

---

## 5-Bosqich: Docker Compose ni GPU uchun Sozlash

### GPU BOR — `docker-compose.prod.yml` yaratish:

```bash
cat > /opt/uzasbo2-ai/docker-compose.prod.yml << 'EOF'
services:

  # --- OLLAMA: GPU bilan ---
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "127.0.0.1:11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped

  # --- MODEL YUKLOVCHI ---
  ollama-pull:
    image: ollama/ollama:latest
    container_name: ollama-pull
    depends_on:
      - ollama
    environment:
      - OLLAMA_HOST=http://ollama:11434
    entrypoint: >
      sh -c "
        echo 'Ollama kutilmoqda...' &&
        sleep 15 &&
        echo 'llama3.1:8b yuklanmoqda...' &&
        ollama pull llama3.1:8b &&
        echo 'nomic-embed-text yuklanmoqda...' &&
        ollama pull nomic-embed-text &&
        echo 'Barcha modellar yuklandi!'
      "
    restart: "no"

  # --- CHROMADB ---
  chromadb:
    image: chromadb/chroma:latest
    container_name: chromadb
    ports:
      - "127.0.0.1:8000:8000"
    volumes:
      - chroma_data:/chroma/chroma
    environment:
      - ANONYMIZED_TELEMETRY=FALSE
      - IS_PERSISTENT=TRUE
    restart: unless-stopped

  # --- REDIS ---
  redis:
    image: redis:7-alpine
    container_name: redis
    ports:
      - "127.0.0.1:6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru
    restart: unless-stopped

  # --- AI SERVICE ---
  ai-service:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: uzasbo2-ai-assistant
    ports:
      - "0.0.0.0:8100:8100"
    volumes:
      - ./knowledge_base:/app/knowledge_base
      - ./logs:/app/logs
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - OLLAMA_MODEL=llama3.1:8b
      - OLLAMA_EMBED_MODEL=nomic-embed-text
      - CHROMA_HOST=chromadb
      - CHROMA_PORT=8000
      - CHROMA_COLLECTION=uzasbo2_knowledge
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - REDIS_DB=0
      - APP_PORT=8100
      - APP_DEBUG=False
      - CORS_ORIGINS=http://localhost:3000,http://your-domain.uz
      - RAG_TOP_K=5
      - RAG_TEMPERATURE=0.2
      - RAG_CHUNK_SIZE=800
      - RAG_CHUNK_OVERLAP=200
    depends_on:
      - ollama
      - chromadb
      - redis
    restart: unless-stopped

volumes:
  ollama_data:
  chroma_data:
  redis_data:
EOF
```

### GPU YO'Q — oddiy `docker-compose.prod.yml`:

```bash
# Yuqoridagi fayldan faqat ollama service dagi
# deploy: ... devices: ... qismini olib tashlang.
# Qolgani bir xil.

# Tezroq ishlashi uchun kichikroq model:
# OLLAMA_MODEL=qwen2.5:3b (yoki phi3:mini)
```

---

## 6-Bosqich: Ishga Tushirish

```bash
cd /opt/uzasbo2-ai

# Docker image ni build qilish va ishga tushirish
docker compose -f docker-compose.prod.yml up -d --build

# Modellar yuklanishini kuzatish (birinchi marta ~5 daqiqa)
docker logs -f ollama-pull

# Barcha containerlar ishlayotganini tekshirish
docker ps

# Health check
curl http://localhost:8100/health
```

---

## 7-Bosqich: Knowledge Base Yuklash

```bash
# ChromaDB ga bilim bazasini yuklash
docker exec uzasbo2-ai-assistant python scripts/load_knowledge_base.py --force

# Tekshirish — knowledge_base_chunks > 0 bo'lishi kerak
curl http://localhost:8100/health
```

---

## 8-Bosqich: Nginx Reverse Proxy (Production uchun)

```bash
# Nginx o'rnatish
sudo apt install -y nginx

# Konfiguratsiya yaratish
sudo cat > /etc/nginx/sites-available/uzasbo2-ai << 'EOF'
server {
    listen 80;
    server_name ai.your-domain.uz;  # O'zingizning domenni yozing

    # API va WebSocket uchun
    location / {
        proxy_pass http://127.0.0.1:8100;
        proxy_http_version 1.1;

        # WebSocket qo'llab-quvvatlash
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Timeout — LLM javob generatsiyasi uchun
        proxy_read_timeout 120s;
        proxy_send_timeout 120s;
    }
}
EOF

# Saytni yoqish
sudo ln -s /etc/nginx/sites-available/uzasbo2-ai /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

### SSL Sertifikat (HTTPS) — Let's Encrypt

```bash
# Certbot o'rnatish
sudo apt install -y certbot python3-certbot-nginx

# SSL sertifikat olish (domen DNS sozlangan bo'lishi kerak)
sudo certbot --nginx -d ai.your-domain.uz

# Avtomatik yangilash tekshirish
sudo certbot renew --dry-run
```

---

## 9-Bosqich: Firewall Sozlash

```bash
# UFW yoqish
sudo ufw allow 22/tcp      # SSH
sudo ufw allow 80/tcp      # HTTP
sudo ufw allow 443/tcp     # HTTPS
sudo ufw enable

# Ichki portlar (11434, 8000, 6379) tashqaridan yopiq qoladi
# chunki docker-compose da 127.0.0.1 ga bind qilingan
```

---

## 10-Bosqich: Avtomatik Ishga Tushish (Reboot dan keyin)

```bash
# Docker xizmati avtomatik ishga tushadi
sudo systemctl enable docker

# Containerlar restart: unless-stopped bilan sozlangan,
# shuning uchun server qayta ishga tushganda ham ishlaydi.
```

---

## 11-Bosqich: Monitoring va Loglar

```bash
# Barcha containerlar holati
docker ps

# AI service loglari
docker logs -f uzasbo2-ai-assistant --tail 100

# Ollama loglari (GPU/CPU yuklanish)
docker logs -f ollama --tail 50

# Disk hajmi tekshirish
docker system df

# Eski image larni tozalash
docker system prune -f
```

---

## Tezlikni Oshirish Bo'yicha Tavsiyalar

### 1. GPU ishlatish (eng muhim)
| Holat | Javob vaqti |
|-------|-------------|
| CPU (i7-9700) | 30-60 sek |
| NVIDIA RTX 3060 (12GB) | 3-5 sek |
| NVIDIA RTX 4090 (24GB) | 1-2 sek |

### 2. Model tanlash
| Model | VRAM | Sifat | Tezlik |
|-------|------|-------|--------|
| llama3.1:8b | 5 GB | Yaxshi | O'rtacha |
| qwen2.5:7b | 4.5 GB | Yaxshi | Tez |
| qwen2.5:3b | 2 GB | O'rtacha | Juda tez |
| phi3:mini (3.8B) | 2.3 GB | Yaxshi | Tez |

### 3. Ollama sozlamalari (tezlik uchun)
```bash
# docker-compose.prod.yml da ollama service ga qo'shish:
environment:
  - OLLAMA_NUM_PARALLEL=4        # Bir vaqtda 4 ta so'rov
  - OLLAMA_MAX_LOADED_MODELS=2   # 2 ta model RAM da turadi
  - OLLAMA_FLASH_ATTENTION=1     # Tez attention (GPU uchun)
```

### 4. Uvicorn workers soni
```dockerfile
# Dockerfile da CMD ni o'zgartirish:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8100", "--workers", "4"]
```

---

## Xatoliklarni Bartaraf Etish

### Ollama GPU ni ko'rmayapti
```bash
# GPU driver tekshirish
nvidia-smi

# Docker ichida GPU tekshirish
docker exec ollama nvidia-smi

# Agar ko'rinmasa — nvidia-container-toolkit qayta o'rnatish
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### ChromaDB ulanmayapti
```bash
docker logs chromadb --tail 20
# Port band bo'lsa:
sudo lsof -i :8000
```

### RAM yetishmayapti
```bash
# RAM holati
free -h

# Swap qo'shish (16 GB)
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### AI Service ishga tushmayapti
```bash
docker logs uzasbo2-ai-assistant --tail 50
# Odatda sabab: Ollama yoki ChromaDB hali tayyor emas
# Yechim: qayta ishga tushirish
docker restart uzasbo2-ai-assistant
```

---

## Yangilash (Update)

```bash
cd /opt/uzasbo2-ai

# Yangi kodni olish
git pull origin main

# Qayta build va ishga tushirish
docker compose -f docker-compose.prod.yml up -d --build

# Knowledge Base yangilash (agar o'zgargan bo'lsa)
docker exec uzasbo2-ai-assistant python scripts/load_knowledge_base.py --force
```

---

## Tezkor Buyruqlar Ro'yxati

```bash
# Ishga tushirish
docker compose -f docker-compose.prod.yml up -d

# To'xtatish
docker compose -f docker-compose.prod.yml down

# Qayta ishga tushirish
docker compose -f docker-compose.prod.yml restart

# Loglar
docker compose -f docker-compose.prod.yml logs -f

# Health check
curl http://localhost:8100/health

# Test savol
curl -X POST http://localhost:8100/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message": "To'\''lov topshiriqnomasi nima?", "session_id": "test", "language": "uz_latn"}'
```
