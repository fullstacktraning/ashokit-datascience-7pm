# key - value
# mutable
# ordered (>3.7) and unordered(<3.7)
# {}

# Example-1
# d1 = {"num1":200,"num2":100}
# print(d1)

# d2 = dict(num1=200,num2=100)
# print(d2)

# d3 = dict([("num1",200),("num2",100)])
# print(d3)

# d4 = {}
# print(d4)

# Example-2
# Access
# d1 = {"num1":300,"num2":200}
# print(d1["num1"])
# print(d1.get("num3"))

# Add
# d1["num3"] = 100
# print(d1)

# update
# d1["num1"] = 3000
# d1.update({"num2":2000,"num3":1000})
# print(d1)


# delete
# d1 = {"num1":300,"num2":200,"num3":100}
# del d1["num30"]
# print(d1)

# print( d1.pop("num1") )
# print(d1)

# d1.popitem()
# print(d1)

# d1.clear()
# print(d1)

# Loop
# d1 = {"num1":300, "num2":200, "num3":100}
# for k in d1:
#     print(k)

# for v in d1.values():
#     print(v)

# for k,v in d1.items():
#     print(k,v)

# print(d1.keys())
# print(d1.values())
# print(d1.items())

# d1 = {x:x*x for x in range(5) if x%2 == 0}
# print(d1)


# d1 = {"num1" : 300}

# d2 = d1.copy() # shallow copy
# d1["num1"] = 3000
# print(d2)


# d2 = d1 # ref copy
# d1["num1"] = 3000
# print(d2)


# students = {
#     "s1" : {"name":"std1","marks":90},
#     "s2" : {"name":"std2","marks":80}
# }

# for v in students.values():
#     for val in v.values():
#         print(val)

# keys - int,float,str,tuple, bool,None (allowed), list & dict (not allowed)
# d1 = {
#     10 : "Hello_1",
#     10.1 : "Hello_2",
#     "str" : "Hello_3",
#     (10,20) : "Hello_4",
#     True : "Hello_5",
#     None : "Hello_6",
#     # [10,20]: "Hello_7"
#     # {"str":"Hello"} : "Hello_8"
# }
# print(d1)

# str = "aaabbbccc"
# freq = {}
# for ch in str:
#     freq[ch] = freq.get(ch,0) + 1

# print(freq)


d1 = {"a":3, "b":1, "c":2}
sorted_d1 = sorted(d1.items(),key=lambda x:x[1])
print(dict(sorted_d1))