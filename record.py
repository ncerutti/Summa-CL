import pyaudio
import wave
from dataclasses import dataclass, asdict


@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 2
    rate: int = 44100
    frames_per_buffer: int = 1024
    input: bool = True
    output: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


class Recorder:
    """Uses pyaudio to record from microphone.

    Attributes:
        - StreamParams object with values for the stream"""

    def __init__(self, stream_params: StreamParams) -> None:
        self._pyaudio = None
        self.stream_params = stream_params
        self.stream = None
        self._wav_file = None

    def record(self, save_path: str, duration: int = 0) -> None:
        """Records audio for a given duration and saves it
        to a wav file.

        duration: number of seconds to record
        save_path: path to save the wav file"""
        print("Now recording...")
        self._pyaudio = pyaudio.PyAudio()
        self._stream = self._pyaudio.open(**self.stream_params.to_dict())
        self._create_wav_file(save_path)

        if duration == 0:

            print('Press "q" to stop recording')
            try:
                while True:
                    data = self._stream.read(self.stream_params.frames_per_buffer)
                    self._wav_file.writeframes(data)
            except KeyboardInterrupt:
                pass

        else:
            print(f"Recording for {duration} seconds")
            for _ in range(
                0,
                int(
                    self.stream_params.rate
                    * duration
                    / self.stream_params.frames_per_buffer
                ),
            ):
                data = self._stream.read(self.stream_params.frames_per_buffer)
                self._wav_file.writeframes(data)

        self._close_recording_resources()
        print("Recording finished.")

    def _create_wav_file(self, save_path: str):
        self._wav_file = wave.open(save_path, "wb")
        self._wav_file.setnchannels(self.stream_params.channels)
        self._wav_file.setsampwidth(
            self._pyaudio.get_sample_size(self.stream_params.format)
        )
        self._wav_file.setframerate(self.stream_params.rate)

    def _write_wav_file_from_stream(self, duration: int) -> None:
        """Writes the wav file from the stream.
        If duration is 0, it will write until the user presses "q".
        Otherwise, it will write for the given duration."""
        # q: why doesn't this save the file?
        # a: because the file is closed before the data is written
        if duration == 0:
            for i in range(10):
                data = self._stream.read(self.stream_params.frames_per_buffer)
                self._wav_file.writeframes(data)
                i = i - 1
                if input() == "q":
                    i = i + 10
        else:
            for _ in range(
                0,
                int(
                    self.stream_params.rate
                    * duration
                    / self.stream_params.frames_per_buffer
                ),
            ):
                data = self._stream.read(self.stream_params.frames_per_buffer)
                self._wav_file.writeframes(data)

    def _close_recording_resources(self) -> None:
        self._stream.stop_stream()
        self._stream.close()
        self._pyaudio.terminate()
        self._wav_file.close()
