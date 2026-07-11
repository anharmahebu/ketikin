"""Ketikin — dikte suara -> teks (STT) -> auto-paste.

Tahan HOTKEY -> ngomong -> lepas -> teks STT ke-paste di app aktif.
Ctrl+C di terminal buat berhenti.
"""
import time
import keyboard

from config import HOTKEY
from recorder import Recorder
from transcribe import transcribe
from paster import paste

_KEYS = [k.strip() for k in HOTKEY.split("+") if k.strip()]


def _hotkey_down():
    return all(keyboard.is_pressed(k) for k in _KEYS)


def main():
    print("=== Ketikin ===")
    print(f"Siap. Tahan [{HOTKEY}] buat ngomong. Ctrl+C buat keluar.\n")

    rec = Recorder()

    while True:
        # Tunggu hotkey ditahan
        if not _hotkey_down():
            time.sleep(0.03)
            continue

        print("Rekam...")
        rec.start()
        while _hotkey_down():
            time.sleep(0.03)
        audio = rec.stop()
        import numpy as np
        peak = float(np.abs(audio).max()) if len(audio) else 0.0
        print(f"Selesai rekam ({len(audio)/16000:.1f}s, peak {peak:.2f}). Proses...")
        if peak < 0.02:
            print("  (!) Suara kekecilan/ga kedengeran. Naikin volume mic / deketin.")

        try:
            raw = transcribe(audio)
        except Exception as e:
            print(f"[stt] Gagal ({e}). Cek internet / limit Groq. Skip.\n")
            continue
        if not raw:
            print("(kosong / ga kedengeran)\n")
            continue
        print(f"Teks   : {raw}")

        paste(raw)
        print("Ke-paste.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDah, bye.")
