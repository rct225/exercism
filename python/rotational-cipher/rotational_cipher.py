def rotate(plain, rot_key):
    rot_key = rot_key % 26
    alphabet = [chr(97 + i) for i in range(0, 26)]
    shift_alphabet = alphabet[rot_key:] + alphabet[:rot_key]
    rotated = ''
    for c in plain:
        if c.isupper():
            rotated += shift_alphabet[ord(c.lower()) - 97].upper()
        elif c.isalpha():
            rotated += shift_alphabet[ord(c) - 97]
        else:
            rotated += c
    return rotated
