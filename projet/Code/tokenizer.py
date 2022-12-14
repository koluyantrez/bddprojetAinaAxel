def tokenize(sentence: str) -> list:
    # Return a list containing all the tokens of a sentence
    wordList = []
    length = len(sentence)
    word = ""
    current = ""
    for i in range(length):
        current = sentence[i]
        if current == ' ':
            __addWord(word,wordList)
            word = ""
        if not current.isalpha() and not current.isdigit():
            __addWord(word,wordList)
            __addWord(current,wordList)
            word = ""
        else:
            word += current
        
    __addWord(word,wordList)
    return wordList


def __addWord(word: str, liste: list):
    if len(word) != 0 and word != ' ':
        liste.append(word)

def toString(tokens: list):
    if (len(tokens) == 0):
        raise Exception("The list size must be greater than 0")
    res = ""
    for i in range(len(tokens)):
        res += tokens[i]
    
    return res