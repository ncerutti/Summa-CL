def separate_track(path: str) -> list[str]:
    """Function that separates an audio track with 1 or more speakers to 1 track per speaker.

    Args:
        track_path (str): path to the audio file to separate (.wav)

    Returns:
        str: List of paths of separated tracks.
    """
    print("Separating audio in {path}...")
    listone = []
    listone.append(path)
    return listone
