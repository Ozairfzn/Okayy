def palin(mot):
    mot1 = ""
    for i in mot:
        mot1 = i + mot1
    return mot == mot1
