def calculator(functions):
    functions = ["add", "minus", "times",
                 "division", "negation", "power", "remioin"]
    return functions


print("1 : plus || 2 : minus || 3: times || 4: division || 5: negation || 6 : power || 7: remioin")
n = int(input("which function do u want to use ? : ")) - 1
# print(calculator([n]))
calculator()

# for i in calculator([]):
#     print(i)
