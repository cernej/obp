def generuj_cisla(n):
    result = []
    for i in range(n):
        x = {"i": i}
        result.append(x)
    return result


def generuj_cisla2(n):
    for i in range(n):
        yield {"i": i}


for i in generuj_cisla2(10000000):
    print(i)