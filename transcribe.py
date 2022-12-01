# type: ignore

import whisper

# Right now this uses the default model, eventually we should be able to choose with different arguments.


def transcribe(n_tracks: int) -> list[str]:
    """Function that transcribes an audio track using whisper.

    Args:
        n_tracks (int): number of tracks to transcribe. All tracks are found in the ./tmp/separated/ folder.

    Returns:
        str: text file with the transcription. It will also write the file to the /tmp folder.
    """
    print(
        "Note that so far, and with this model, it works decently only with good quality audio."
    )
    print("Transcribing {track_path}...")
    model = whisper.load_model("small.en")
    transcriptions = []
    for i in range(n_tracks):
        result = model.transcribe(f"./tmp/separated/{i}.wav")
        # save result['text'] to a file
        with open(f"./tmp/transcribed/{i}.txt", "w+", encoding="utf-8") as f:
            f.write(result["text"])
            transcriptions.append(result["text"])
    return transcriptions
