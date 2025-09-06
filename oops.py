# Assignment 1: Design Your Own Class!

class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Encapsulated attribute

    def call(self, number):
        if self.__battery_level > 0:
            print(f"{self.brand} {self.model} is calling {number}...")
            self.__battery_level -= 1
        else:
            print("Battery too low to make a call.")

    def charge(self, amount):
        self.__battery_level += amount
        print(f"{self.brand} {self.model} charged to {self.__battery_level}%.")

    def get_battery_level(self):
        return self.__battery_level

# Inheritance example
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_level, strap_type):
        super().__init__(brand, model, battery_level)
        self.strap_type = strap_type

    def show_time(self):
        print(f"{self.brand} {self.model} shows the current time.")

# Demonstration
phone = Smartphone("Samsung", "Galaxy S21", 10)
watch = Smartwatch("Apple", "Watch Series 7", 5, "Silicone")

phone.call("123-456-7890")
phone.charge(5)
print("Phone battery:", phone.get_battery_level())

watch.show_time()
watch.call("987-654-3210")
print("Watch battery:", watch.get_battery_level())

print("\n--- Polymorphism Challenge ---")

# Activity 2: Polymorphism Challenge!

class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road [car]")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky [plane]")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water [boat]")

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()