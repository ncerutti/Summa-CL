# type: ignore

from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio


def separate_track(path: str) -> int:
    """Function that separates an audio track with 1 or more speakers to 1 track per speaker.

    Args:
        track_path (str): path to the audio file to separate (.wav)

    Returns:
        int: number of separate tracks.
    """
    print("Separating audio in {path}...")
    model = separator.from_hparams(
        source="speechbrain/sepformer-whamr",
        savedir="pretrained_models/sepformer-whamr",
    )
    # open audio file from path and convert to 8kHz single channel

    waveform, sample_rate = torchaudio.load(path)
    waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=8000)(
        waveform
    )
    waveform = waveform.mean(dim=0, keepdim=True)

    # save waveform to a temporary file

    torchaudio.save(path, waveform, 8000)
    est_sources = model.separate_file(path)
    tracks = est_sources.shape[2]

    print(f"Separated audio in {path} into {tracks} tracks.")
    for i in range(tracks):
        torchaudio.save(f"./tmp/separated/{i}.wav", est_sources[:, :, i], 8000)

    return tracks
