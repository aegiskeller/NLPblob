from corenlp import summarise_wikipedia, get_text_blob, get_phrases


def test_summarise_wikipedia():
    assert "Cros Araild" in summarise_wikipedia("Harold's Cross")


def test_get_text_blob():
    assert "farrk" == get_text_blob("farrk")


def test_get_phrases():
    assert "francophonie" in get_phrases("Franco")
