# Function that returns a list of strings,
# each string being a path to a file.


def separate_track(path: str) -> list[str]:
    # Separate audio into different tracks (one for each speaker)
    print("Separating audio in {path}...")
    listone = []
    listone.append(path)
    return listone
