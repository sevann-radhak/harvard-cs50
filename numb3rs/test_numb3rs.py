from numb3rs import validate


def test_validate_strings():
    assert validate("aa5.255.255.255") == False
    assert validate("255.a55.255.255") == False
    assert validate("255.255.a5a.255") == False
    assert validate("255.2555.255.5aa") == False
    assert validate("25!.255.255.255") == False
    assert validate("255?255.255.255") == False
    assert validate("255.255?255.255") == False
    assert validate("255.255.255?255") == False
    assert validate("255a255.255.255") == False
    assert validate("255.255a255.255") == False
    assert validate("255.255.255a255") == False
    

def test_extra_octet():
    assert validate(".255.255.255.255") == False
    assert validate("255.255.255.255.") == False
    assert validate("255.255.255.255.255") == False
    

def test_missing_octet():
    assert validate("255.255.255.") == False
    assert validate("255.255.255") == False
    assert validate("255.255.") == False
    assert validate("255.255") == False
    assert validate("255.") == False
    assert validate("255") == False
    assert validate("") == False
  
    
def test_extra_point():
    assert validate(".255.255.255.255") == False
    assert validate("255.255.255.255.") == False
    assert validate("255..255.255.255") == False
    assert validate("255.255..255.255") == False
    assert validate("255.255.255..255") == False


def test_missing_point():
    assert validate("255255255255") == False
    assert validate("255255255") == False
    assert validate("255255") == False
    assert validate("255") == False
    assert validate("") == False
    

def test_valid_ipv4():
    assert validate("0.0.0.0") == True
    assert validate("0.255.255.255") == True
    assert validate("255.0.255.255") == True
    assert validate("255.255.0.255") == True
    assert validate("255.255.255.0") == True
    assert validate("0.255.255.0") == True
    assert validate("255.0.0.255") == True
    assert validate("0.100.50.255") == True
    assert validate("255.1.249.255") == True
    assert validate("254.254.254.254") == True
    assert validate("255.255.255.255") == True
    
    
def test_invalid_ipv4():
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("255.255.255.2555") == False
    assert validate("2555.255.255.255") == False