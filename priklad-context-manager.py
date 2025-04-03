import time
from contextlib import contextmanager


class MyContext:
    def __enter__(self):
        print("Start")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"End: {exc_type}, {exc_val}, {exc_tb}")
        return True


# with MyContext() as ctx:
#     print("Run")
#     raise ValueError("Nejaka chyba")


class Timing():
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Trvalo {time.time() - self.start:.2f}s")


@contextmanager
def timing():
    start = time.time()
    yield
    print(f"Trvalo {time.time() - start:.2f}s")


# with timing() as ctx:
#     for i in range(1000000):
#         pass


with timing(), MyContext() as ctx:
        print("Run")
        raise ValueError("aaa")