from tema_4.GaussSeidelRareSystem import GaussSeidelRareSystem
from tema_4.RareMatrix import RareMatrix

epsilon = 10 ** -8

if __name__ == '__main__':
    # print("-------------------------------------------")
    # print("Exemplu laborator")
    # a_test = GaussSeidelRareSystem("a_test.txt", "b_test.txt", 10000, epsilon)
    #
    # print(a_test.a)
    # print(a_test.b)
    # print(a_test.solve())

    print("-------------------------------------------")
    print("Exemplu 1")

    s_1 = GaussSeidelRareSystem("./surse/a_1.txt", "./surse/b_1.txt", 10000, epsilon)
    print(s_1.solve())
    print("Norma: ", s_1.norm)
    print("Iteratii: ", s_1.gauss_seidel_iterations)

    print("-------------------------------------------")
    print("Exemplu 2")

    s_2 = GaussSeidelRareSystem("./surse/a_2.txt", "./surse/b_2.txt", 10000, epsilon)
    print(s_2.solve())
    print("Norma: ", s_2.norm)
    print("Iteratii: ", s_2.gauss_seidel_iterations)

    print("-------------------------------------------")
    print("Exemplu 3")

    s_3 = GaussSeidelRareSystem("./surse/a_3.txt", "./surse/b_3.txt", 10000, epsilon)
    print(s_3.solve())
    print("Norma: ", s_3.norm)
    print("Iteratii: ", s_3.gauss_seidel_iterations)

    print("-------------------------------------------")
    print("Exemplu 4")

    s_4 = GaussSeidelRareSystem("./surse/a_4.txt", "./surse/b_4.txt", 10000, epsilon)
    print(s_4.solve())
    print("Norma: ", s_4.norm)
    print("Iteratii: ", s_4.gauss_seidel_iterations)

    print("-------------------------------------------")
    print("Exemplu 5")

    try:
        s_5 = GaussSeidelRareSystem("./surse/a_5.txt", "./surse/b_5.txt", 10000, epsilon)
        print(s_5.solve())
        print("Norma: ", s_5.norm)
        print("Iteratii: ", s_5.gauss_seidel_iterations)
    except Exception as e:
        print(e)

    print("-------------------------------------------")
    print("Bonus")

    a = RareMatrix("./surse/a.txt", epsilon)
    b = RareMatrix("./surse/b.txt", epsilon)
    aplusb = RareMatrix("./surse/aplusb.txt", epsilon)
    print(aplusb.equals(a.sum(b)))
