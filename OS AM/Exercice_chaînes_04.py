def maj_min(txt):
    inverse = ""
    for i in txt:
        if i.isupper():
            inverse += i.lower()
        else:
            inverse += i.capitalize()
    return inverse
