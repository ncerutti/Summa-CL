import whisper

# Right now this uses the default model, eventually we should be able to choose with different arguments.


def transcribe(track_path: str) -> str:
    """Function that transcribes an audio track using whisper.

    Args:
        track_path (str): path to an audio file to transcribe (.wav)

    Returns:
        str: text file with the transcription. It will also write the file to the /tmp folder.
    """
    print(
        "Note that so far, and with this model, it works decently only with good quality audio."
    )
    print("Transcribing {track_path}...")
    model = whisper.load_model("small")
    result = model.transcribe(track_path)
    # save result['text'] to a file
    with open(f"{track_path}.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    return result["text"]
