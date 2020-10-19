n = 158
plus_grand = 0
x1, y1, z1 = 0, 0, 0


def y_z(x): return (n - x)/3, 2*(n - x)/3


def res(x, prec):
    global n, plus_grand, x1, y1, z1
    while x <= n:
        y, z = y_z(x)
        v = x*y*z

        if v > plus_grand:
            plus_grand = v
            x1, y1, z1 = x, y, z

        x += prec

    return f"x = {x1}, y = {y1}, z = {z1} \nV = {plus_grand}"


print(res(0, 0.001))
