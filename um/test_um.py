from um import count

def test_um():
    assert count('um') == 1
    assert count('um, I mean the quick brown dog jumps over the lazy fox, um.') == 2
    assert count('The quick brown fox um jumps over the lazy dog. Um, I mean the quick brown dog jumps over the lazy fox, um.') == 3
    
def test_um_zero():
    assert count('') == 0
    assert count('The quick brown fox jumps over the lazy dog.') == 0
    assert count('The quick brown fox jumps over the lazy dog. I mean the quick brown dog jumps over the lazy fox.') == 0
    assert count('u.m') == 0
    
def test_um_case():
    assert count('UM') == 1
    assert count('uM, I mean the quick brown dog jumps over the lazy fox, um.') == 2
    assert count('The quick brown fox um jumps over the lazy dog. uM, I mean the quick brown dog jumps over the lazy fox, UM.') == 3
    assert count('uM') == 1