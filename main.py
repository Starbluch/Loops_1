#lessons 1.2 hm
def cals():
    factor_1 = 0
    while (factor_1 < 10):
        factor_1 += 1
        factor_2 = 0
        while (factor_2 < 10):
            factor_2 += 1
            print(f"{factor_1}{"*"}{factor_2}={factor_1 * factor_2}{" |"}", end=" ")
        print(f"\n{"." * 100}")


cals()