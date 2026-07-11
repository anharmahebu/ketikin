"""Konfigurasi terpusat. Baca dari .env."""
import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")

HOTKEY = os.getenv("HOTKEY", "alt+`")

WHISPER_LANGUAGE = os.getenv("WHISPER_LANGUAGE", "id")
GROQ_STT_MODEL = os.getenv("GROQ_STT_MODEL", "whisper-large-v3-turbo")

SAMPLE_RATE = 16000  # Whisper maunya 16kHz mono
