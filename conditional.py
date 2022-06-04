# def plus(a,b):
#     if type(b) is int or type(b) is float:
#         return a+b
#     else :
#         return None

def age_check(age):
    print(f'your {age}')
    if age < 18:
        print("u can not drink ")
    elif age == 18:
        print("u r new to this")
    elif age > 20 and age < 25:
        print("u r still young")
    else:
        print("enjoy your drink")


age_check(22)
