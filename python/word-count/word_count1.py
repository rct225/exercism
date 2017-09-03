import re

def word_count(string):
    string = re.sub(r'[^a-zA-Z0-9]',' ', string.lower())
    words = string.split();
    word_freq = {};
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq
