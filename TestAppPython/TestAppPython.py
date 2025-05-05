from SkullFourierFunc import SkullFourierFunc

func = SkullFourierFunc()

with open("coords.txt", "w") as file:
    for i in range(0, 10000):
        t = i / 10000.0
        c = func.calc_normal(t)
        if c is None:
            continue
        file.write(f"{c.x}\t{c.y}\n")
