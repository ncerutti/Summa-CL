# type: ignore

from datetime import datetime
import torch

from clean import clean, clean_process
from diarize import diarize
from enhance import enhance
from record import Recorder, StreamParams
from separate import separate_track
from transcribe import transcribe


def main() -> None:
    """Main function. At the moment calling sequentially the other functions."""

    # empty GPU memory
    torch.cuda.empty_cache()

    empty_tmp_folder = input("Do you want to clean the tmp folder? (y/n) ")
    if empty_tmp_folder == "y":
        clean()
        print("Cleaned folders from previous runs.")

    #                    Record audio

    record = input("Do you want to record audio? (y/n) ")
    if record == "y":
        stream_params = StreamParams()
        recorder = Recorder(stream_params)
        recording_path = f"./tmp/recorded/{datetime.now().strftime('%d%m_%H%M')}.wav"
        recorder.record(recording_path)
    if record == "n":
        # search in tmp/recorded for the latest file
        recording_path = "./tmp/test_file/test.wav"

    print(record)
    if record == "y":
        enhance(recording_path)

    #                   Diarization

    diarize(recording_path)

    #                   Separate audio tracks

    num_tracks = separate_track(recording_path)

    #              Perform speech recognition
    #   on each track and assign a speaker to each track

    transcriptions = transcribe(num_tracks)
    print(f"Transcribed {len(transcriptions)} tracks.")

    keep_only_transcriptions = input("Do you want to remove the original audio? (y/n) ")
    if keep_only_transcriptions == "y":
        clean_process()
        print("Cleaned original audio folder.")

    print("All worked out, apparently.")


#                       Generate a summary


if __name__ == "__main__":
    main()
