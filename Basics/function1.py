
# f = lambda a = 10 : a + 10
# print(f())
# print(f(20))


# filter() - used to apply conditions
# print( list( filter( lambda num: num%2 == 0 , [1,2,3,4,5] ) ) )


# map() - used to manipulate all list items
# print( list( map(lambda x:x*x,[1,2,3,4]) ) )

# addition = lambda param1, param2 : param1 + param2
# print(addition(200,100))

# def test_func(param1 = []):
#     param1.append(1)
#     return param1

# print( test_func() )
# print( test_func() )
# print( test_func() )


# balance = 1000 # global

# def widthdraw(amount):
#     global balance
#     if balance>=amount:
#         balance-=amount
#         return balance
#     return "Insufficient Balance"

# res1 = widthdraw(200)
# print(res1)

# res2 = widthdraw(10000)
# print(res2)



# LEGB Rule # L - Local E - Enclosing G - Global B - Built-in
# name = "HPSchool" # global
# def student():
#     #name = "STD1"  # enclosing
#     def info():
#         #name = "CLASS X" # local
#         print(name)
#     info()

# student()





# def test1():
#     num1 = 200
#     def test2():
#         nonlocal num1
#         num1 = num1 * num1
#         print(num1)
#     test2()
# test1()






#Closure
# def outer():
#     x = 10 #local variable

#     def inner():
#         print(x)
    
#     inner()

# outer()



# num1 = 200
# def test_func():
#     global num1
#     num1 = num1 + 100
#     print(num1)

# test_func()


# num1 = 200
# def test_func():
#     num1 = num1 + 100
#     print(num1)

# test_func() #UnboundLocalError



# num1 = 200
# def test_func():
#     num1 = 100
#     print(num1) #100 (local)

# test_func()
# print(num1) #200 (global)





#Global
# num1 = 200
# def test_func():
#     print(num1)  #200

# test_func()
# print(num1)     #200





#Local
# def test_func():
#     num1 = 200
#     print(num1) #200

# test_func()
# print(num1) #Error




# def test_func():
#     return 
#     "AshokIT"

# x = test_func()
# print(x) #None


# def test_func(num1,num2):
#     return num1+num2, num1-num2, num1*num2, num1/num2

# addition, subtraction, multiplication, division =  test_func(200,100)
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)




# def test_func(num1,num2=200,num3=300):
#     print(num1,num2,num3)

# test_func(100)                              #100 200 300
# test_func(100,num3=3000)                    #100 200 3000
# test_func(num1=1000,num2=None,num3=3000)    #1000 None 3000





# ** --> create dictionary internally
# def test_func(**data):
#     print(data)
#     print(type(data))

# test_func(name="AshokIT", course="Gen AI with RAG") #{'name': 'AshokIT', 'course': 'Gen AI with RAG'}
