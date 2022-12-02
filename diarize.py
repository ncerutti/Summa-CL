from pyannote.audio import Pipeline


def diarize(path: str) -> None:
    """Diarize the audio file at the given path."""
    print("Diarizing file at path: ", path)
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization@2.1",
        use_auth_token="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",
    )
    diarization = pipeline(path, min_speakers=3, max_speakers=6)
    # eventually I should have the same filename with a different extension
    # I kind of like the idea of having the files in different folders
    print(diarization)
    # well, considering that it's taken from the phone with the pre-trained model...
    # could be worse! However, that is not satisfactory.
    with open("./tmp/diary/1.rttm", "w") as rttm:
        diarization.write_rttm(rttm)
