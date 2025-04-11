class Iter:

    def __init__(self, max=10):
        self.cnt = 0
        self.max = max

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cnt < self.max:
            val = self.cnt
            self.cnt += 1
            return val
        else:
            raise StopIteration


class IterYield:

    def __init__(self, max=10):
        self.max = max

    def __iter__(self):
        for i in range(self.max):
            yield i


# iter1 = Iter(5)
# iter2 = IterYield(5)

# print(f"Iter: {iter1}")
# print(f"IterYield: {iter2}")

# print(f"Iter: {[i for i in iter1]}")
# print(f"IterYield: {[i for i in iter2]}")


# ls = [1, 2, 3, 4, 5]
# for i in ls:
#     print(i)

# it1 = iter(ls)
# it2 = iter(ls)
# print(it1)
# print(it2)
# print(next(it1))
# print(next(it1))
# print(next(it2))
# print(next(it1))
# print(next(it2))
# print(next(it2))

class FileWords:
    def __init__(self, filename):
        self.file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        buff = ""
        while True:
            char = self.file.read(1)
            if not char:
                raise StopIteration
            if char == " ":
                break
            buff += char
        return buff

f = FileWords("selenium.txt")
for x in f:
    print(x)