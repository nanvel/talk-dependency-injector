from todopy.enumerators import SequenceEnumerator


def test_sequence_enumerator():
    shelf = {}

    enumerator = SequenceEnumerator(shelf=shelf)

    assert next(enumerator) == 0
    assert next(enumerator) == 1
    assert shelf[SequenceEnumerator.SEQUENCE_KEY] == 1
