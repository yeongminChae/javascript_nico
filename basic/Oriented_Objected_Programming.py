# class = blueprint
# instance = product which is made by blueprint(= class)

# class
# class Car():
#     wheels = 4
#     doors = 4
#     windows = 4
#     seat = 4

# # instance
# porche = Car()
# porche.color = "Red"
# print(porche.color)

# ferrari = Car()
# ferrari.color = "Yellow"

# method
# method is the function which is inside of class

class Car():
    # wheels = 4
    # doors = 4
    # windows = 4
    # seat = 4

    # def start(self):  # first argument of method is instance which is calling the method
    #     print("I started")

    def __init__(self, *args, **kwargs):
        # print(kwargs)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seat = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    # override 재정의

    def __str__(self):
        return f"Car with {self.wheels} wheels "


porche = Car(color="Green", price="$50")
# print(dir(Car)) # dir shows to us for all of the strings
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)
