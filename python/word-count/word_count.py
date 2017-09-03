import re

def word_count(string):
    string = re.sub(r'[^a-zA-Z0-9]',' ', string.lower())
    words = string.split();
    word_freq = {word: words.count(word) for word in set(words)};

    return word_freq
