# Ketikin

Klon lokal & gratis dari [Wispr Flow](https://wisprflow.ai): **lu ngomong, dia yang ngetikin**.

Tahan hotkey → ngomong → lepas → teks langsung ke-paste di aplikasi yang lagi aktif.

```
Tahan hotkey  →  ngomong  →  lepas
      │
      ▼  rekam mic
      ▼  STT (Groq Whisper)      →  teks
      ▼  auto-paste (Ctrl+V) ke app yang lagi fokus
```

Contoh: *"tolong kirim laporan itu ke budi ya besok pagi"* → ke-paste apa adanya dari hasil STT.

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
| `LLM_API_KEY` | — | Key Groq. Dipakai buat STT. **Wajib.** |
| `LLM_BASE_URL` | `https://api.groq.com/openai/v1` | Endpoint OpenAI-compatible. |
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
| `transcribe.py` | Audio → teks (Groq Whisper). |
| `paster.py` | Set clipboard + kirim Ctrl+V. |
| `config.py` | Konfig terpusat (baca `.env`). |
| `main.py` | Loop hotkey, gabungin semua. |

## Lisensi

Bebas pakai. Nol rupiah.
