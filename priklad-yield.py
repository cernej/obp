def generuj_cisla(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


def generuj_cisla2(n):
    for i in range(n):
        yield i


for i in generuj_cisla(1000000):
    print(i)