def compteur(txt):
    mots = 0
    for i in txt:
        if i == " " or i == ".":
            mots+=1
    return mots
