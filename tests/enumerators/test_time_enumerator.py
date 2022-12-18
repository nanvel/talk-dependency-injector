from todopy.enumerators import TimeEnumerator


def test_time_enumerator():
    enumerator = TimeEnumerator()

    assert isinstance(next(enumerator), int)
