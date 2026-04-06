# class - collection of variables and functions called as class
# "class" is the keyword, used to declare the classes in python
# oops -- 1) encapsulation  2) abstraction 3) inheritance  4) polymorphism

# Example-1
# class Student:
#     pass

# s1 = Student()
# s2 = Student()

# Example - 2
# class Student:
#      def __init__(self):
#           self.name = "Student1"
#           self.age = 20
# s1 = Student()
# print(s1.name)
# print(s1.age)

# Example - 3
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("Std1",20)
# print(s1.name)
# print(s1.age)

# s2 = Student("Std2",22)
# print(s2.name)
# print(s2.age)

# Example - 4
# class Test:
#     def __init__(abc,name):
#         abc.name = name

# t1 = Test("Hello")
# print(t1.name)

# Example - 5
# class Student:
#     def __init__(self):
#         self.name = "AshokIT"
#     def display(self):
#         print(self.name)
# s1 = Student()
# s1.display()

# Example-6
# class Demo:
#     def __init__(self):
#         self.x = 10 # instance variable

# obj1 = Demo()
# obj1.x = 100
# print(obj1.x)
# obj2 = Demo()
# print(obj2.x)

# Example-7
# class Demo:
#     x = 100 # class variable

# obj1 = Demo()
# obj2 = Demo()

# Demo.x = 200
# print(obj1.x)
# print(obj2.x)

#Example-8
# class Demo:
#     x = 100 # class variable

# obj1 = Demo()
# obj2 = Demo()
# Demo.x = 200
# obj1.x = 1000 # instance variable created inside object (obj1)

# print(obj1.x) #1000
# print(obj2.x) #100

# Example-9
# class Demo:
#     def square1(self):
#         num1 = 100
#         res = num1 * num1
#         print(res)
#     def square2(self,num1):
#         res = num1 * num1
#         print(res)
#     def square3(self):
#         num1 = 100
#         res = num1 * num1
#         return res
#     def square4(self,num1):
#         return num1 * num1

# obj = Demo()
# obj.square1()
# obj.square2(100)
# res = obj.square3()
# print(res)
# res1 = obj.square4(100)
# print(res1)


#Example-10
# class Demo:
#     x = 100

#     @classmethod
#     def test_method(cls):
#         print(cls.x)

# Demo.test_method()

# obj = Demo()
# obj.test_method()


#Example-11
# class Demo:
#     @staticmethod
#     def validation(email):
#         return "@" in email

# print( Demo.validation("info@ashokit.in") )

# Example-12
# class Parent:
#     def __init__(self):
#         self.x = 200

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.y = 100

# obj = Child()
# print(obj.y)
# print(obj.x)


#Example-13
# class Parent:
#     def test_func1(self):
#         print("Hello, Parent")

# class Child(Parent):
#     def test_func2(self):
#         print("Hello,Child")

# class Subchild(Child):
#     def test_func3(self):
#         print("Hello,Subchild")

# obj = Subchild()
# obj.test_func1()
# obj.test_func2()
# obj.test_func3()

# Example - 14
# method overriding
# class Parent():
#     def db_conn(self):
#         return "mysql conn soon"
# class Child(Parent):
#     def db_conn(self):
#         return "mongodb conn soon"
    
# obj = Child()
# res = obj.db_conn()
# print(res)

# Example - 15
# class Parent():
#     def db_conn(self):
#         return "mongodb conn soon...!"
    
# class Child(Parent):
#     def test_func(self):
#         return super().db_conn()

# obj = Child()
# res = obj.test_func()
# print(res)

# Example - 16
# Encapsulation
# class Class1:
#     def __init__(self):
#         self.__x = 100  # private

# obj = Class1()
# # obj.__x # unable to access private variable
# print( obj._Class1__x ) # we are able to access private variable

# Example - 17 
# Polymorphism (Behaves like many)
# class Demo():
#     def addn(self,param1,param2):
#         print(param1 + param2)

# obj = Demo()
# obj.addn(200,100) # addn -- adding
# obj.addn("Hello","Welcome") # addn -- concatination

# Example - 18
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#        self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rect(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return 2 * self.width * self.height

# c = Circle(10)
# res1 = c.area()
# print(res1)

# r = Rect(200,100)
# res2 = r.area()
# print(res2)

# Example - 19 (Dunder)
# class Demo():
#     def __str__(self):
#         return "Hello"
    

# obj = Demo()
# print(obj)

# Example - 20
class Test1():
    def show(self):
        print("Test1")
class Test2():
    def show(self):
        print("Test2")
class Test3(Test2,Test1):
    pass

obj = Test3()
obj.show()
