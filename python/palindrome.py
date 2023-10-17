# alphaNumeric = "0123456789abcdefghijklmnopqrstuvwxyz";

# def palindrome(inputWord, onlyCheckAlphaNumeric = False):
#     word = str(inputWord).lower()
#     newWord = ""
#     if onlyCheckAlphaNumeric:
#         for index in range(len(word)):
#             if word[index] in alphaNumeric:
#                 newWord += word[index]
#         word = newWord

#     for index in range(len(word)):

#         if word[index] != word[(len(word)-1-index)]:
#             return False
        
    
#     return True



def palindrome_recursive(input_word):
    firstString = ""
    secondString = ""
    if len(input_word) % 2 == 0:
        firstString = input_word[0:len(input_word)//2]
        secondString = input_word[len(input_word)//2:][::-1]
    else:
        firstString = input_word[0:len(input_word)//2]
        secondString = input_word[len(input_word)//2 + 1:][::-1] 

    if firstString == secondString:
        return True
    return False

print(palindrome_recursive("civic"))