# functions
# "particular business logic" called as function
# set of statements also called as "function"
# functions are used to "reuse" the business logic
# "def" is the keyword, used to declare the functions

# def greet():
#     print("welcome to functions !!!")
# greet()

# no para & no return
# def addition():
#     num1 = 200
#     num2 = 100
#     res = num1 + num2
#     print(res)

# addition()

# with parameters and no return type
# def addition(num1,num2):
#     res = num1 + num2
#     print(res)

# addition(200,100)

# no parameters with return type
# def addition():
#     num1 = 200
#     num2 = 100
#     res = num1 + num2
#     return res

# x = addition()
# print(x)

# with parameters & with return type
# def addition(num1,num2):
#     res = num1 + num2
#     return res

# x = addition(200,100)
# print(x)

# 1) no para no return type
# 2) with para no return type
# 3) no para with return type
# 4) with para with return type

# Assign : square of a number

# Types of functions
# 1) predefined functions  2) user defined functions   3) anonymous functions (lamda)
# functions given by python itself called as predefined functions
# functions defined by user called as user defined functions
# functions without name called as "anonymous" functions (lambda functions)

# list1 = [10,20,30,40,50]
# print( len(list1) )

# square = lambda x:x*x
# print(square(10))

# add = lambda num1,num2:num1+num2
# print(add(200,100))



# def db_conn(username,password):
#     res = "Success" if username == "ashokit" and password == "ashokit@123" else "Fail"
#     print(res)

#db_conn("ashokit","ashokit@123")
#db_conn(password="ashokit@123",username="ashokit") keyword arguments


# def test_func(name="AshokIT"):
#     print(name)

# test_func() # Default arguments
# test_func("AshokIT - DataScience")


def test_func(*num):        # variable length arguments
    print(type(num))
    print(sum(num))

test_func(10,20,30,40,50)

