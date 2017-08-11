def break_words(sentence):
    """ This function will break up words for us. """
    words = sentence.split(" ")
    return words

def sort_words(words):
    """ returns sorted words. """
    return sorted(words)

def print_first_word(words):
    """ prints the first word after popping it off """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ prints the last word after popping it off """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """ takes a sentence and returns the sorted words """
    words = break_words(sentence)
    return sort_words(words)

