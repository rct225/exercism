def is_isogram(string):
    if string == "":
        return True

    s = list(filter(lambda c: c.isalpha(), string.lower()))
    return len(s) == len(set(s)) if s else False
