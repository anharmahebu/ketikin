"""Rekam mic. Stream dibuka SEKALI & nyala terus; rekam = nyalain flag.

Kenapa gini: buka-tutup stream tiap rekam ada delay ~100-200ms -> awal
ngomong kepotong ("ilang-ilangan"). Stream persisten = nol delay.
"""
import numpy as np
import sounddevice as sd
from config import SAMPLE_RATE


class Recorder:
    def __init__(self):
        self._chunks = []
        self._recording = False
        self._stream = sd.InputStream(
            samplerate=SAMPLE_RATE, channels=1, dtype="float32",
            blocksize=0, callback=self._callback,
        )
        self._stream.start()  # nyala terus sejak awal

    def _callback(self, indata, frames, time, status):
        if self._recording:
            self._chunks.append(indata.copy())

    def start(self):
        self._chunks = []
        self._recording = True

    def stop(self):
        self._recording = False
        if not self._chunks:
            return np.zeros(0, dtype=np.float32)
        return np.concatenate(self._chunks, axis=0).flatten()
