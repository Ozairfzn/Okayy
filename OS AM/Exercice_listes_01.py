def suppr_min(L):
    L.remove(min(L))
    return L


def suppr_min_2(L):
    index = 0
    mini = L[0]
    for i in range(len(L)):
        if mini > L[i]:
            mini = L[i]
            index = i
    L.pop(index)
    return L
