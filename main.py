"""

Summa Cum Laude - Main module

Author: ncerutti

"""
import time
from datetime import datetime


from gui import GUI
from init import hwcheck
from record import Recorder, StreamParams
from separate import separate_track
from transcribe import transcribe


def main() -> None:

    # Start the GUI

    gui = GUI()
    #                    Record audio

    stream_params = StreamParams()
    recorder = Recorder(stream_params)
    recording_path = f"{datetime.now().strftime('%d%m_%H%M')}.wav"
    recorder.record(recording_path)

    #                   Separate audio
    #       into different tracks (one for each speaker)

    # tracks = separate_track(recording_path)

    #              Perform speech recognition
    #   on each track and assign a speaker to each track

    # transcriptions = []
    # n_transcriptions = 0
    # for track in tracks:
    #    n_transcriptions += 1
    #    transcriptions += transcribe(track)

    # print(f"Transcribed {n_transcriptions} tracks.")
    # Generate a summary

    # Generate a transcript


if __name__ == "__main__":
    main()
