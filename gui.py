# type: ignore

import threading
import time
import tkinter as tk
import wave
from datetime import datetime

import pyaudio


class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("SCL")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.rec_button = tk.Button(
            self.root, text="Record", command=self.record_click_handler
        )
        self.rec_button.pack()
        self.rec_label = tk.Label(self.root, text="00:00:00")
        self.rec_label.pack()
        self.sep_button = tk.Button(
            self.root, text="Separate", command=self.separate_click_handler
        )
        self.sep_button.pack()
        self.recording = False
        self.root.mainloop()

    def record_click_handler(self) -> None:
        if self.recording:
            self.recording = False
            self.rec_button.config(fg="black", text="Record")
        else:
            self.recording = True
            self.rec_button.config(fg="red", text="Stop")
            threading.Thread(target=self.record).start()

    def separate_click_handler(self) -> None:

        pass

    def record(self) -> None:
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )
        frames = []
        start = time.time()
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
            self.rec_label.config(
                text=time.strftime("%H:%M:%S", time.gmtime(time.time() - start))
            )
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wavfile = wave.open(f"{datetime.now().strftime('%d%m_%H%M')}.wav", "wb")
        wavfile.setnchannels(2)
        wavfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wavfile.setframerate(44100)
        wavfile.writeframes(b"".join(frames))
        wavfile.close()
