# 1. *args

# def plus(a, b):
#     return a + b

# plus(1, 2, 3, 4, 5, 6) -> plus() takes 2 positional arguments but 6 were given

# def plus(*args):
#     print(args)
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(plus(1, 2, 3, 4, 5)) -> positional argument

# def plus(a, b):
#     return a + b


# plus(hi=True, hello=True, bye=True) -> plus() got an unexpected keyword argument 'hi'


# def plus(a, b, **kwargs):
#     print(kwargs)
#     return a + b


# plus(1, 2, hi=True, hello=True, bye=True) -> keyword arguments
