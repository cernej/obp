def fce(*args, **kwargs):
    print(args)
    print(kwargs)


fce(1, 2, 3, a=1, b=2, c=3, d=4, e=5)