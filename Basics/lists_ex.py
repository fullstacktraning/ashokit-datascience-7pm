# List
# Collection of elements
# []
# Ordered
# Mutable (we can modify)
# Allow duplicates
# Hetrogeneous Elements

# Example-1 (Basics)
# list1 = []
# print(list1)

# list2 = [10,20,30,40,50]
# print(list2)

# list3 = [10,"Hello",True,10.1,None]
# print(list3)

# list4 = list("Hello")
# print(list4)

# list5 = list(range(5))
# print(list5)



# Example - 2 (Slicing)
# list1 = [10,20,30,40,50]
# print(list1[0], list1[-5])
# print(list1[0:3])
# print(list1[:2])
# print(list1[-3:])
# print(list1[-4:-1])
# print(list1[::-1])

# Example - 3 (Mutability)
# list1 = [1,2,3]
# list1[0] = 100
# print(list1) #[100, 2, 3]

# Example-4 (Add Element)
# list1 = [1,2]
# list1.append(3)
# list2 = [4,5]
# list1.extend(list2)
# list1.insert(1,99)
# print(list1)

# Example-5 (Delete)
# list1 = [1,2,3,2]
# list1.remove(2)
# print(list1) # removes first "2"
# list1.pop() # removes last element
# print(list1)
# list1.pop(1) # remove based on index
# print(list1)
# list1.clear() # remove all elements
# print(list1)

# Example-6 (Search)
# list1 = [1,2,3,2,2]
# print(list1.index(2))
# print(list1.index(3))
# print(list1.index(4))

# Example-7 (Frequency Of Elements)
# list1 = [1,2,3,2,2]
# print(list1.count(2))
# print(list1.count(4))

# Example-8 (Sorting)
# list1 = [5,2,9,1]
# list1.sort() # mutable
# print(list1) # ascending
# list1.sort(reverse=True) # decending
# print(list1)
# new_list = sorted(list1,reverse=True) # immutable
# print(new_list)
# print(list1)

# Example-9 (Loops)
# list1 = [10,20,30,40,50]
# for element in list1:
#     print(element)

# for i in range(len(list1)):
#     print(f'index : {i} and element : {list1[i]}')

# Example - 10 
# list1 = [i*i for i in range(5)]
# print(list1)