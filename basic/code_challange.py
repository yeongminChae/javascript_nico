li = ["add", "minus", "times", "division", "negation", "power", "remain"]
li2 = []
print("1 : plus || 2 : minus || 3: times || 4: division || 5: negation || 6 : power || 7: remain")


def input_function():
    n = int(input("which function do u want to use ? : "))
    if 1 <= n < 8:
        a = li2.append(n-1)
        return a
    else:
        print("wrong")


print(li2)


def detective_function():
    return


# def choose_num():
#     print(n)
#     else:
#         return return_method


def return_method():
    print("hi")
