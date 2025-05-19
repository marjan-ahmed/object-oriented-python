Coding Task — Student Management System
---------------------------------------

A simple school management system where you manage **Teachers** and **Students** using **Object-Oriented Programming (OOP)** principles.

### 🔹 Step 1: Encapsulation (Data Hiding)

*   Create a class Person
    
*   Add the following data members:
    
    *   \_name (protected)
        
    *   \_\_age (private)
        
*   Create methods:
    
    *   get\_age() — to access age
        
    *   set\_age() — to safely update age
        

### 🔹 Step 2: Inheritance

*   Create two classes that inherit from Person:
    
    *   Student
        
    *   Teacher
        
*   Add extra fields:
    
    *   **Student**: student\_id, grade
        
    *   **Teacher**: subject, salary
        

### 🔹 Step 3: Abstraction

*   Use the ABC module
    
*   Create an abstract class SchoolMember
    
*   Add abstract method show\_details()
    
*   Inherit Student and Teacher from SchoolMember
    

### 🔹 Step 4: Polymorphism

*   Define show\_details() method in both Student and Teacher
    
*   Store both objects in a loop and call show\_details() on each — this demonstrates **polymorphism**
    

### 🔧 Code Requirements

*   Use `___init__` constructor in every class
    
*   Use `super()` to reuse the constructor of the base class
    
*   Use `__str__()` in at least one class
    
*   Add a custom method `greet()` in both Student and Teacher to show **method overriding**
