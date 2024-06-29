# loops
# print from 0 to 9
for i in range(0,10):
    print(i,end=" ") # printing in same line
    
print() # next line

for i in range(0,10,2):
    print(i, end=" ")

print()

for i in range(0,5):
    print(i,end="\n")
    
pylist = ["Numpy", "Pandas", "Matplotlib", "Sciket Learn", "Seaborn", "Keras"]
for i in pylist:
    print(i,end=" ")

print()

jslist = ["ReactJS","NodeJS","ExpressJS","AngularJS","NextJS"]
for i in jslist:
    print(i,end=" ")

i = 0
while i <= 5:
    print("While loop using python")
    i = i + 1
    
# n = int(input("Enter n: "))
# for _ in range(n):
#     print("*"*5)
    
# print("Dollar rectangle: ")
# n2 = int(input("Enter the number of rows: "))
# m2 = int(input("Enter the number of columns: "))
# for i in range(n2):
#     for j in range(m2):
#         print("$",end=" ")
#     print()
    
# print("Star triangle: ")
# n3 = int(input("Enter n: "))
# for i in range(n3):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# lists
print("Python lists: ")
pylist = ["numpy", "pandas", "matplotlib"]
for i in pylist:
    print(i,end=" ")
print()

print("Single element: ", pylist[1])
# python also follows 0 based indexing


pylist[2] = "keras"
print(pylist[0], pylist[1], pylist[2])

print(type(pylist))

print("Negative indexing in python: ", pylist[-1]) #prints elements from last
print("Sub array in python: ", pylist[1:2]) # list[start_index: end_index+1]
print("Subarray with negative indexing: ", pylist[-3:-1])

# some built in functions 
pylist.append("matplotlib")
pylist.append("pytorch")
for i in pylist:
    print(i,end=" ")

print()
pylist.remove("numpy")
for i in pylist:
    print(i,end=" ")
    
print()
pylist.insert(0,"numpy")
for i in pylist:
    print(i,end=" ")

print()
jslist = ["react","node","express","angular"]
pylist.extend(jslist) # extend is used to concat 2 arrays
for i in pylist:
    print(i,end=" ")
   
print() 
num_list = [1,2,3,4,5,6,7]
num_list.pop(3) # remove tht particular index
for i in num_list:
    print(i,end=" ")

#subarray concept
jslist[0:3] = ["apple","microsoft","nvidia"]
print(jslist)

jslist[1:3] = "google"
print(jslist)

jslist.append("meta")
print(jslist)

unsorted = [10,18,2,7,9,1,-20,70]
unsorted.sort()
print(unsorted)

jslist.sort(reverse=True)
print(jslist)

pylist.reverse()
print(pylist)

# list comprehension
list_comprehension = [i for i in num_list if i>5]
print(list_comprehension)

copy = pylist.copy()
print(copy)

#nested list
new_list = [10, 40, [20, 70, 90], 30]
print(new_list[2][2])

# swap 2 elements in the list
# marks = []
# m = int(input("Enter size of the list: "))
# for _ in range(m):
#     num = int(input())
#     marks.append(num)

# print(marks)

# idx1 = int(input("Enter 1st index: "))
# idx2 = int(input("Enter 2nd index: "))

# temp = marks[idx1]
# marks[idx1] = marks[idx2]
# marks[idx2] = temp

# print(marks)

# tuples: similar to lists, used to store multiple elements in one variable
colors = ("orange", "blue", "green", "red")
print(colors)
print(type(colors))

tpl = tuple(("apple","samsung","qualcomm"))
print(tpl)

lst = list(["1","2","3"])
print(lst)

# tuple properties
'''
tuple are ordered, immutable(unlike lists), duplicates allowed, different datatypes allowed
'''
tupple = ("name","prathica",18,98.92)
print(tupple, len(tupple))

if "apple" in tpl:
    print("apple is in the tuple")
if "nvidia" not in tpl:
    print("nvidia is not present in tuple")

# traversal
for i in tpl:
    print(i,end=" ")

print()
num_tpl = (1,2,3,4,5,6)
for i in reversed(num_list):
    print(i, end=" ")

print()
# typecast list into tuple
listss = ["modi","rahul gandi","kejrival"]
tupless = tuple(listss)
print(tupless)
   
# SETS: it is also similar to lists and tuples
setts = {"apple","microsoft","google", "meta"} 
print(setts, type(setts), len(setts))
#properties: unordered, contains only unique elements, immutable(only addition deletion possible, update not possible)

for i in setts:
    print(i, end=" ")

print()
setts.add("JP Morgan")
setts.add("Morgan Stanley")
print(setts)

# adding sets to existing set
setts.update(["Amazon","Flipkart"])
print(setts)

setts.remove("Morgan Stanley") # might throw an error if its not present
setts.discard("phonepay") # doesn't thow error if it is not present
print(setts)

# joins 2 sets using union()
sets = {"OpenAI","X","Myntra"}
new_set = setts.union(sets)
print(new_set)
setss = {"whatsapp", "facebook"}
# or it can also be done using
setss.update(sets)
print(setss)

s1 = {1,2,3,4}
s2 = {2,7,8,9,3}
s1.intersection_update(s2) # finds common elements
print(s1)
s2.symmetric_difference_update(s1) # keep all elements except the common ones
print(s2)

# find the common elements using sets
'''
1. convert list to sets
2. concat any 2 sets
2. find the intersection update
'''
lst1 = [10, 20, 30, 40]
lst2 = [30, 40, 90, 110]
lst3 = [20, 30, 80,10]

set1 = set(lst1)
set2 = set(lst2)
set3 = set(lst3)

print(set1,set2,set3)

set1.update(set2)
print(set1)
set1.intersection_update(set3)
print(set1)


