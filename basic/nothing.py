# plus minus times division negation power remioin

def sum(x, y):
    return x+y


def minus(x, y):
    return x-y


def times(x, y):
    return x*y


def division(x, y):
    return x/y


def negation(x, y):
    return x//y


def remainer(x, y):
    return x % y


def power(x, y):
    return x**y


a = input("first num : ")
b = int(input("second num : "))
if type(a) | type(b) != int:
    print("pls write interger")


fun_sum = sum(a, b)
print(fun_sum)
