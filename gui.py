import tkinter as tk
import threading
from record import Recorder, StreamParams


class GUI():

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("SCL")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.button = tk.Button(self.root, text="Record", command=self.click_handler)
        self.button.pack()
        self.label = tk.Label(self.root, text="00:00")
        self.label.pack()
        self.recording=False
        self.root.mainloop()

    def click_handler(self) -> None:
        if self.recording:
            self.recording=False
            self.button.config(fg="black", text="Record")
        else:
            self.recording=True
            self.button.config(fg="red", text="Stop")
            recorder = Recorder(StreamParams())
            recording_path = f"{datetime.now().strftime('%d%m_%H%M')}.wav"
            threading.Thread(target=recorder.record(recording_path).start())
        pass