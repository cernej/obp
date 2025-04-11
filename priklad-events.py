class Event:
    def __init__(self):
        self.handlers = []

    def register(self, handler):
        self.handlers.append(handler)

    def unregister(self, handler):
        self.handlers.remove(handler)
    
    def __call__(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)


def vypis_jmeno(jmeno):
    print(f"Jmeno: {jmeno}")


class Osoba:
    def __init__(self):
        self.jmeno = None

    def __call__(self, jmeno):
        self.jmeno = jmeno
        print(f'Osoba: {self.jmeno}')


osoba = Osoba()
print(osoba.jmeno)
new_user_registered = Event()
new_user_registered.register(vypis_jmeno)
new_user_registered.register(osoba)

new_user_registered("Jan Novák")
print(osoba.jmeno)