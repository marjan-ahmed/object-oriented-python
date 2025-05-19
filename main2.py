# class Vehicle:
#     def __init__(self, engine:int):
#         self.__engine = engine
        
#     @property
#     def engine(self):
#         return self.__engine
    
#     @engine.setter
#     def engine(self, new_engine):
#         self.__engine = new_engine 
    
#     @staticmethod
#     def move():
#         return "Vehicle is going to start"
    
# class Car(Vehicle):
#     def move():
#         return "Car is starting..."
    
    
# # Create object
# vehicle = Vehicle(100)
# print(vehicle.move())        # ✅ Output: Vehicle is going to start
# print(vehicle.engine)        # ✅ Output: 100

# vehicle.engine = 10         # ✅ Using property setter
# print(vehicle.engine)        # ✅ Output: 2
# p = Vehicle().engine 
# print(p)

# class Circle:
#     def __init__(self, radius: int):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# c1 = Circle(5)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     def __init__(self, role: str, department: str, salary: int):
#         self.role = role
#         self.department = department
#         self.salary = salary
    
#     def show_details(self):
#         return f"Employee Role: {self.role}, Department: {self.department}, Salary: {self.salary}"
        
# e = Employee("Software developer", "software engineer", 3000)
# print(e.show_details())

# class Engineer(Employee):
#     def __init__(self, name, age):
#         super().__init__("Engineer", "IT", 55400)
#         self.name = name
#         self.age = age
        
# eng = Engineer("Elon Musk", 40)
# print(eng.show_details())


# class Order:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __gt__(self, k):
    

def login_required(func):
    def wrapper(*args, **kwargs):
        print("Welcome to login page")
        if args or kwargs:  # Checks if user passed some login info
            print("User can join")
            return func(*args, **kwargs)  # ✅ Actually call the function
        else:
            print("User can't join")
            return None
    return wrapper

@login_required
def user(psd, username=None):
    return f"Logged in as {username}"

print(user('ahmed'))  
