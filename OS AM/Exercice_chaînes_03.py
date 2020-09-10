def initiales(txt):
    ini = ""
    for i in txt:
        if i.isupper():
            ini+=i
    return ini
        
print(initiales("Ozair Faizan"))