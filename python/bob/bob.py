def hey(string):
    string = "".join(string.split())
    if string == '':
        return 'Fine. Be that way!'

    if string.isupper():
        return 'Whoa, chill out!'

    if string[-1] == '?':
        return 'Sure.'

    return 'Whatever.'
