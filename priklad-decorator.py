def upper(func):
    def wrapper():
        result_from_func = func()
        return result_from_func.upper()
    return wrapper


@upper
def say_hello():
    return "Hello"


if __name__ == "__main__":
    print(say_hello())