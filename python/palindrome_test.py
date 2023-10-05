from palindrome import palindrome
def test_palindrome_racecar():
    assert palindrome('racecar') == True
    assert palindrome('Noon') == True
    assert palindrome('ciVic') == True
    assert palindrome('nice') == False
    assert palindrome('434') == True
    assert palindrome('123') == False
    assert palindrome('bomb') == False
    assert palindrome('Sore was I ere I saw Eros.',True) == True
    assert palindrome('A man, a plan, a canal -- Panama',True) == True