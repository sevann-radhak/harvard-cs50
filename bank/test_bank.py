from bank import value

def test_value_100():
    assert value('') == 100
    assert value('aeiou') == 100
    assert value('_h') == 100


def test_value_20():
    assert value('h') == 20
    assert value('H') == 20
    assert value('hell') == 20
    assert value('Hell') == 20
    assert value('hEl') == 20  
    assert value('HeL') == 20
    assert value('Hhello') == 20
    assert value('Hi') == 20


def test_0():
    assert value('Hello') == 0
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hElLo') == 0
    assert value('Hellohello') == 0
    assert value('Hello World!') == 0