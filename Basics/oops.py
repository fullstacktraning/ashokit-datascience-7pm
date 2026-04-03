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








