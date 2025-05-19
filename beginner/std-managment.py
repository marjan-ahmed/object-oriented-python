from abc import ABC, abstractmethod

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self.__age = age
    
    @property    
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, new_age: int):
        if isinstance(new_age, int):  
            self.__age = new_age
        else:
            print("Invalid age. Please enter a number.")
            

class SchoolMember(ABC):
    @abstractmethod
    def show_details(self):
        pass
        
        
class Student(Person, SchoolMember):
    def __init__(self, student_id: int, grade: int):
        super().__init__("Marjan", 16)
        self.std_id = student_id
        self.grade = grade
    
    def show_details(self):
        return f"Student ID: {self.std_id}, Grade: {self.grade}"
    
    @staticmethod
    def greet():
        return "Hey, Welcome to get student detail!"
    
    def __str__(self):
        return f"Student({self.std_id}, {self.grade})"
    
class Teacher(Person, SchoolMember):
    def __init__(self, subject: str, salary: int):
        super().__init__("Jawwad", 27)
        self.subject = subject
        self.salary = salary
        
    def show_details(self):
        return f"Teacher Subject: {self.subject}, Salary: {self.salary}"

    @staticmethod
    def greet():
        return "Hey, Welcome to get teacher detail!"

    def __str__(self):
        return f"Teacher({self.subject}, {self.salary})" 
        
        
s1 = Student(1001, 9)
t1 = Teacher("english", 5000) # in dollars

print(s1.get_age)
s1.set_age = 17
print(s1.set_age)

for info in s1,t1:
    print(info, "\n")
    print(info.show_details())