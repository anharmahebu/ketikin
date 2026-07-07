# Ketikin

Klon lokal & gratis dari [Wispr Flow](https://wisprflow.ai): **lu ngomong, dia yang ngetikin**.

Tahan hotkey → ngomong → lepas → teks rapi langsung ke-paste di aplikasi yang lagi aktif.

```
Tahan hotkey  →  ngomong  →  lepas
      │
      ▼  rekam mic
      ▼  STT (Groq Whisper)      →  teks mentah
      ▼  formatting (Groq LLM)   →  teks rapi
      ▼  auto-paste (Ctrl+V) ke app yang lagi fokus
```

Contoh: *"ehm... tolong kirim laporan itu ke budi ya besok pagi"* → **"Tolong kirim laporan itu ke Budi besok pagi."**

## Butuh apa

- **Windows 11** (belum cross-platform).
- **Python 3.9+**.
- **Internet** — STT & LLM lewat cloud (Groq).
- **API key Groq** (gratis): bikin di https://console.groq.com/keys

## Install

```bash
pip install -r requirements.txt
```

## Setup

1. Copy `.env.example` jadi `.env`.
2. Isi `LLM_API_KEY` pakai key Groq lu. Jangan commit `.env` (udah di-`.gitignore`).

```bash
cp .env.example .env
```

Isi `.env`:

| Variabel | Default | Guna |
|---|---|---|
| `LLM_API_KEY` | — | Key Groq. Dipakai buat STT **dan** LLM. **Wajib.** |
| `LLM_BASE_URL` | `https://api.groq.com/openai/v1` | Endpoint OpenAI-compatible. |
| `LLM_MODEL` | `llama-3.3-70b-versatile` | Model buat mrapiin teks. |
| `GROQ_STT_MODEL` | `whisper-large-v3-turbo` | Model Whisper buat STT. |
| `HOTKEY` | `` alt+` `` | Push-to-talk. |
| `WHISPER_LANGUAGE` | `id` | Bahasa utama. |

## Jalanin

```bash
python main.py
```

Tahan **hotkey** → ngomong → lepas → teks ke-paste. `Ctrl+C` di terminal buat berhenti.

> **Windows note:** `keyboard` butuh akses global hotkey. Kalau hotkey/paste gak jalan, jalanin terminal sebagai **Administrator**.

## File

| File | Guna |
|---|---|
| `recorder.py` | Rekam mic (stream persisten, nol delay awal). |
| `transcribe.py` | Audio → teks mentah (Groq Whisper). |
| `formatter.py` | Teks mentah → teks rapi (Groq LLM). |
| `paster.py` | Set clipboard + kirim Ctrl+V. |
| `config.py` | Konfig terpusat (baca `.env`). |
| `main.py` | Loop hotkey, gabungin semua. |

## Lisensi

Bebas pakai. Nol rupiah.
