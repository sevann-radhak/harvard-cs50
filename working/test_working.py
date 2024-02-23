from working import convert

def test_convert():
    assert convert('11:59 AM to 12:00 PM') == '11:59 to 12:00'
    assert convert('11:59 PM to 12:00 AM') == '23:59 to 00:00'
    assert convert('12:59 PM to 1:00 PM') == '12:59 to 13:00'
    assert convert('12:59 AM to 1:00 AM') == '00:59 to 01:00'
    assert convert('1:59 AM to 2:00 AM') == '01:59 to 02:00'
    assert convert('1:59 PM to 2:00 PM') == '13:59 to 14:00'
    assert convert('1:59 PM to 2:00 AM') == '13:59 to 02:00'
    assert convert('1:59 AM to 2:00 PM') == '01:59 to 14:00'
    assert convert('11:59 AM to 11:59 PM') == '11:59 to 23:59'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'
    assert convert('12:00 PM to 12:00 PM') == '12:00 to 12:00'
    assert convert('12:00 AM to 12:00 AM') == '00:00 to 00:00'
    assert convert('1:00 AM to 1:00 AM') == '01:00 to 01:00'
    assert convert('1:00 PM to 1:00 PM') == '13:00 to 13:00'
    assert convert('1:00 PM to 1:00 AM') == '13:00 to 01:00'
    assert convert('1:00 AM to 1:00 PM') == '01:00 to 13:00'
    assert convert('11:59 PM to 11:59 AM') == '23:59 to 11:59'
    assert convert('11:59 PM to 11:59 PM') == '23:59 to 23:59'
    assert convert('11:59 AM to 11:59 AM') == '11:59 to 11:59'


def test_invalid():
    try:
        convert('11:60 AM to 03:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('cat AM to dog PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('01:00 A M to 01:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 13:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 12:60 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 12:00 PM to 12:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 12:00 PM to 12:00 PM to 12:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 12:00 PM to 12:00 PM to 12:00 PM to 12:00 PM')
        assert False
    except ValueError:
        assert True
    try:
        convert('11:59 AM to 12:00 PM to 12:00 PM to 12:00 PM to 12:00 PM to 12:00 PM')
        assert False
    except ValueError:
        assert True
