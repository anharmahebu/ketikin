"""Auto-paste ke app aktif: set clipboard + kirim Ctrl+V."""
import time
import pyperclip
import keyboard


def paste(text):
    if not text:
        return
    pyperclip.copy(text)
    time.sleep(0.05)  # kasih clipboard waktu ke-set
    keyboard.send("ctrl+v")
