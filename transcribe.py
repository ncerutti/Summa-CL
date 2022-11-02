import whisper

def transcribe(track_path: str) -> str:
    """
    Perform speech recognition on a track and return the transcript.
    """
    print("Transcribing {track_path}...")
    model = whisper.load_model('base')
    result = model.transcribe(track_path)
    # save result['text'] to a file
    with open(f'{track_path}.txt', 'w') as f:
        f.write(result['text'])
    return result['text']