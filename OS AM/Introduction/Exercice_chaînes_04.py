def maj_min(txt):
    inverse = ""
    for i in txt:
        if i.isupper():
            inverse += i.lower()
        elif i.islower():
            inverse += i.capitalize()
        else:
            inverse += i
    return inverse


def maj_min_2(txt):
    inverse = ""
    for i in txt:
        if "A" <= i <= "Z":
            inverse += chr(ord(i)+32)
        elif "a" <= i <= "z":
            inverse += chr(ord(i)-32)
        else:
            inverse += i
    return inverse


def maj_min_3(txt):
    return txt.swapcase()
