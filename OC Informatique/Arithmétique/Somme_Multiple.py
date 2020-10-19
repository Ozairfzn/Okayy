def multiple(Multiple, borne_inf, borne_sup):
    m = borne_inf//Multiple
    n = borne_sup//Multiple

    resa = Multiple*(m*(m+1)/2)
    resb = Multiple*(n*(n+1)/2)

    return int(resb-resa)
