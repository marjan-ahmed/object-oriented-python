# class Car:
#     def __init__(self, brand: str, model: int):
#         self.__brand = brand
#         self.model = model
        
#     def show_name(self):
#         return f"Your car is {self.__brand} {self.model}"
    
#     def get_brand(self):
#         return self.__brand + "!"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
# car1 = Car("Honda", "Civic")
# print(car1.show_name())
# # print(car1.get_brand())

# class ElectricCar(Car):
#     def __init__(self, brand: str, model: str, battery_size: int):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#         return "Electric Charge"
        
# tesla = ElectricCar("Tesla", "S32", 100)
# # print(tesla.show_name())
# print(tesla.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())



class Numbers:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def add(self):
        return self.v1 + self.v2
    
    def __add__(self, x):
        return (self.v1 + self.v2) + (x.v1 + x.v2)
    
    def __str__(self):
        return f"Numbers({self.v1}, {self.v2})"


n1 = Numbers(1,1) # 2
print(n1)
n2 = Numbers(1,2) # 3
print(str(n2))
print(n1 + n2)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

p = Person("Marjan")
print(p)  # 👉 Output: My name is Marjan





class Car:
    def __init__(self, speed):
        self.speed = speed
        
    def __gt__(self, other):
        # compare speeds
        return self.speed > other.speed
        
    def __str__(self):
        return f"Car(speed={self.speed})"

# Create two cars
car1 = Car(120)
car2 = Car(130)

# Use > operator, which calls car1.__gt__(car2)
if car1 > car2:
    print("Car1 is faster")
else:
    print("Car2 is faster")

print(car1)
print(car2)



# Create a Laptop class that checks equality == based on brand and RAM.

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        
    def __eq__(self, x):
        if (self.brand == x.brand) & (self.ram == x.ram):
            print("They both are same")
            return True
        else:
            print("They both are not same")
            return False
    
    def __repr__(self):
        return f"Laptop(ram={self.ram}, brand={self.brand})"
    
lp1 = Laptop("lenovo", 8)
lp2 = Laptop("lenovo", 8)
print(lp1 == lp2)


# Create a Temperature class that subtracts temperatures using - (in Celsius).

class Temp:
    def __init__(self, temp):
        self.temp = temp
        
    def __sub__(self, x):
        return self.temp - x.temp
    
    def __str__(self):
        return f"Your given temperature is {self.temp}"
    
temp1 = Temp(10)
temp2 = Temp(90)
print(temp1 - temp2)


# Make a StudentGroup class where len() returns the number of students using __len__.

# class StudentGroup:
#     count = 0
#     def __init__(self, *std):
#         self.std = std
    
#     def __len__(self):
#         return len(self.std)
        
#     def __repr__(self):
#         return f"Your students are {list(self.std)}"
    
# studentGroup = StudentGroup(2,4,4,5,66,2)
# print(studentGroup)
# print(len(studentGroup))

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius  # Private variable
#     @property
#     def radius(self):
#         return self.__radius  # Getter
    


# # Usage
# c = Circle(5)

class Doubler:
    def __call__(self, x):
        return x * 2

num1 = Doubler()
print(num1(5))  