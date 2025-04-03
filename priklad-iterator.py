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


iter1 = Iter(5)
iter2 = IterYield(5)

print(f"Iter: {iter1}")
print(f"IterYield: {iter2}")

print(f"Iter: {[i for i in iter1]}")
print(f"IterYield: {[i for i in iter2]}")