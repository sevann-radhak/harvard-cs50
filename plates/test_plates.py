from plates import is_valid


def test_is_valid_empty():
    assert is_valid('') == False
    assert is_valid(' ') == False


def test_is_valid_len():
    assert is_valid('A') == False
    assert is_valid('A ') == False
    assert is_valid(' A ') == False
    assert is_valid('ABCDEFG') == False
    assert is_valid('AB') == True
    assert is_valid('ABCDE') == True
    assert is_valid('ABCDEF') == True


def test_is_valid_starts_with_alpha():
    assert is_valid('12ABCD') == False
    assert is_valid('1ABCDE') == False
    assert is_valid('A1BCDE') == False
    assert is_valid('ABCDEF') == True
    assert is_valid('abCDEF') == True
    assert is_valid('ab1234') == True
    assert is_valid('a12345') == False


def test_is_valid_nums():
    assert is_valid('AB1c') == False
    assert is_valid('AB123C') == False
    assert is_valid('ABCDE1') == True
    assert is_valid('ABCDE0') == False
    assert is_valid('ABC012') == False


def test_is_valid_alnum():
    assert is_valid('*CS50') == False
    assert is_valid('CS50!') == False
