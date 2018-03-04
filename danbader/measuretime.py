import timeit


def t(x):
    e = 0
    for i in range(int(x) * 100):
        print(e)
        e += 1
    return e


a = 21
b = 234

a, b = b, a

if __name__ == '__main__':
    from timeit import Timer

    print(t(143))
    t = Timer(lambda: t(15))
    print(f"execution for 20 cycles took {t.timeit(number=20)}")
