class Matrice:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        ligne = f"{self.a}   {self.b}\n{self.c}   {self.d}"
        return ligne

    def trace(self):
        return self.a + self.d

    def determinant(self):
        return self.a*self.d - self.b*self.c

    def produit_scalaire(self, k):
        ps = Matrice(self.a*k, self.b*k, self.c*k, self.d*k)
        return ps

    def inverse(self):
        if self.determinant() == 0:
            return None
        m1 = Matrice(self.d, -self.b, -self.c, self.a)
        return m1.produit_scalaire(1/self.determinant())

    def __add__(self, other):
        m = Matrice(self.a+other.a, self.b+other.b,
                    self.c+other.c, self.d+other.d)
        return m

    def __mul__(self, other):
        m = Matrice(self.a*other.a + self.b*other.c, self.a*other.b + self.b*other.d,
                    self.c*other.a + self.d*other.c, self.c*other.b + self.d*other.d)
        return m
