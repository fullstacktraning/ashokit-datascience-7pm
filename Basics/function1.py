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
