# def say_hello():
#     print("hello")

# say_hello -> if there is no () , it would't be implemeted

# def say_hello(who):  # i must declare the data which is "who"
#     print("hello", who)

# say_hello("hi")


# def plus(a, b):
#     print(a + b)

# # def minus(a, b):


# def minus(a, b=0):  # b=0 is default value so if i missed to declare of the data of b , 0 will be inputed
#     print(a - b)


# plus(1, 5)
# minus(2, 5)

# def say_hello(name="anoymous"):
#     print("hello", name)

# say_hello()

# print vs ruturn

# def p_plus(a, b):
#     print(a + b)


# def r_plus(a, b):
#     return a + b


# p_result = p_plus(2, 3)
# r_result = r_plus(2, 3)

# print(p_result, r_result) # -> p_result : none , r_result : 5

# positional arguments : it depends on the positon
# ex) def plus(a, b) :
#     return a + b
# result = plus(2, 3)
# print(result)
# so 2,3 became a,b

# keyword arguments : it depedns on the name ,
# ex) def plus(a, b) :
#     return a + b
# result = plus(b=3 , a=1)
# print(result)
# so postion doesn't matter in this case

def say_hello(name, age):
    return f'hi {name} u r {age} yo'


hello = say_hello("nice", "12")  # positional arguments
hello = say_hello(age="12", name="nice")  # keyword arguments
print(hello)
