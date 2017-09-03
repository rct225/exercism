def is_pangram(string):
    s = list(filter(lambda ch: ch.isalpha(), string.lower()))
    return 26 == len(set(s)) if s else False
