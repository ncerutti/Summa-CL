import os


def clean() -> None:
    """Clean the temporary files."""
    # for file in os.listdir("./tmp/recorded"):
    #    os.remove(os.path.join("./tmp/recorded", file))
    for file in os.listdir("./tmp/separated"):
        os.remove(os.path.join("./tmp/separated", file))
    for file in os.listdir("./tmp/transcribed"):
        os.remove(os.path.join("./tmp/transcribed", file))
    # for file in os.listdir("./tmp/summary"):
    #    os.remove(os.path.join("./tmp/summary", file))


def clean_process() -> None:
    """Clean the temporary files."""
    for file in os.listdir("./tmp/recorded"):
        os.remove(os.path.join("./tmp/recorded", file))
