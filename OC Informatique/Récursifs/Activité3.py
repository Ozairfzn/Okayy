def pile_ou_face(n):
    if n == 1:
        return ["P", "F"]

    sous_liste = pile_ou_face(n-1)
    liste_deb_P = ["P" + x for x in sous_liste]
    liste_deb_F = ["F" + x for x in sous_liste]

    liste = liste_deb_P + liste_deb_F
    return liste


liste_usl = []


def une_seule_liste(liste):
    global liste_usl
    for i in liste:
        if isinstance(i, int):
            liste_usl.append(i)
        elif isinstance(i, list):
            une_seule_liste(i)
    return liste_usl
