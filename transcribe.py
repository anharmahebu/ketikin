"""STT via Groq Whisper large-v3. Audio numpy -> teks mentah. Online, gratis."""
import io
import wave
import numpy as np
from openai import OpenAI

from config import GROQ_STT_MODEL, WHISPER_LANGUAGE, LLM_API_KEY, LLM_BASE_URL

_client = None


def _get_client():
    global _client
    if _client is None:
        _client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL, timeout=30.0)
    return _client


def _wav_bytes(audio):
    """float32 mono 16k -> WAV bytes (PCM16) buat dikirim ke API."""
    pcm = (np.clip(audio, -1.0, 1.0) * 32767).astype(np.int16)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(16000)
        w.writeframes(pcm.tobytes())
    return buf.getvalue()


def transcribe(audio):
    """audio: numpy float32 mono 16kHz. Return teks mentah (str)."""
    if audio is None or len(audio) == 0:
        return ""
    resp = _get_client().audio.transcriptions.create(
        model=GROQ_STT_MODEL,
        file=("audio.wav", _wav_bytes(audio), "audio/wav"),
        language=WHISPER_LANGUAGE or None,
        temperature=0,
    )
    return resp.text.strip()
