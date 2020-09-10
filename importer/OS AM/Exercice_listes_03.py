crypt = "sd?ip!sov!suos!ros?rt!nu!a!y!li"
L = [i for i in crypt]


def sub(L, s1, s2):
    for i in range(len(L)):
        if L[i] == s1:
            L[i] = s2
    return L


def inv(L):
    L2 = [L[len(L)-1 - i] for i in range(len(L))]
    return L2


L = (inv(L))
L = (sub(L, "!", " "))
L = (sub(L, "?", "e"))
txt = "".join(L)

print(txt)