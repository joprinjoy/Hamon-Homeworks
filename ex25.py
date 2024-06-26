
#this program won't run itself
""" import ex25
>>> sentence = "All good things comes to those who waits"
>>> words = ex25.break_words(sentence)
>>> words
 """
def break_words(stuff):
    """This function will break up words for us 
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prnint last word after poping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    word = break_words(sentence)
    return sort_words(word)

def print_first_and_last(sentence):
    """Print first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words and then prints first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
