from data import DICTIONARY, LETTER_SCORES

def load_words(myfile):
    """Load dictionary into a list and return list"""
    wordlist = []
    myfile = open('dictionary.txt', 'r')
    
    for i in myfile:
        wordlist.append(i)       
    return wordlist

def calc_word_value(wordlist, LETTER_SCORES):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    totalscore = 0
    wordscores = {}
    
    for word in wordlist:
        for letter in word:
            if letter.upper() in LETTER_SCORES:
                score = LETTER_SCORES.get(letter.upper(), 0)
                totalscore += score
            else:   
                wordscores[word.strip()] = totalscore
                totalscore = 0
    return wordscores

def max_word_value(wordscores):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(wordscores.values())

if __name__ == "__main__":
    WordList = load_words(DICTIONARY)
    WordScores = calc_word_value(WordList, LETTER_SCORES)
    MaxWordVal = max_word_value(WordScores)
    
    print('The Max Word Value found in the list:', MaxWordVal)
    
    pass # run unittests to validate
    
