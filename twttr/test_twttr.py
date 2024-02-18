from twttr import shorten 


def test_shorten_empty():
    assert shorten('') == ''


def test_shorten_lower():
    assert shorten('hello') == 'hll'
    assert shorten('Hello') == 'Hll'
    assert shorten('aeiou') == ''


def test_shorten_lower():
    assert shorten('AEIOU') == ''
    assert shorten('hEllO') == 'hll'


