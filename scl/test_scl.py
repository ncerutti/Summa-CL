from transcribe import transcribe


def test_transcribe():
    """Test the transcribe function"""
    test_path = "./testdata/test.wav"
    result = transcribe(test_path)

    assert result == "main.py"
