# Set - Unordered(no index), {}, unique elements, Mutable

# Example-1
# s1 = {1,2,3}
# print(s1)
# s2 = {1,1,2,2,3,3}
# print(s2)
# list1 = [10,20,10,20,30]
# s3 = set(list1)
# print(s3)

# Example-2
# empty = {}
# print(type(empty))  # <class 'dict'>

# empty1 = set()
# print(type(empty1)) # <class 'set'>

# Example-3
# s1 = {1,2}
# s1.add(3)
# list1 = [4,5]
# s1.update(list1)
# print(s1)

# Example-4
# s1 = {10,20,30,40,50}
# s1.remove(10)
# print(s1)
# s1.discard(10)

# Example-5
# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1 | s2)              #union
# print(s1.union(s2))         #union
# print(s1 & s2)              #intersection
# print(s1.intersection(s2))  #intersection
# print(s2-s1)                # difference
# print(s1^s2)                # symetric

# Example-6 (Search)
# s1 = {10,20,30}
# print(20 in s1)
# print(200 in s1)

# Example-7 (loop)
# s1 = {10,20,30,40,50}
# for element in s1:
#     print(element)

# Example-8 (Immutable)
# fs = frozenset([1,2,3])
# print(fs)
# fs.add(4)

# s1 = {True,1,1.0}
# print(s1) #{True}

# s1 = {x*x for x in range(1,5,2)}
# print(s1)

# list1 = [10,20,30,10,20,30]
# print( list(set(list1)) )

# python_students = {"Std1","Std2","Std3"}
# genai_students = {"Std1","Std2","Std4"}
# print(python_students & genai_students)
# print(python_students.intersection(genai_students))

# str = "python is eazy and python is powerful"
# words = str.split()
# unique_words = set(words)
# print(unique_words)
# print(len(unique_words))

# str = "this is a simple sentence"
# stop_words = {"is","a"}
# result = []
# for word in str.split():
#     if word not in stop_words:
#         result.append(word)

# print(" ".join(result))

nums = [1,2,3,2,4,5,1]
seen = set()
duplicates = set()

for n in nums:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(duplicates)
print(seen)
