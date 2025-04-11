class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Alice")
p2 = Person("Bob")
print(p1.__dict__)

setattr(p1, "age", 30)
print(p1.__dict__)

print(p1.age)

delattr(p1, "name")

setattr(Person, "version", 1.0)
print(Person.version)
print(p1.version)
print(p2.version)

print(dir(p1))