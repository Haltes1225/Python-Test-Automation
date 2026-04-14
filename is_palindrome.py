
def is_palindrome(word: str):

    type_word = type(word)  
    if not type_word is str:
        raise TypeError(f"word must be str type, is {type_word}") 

    if len(word) == 0:
        #Empty word is a palindrome
        return True
    
    #Take floor of half of the word length (to account for words of both even and uneven length) 
    len_word = len(word)
    n = math.floor(len_word/2)
    #Traverse tr string from beginning and end and check if the characters are the same 
    for i in range(n):
        if word[i] != word[len_word - i - 1]:
            return False
        
    return True

