alphaNumeric = "0123456789abcdefghijklmnopqrstuvwxyz";

def palindrome(inputWord, onlyCheckAlphaNumeric = False):
    word = str(inputWord).lower()
    newWord = ""
    if onlyCheckAlphaNumeric:
        for index in range(len(word)):
            if word[index] in alphaNumeric:
                newWord += word[index]
        word = newWord

    for index in range(len(word)):

        if word[index] != word[(len(word)-1-index)]:
            return False
        
    
    return True



