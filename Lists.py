# Python collections(arrays)
# 1. List   2. Tuples   3. Set  4. Dictionary

# LIST : allow us to store multiple items in a single value
# features: indexing, ordered, mutable, duplicates allowed, any datatype, mix of datatypes allowed
fruits = ["apple", "mango", "banana", "cherry"]
print(fruits[1])
print("Before mutation: ",end="")
print(fruits)

#updation
fruits[1] = "grapes"
print("After mutation: ",end="")
print(fruits)

#type and length
print("Datatype: ",end="")
print(type(fruits))
print("Length of the List: ",end="")
print(len(fruits))

# check if the item is in the list
if "banana" in fruits:
    print("Banana is a part of the list")
if "Kiwi" not in fruits:
    print("Kiwi is not a part of the list")

# accessing list items
# 1.Indexing     2.Negative Indexing     
# 3.Range of indexes : create a sub array with the main array
# ex: list[startIndex(inclusive) : endIndex(exclusive)]   
# 4.Range of negtive indexes
print("Negative indexing : ", end="")
print(fruits[-1])

listing = [10, 20, 30, 40, 50] # to create a subArray of [20,30]
print("SubList : ", end="")
print(listing[1:3])
print("SubList with negative indexing : ", end="")
print(listing[-3:-1])

# adding elements to the list
# 1.append() : add items to the end of the list
# 2.insert()  
# 3.extend()

newList = [10,20,30,40]
print("List: ",end="")
print(newList)

# append
newList.append(50)
print("Appended List: ",end="")
print(newList)

# insert
newList.insert(2,60)
print("Insert List: ",end="")
print(newList)

# extend : append another list to the cureent list or append another datatype to the current list
# concat list using extend()
li = [100,200,300]
newList.extend(li)
print("Extend List: ",end="")
print(newList)

#Remove elements from the list
# 1.remove(element) : the mentioned element 
# 2.pop() or pop(index): removes last element or the element of the given index

li2 = [100, 200, 300, 400, 500, 600, 700]
li2.remove(200)
print(li2)

li2.pop()
print(li2)

li2.pop(0)
print(li2)

# change items in a list
# 1. at an index     list[2] = 4
# 2.in a range
# variations of range in list
li2[0:3] = ["apple", "kiwi", "papaya"]
print(li2)
#['apple', 'kiwi', 'papaya', 600]

li2[1:3] = ["apple"]
print(li2)
# ['apple', 'apple', 600]

li2[1:3] = "blackberry"
print(li2)
# ['apple', 'b', 'l', 'a', 'c', 'k', 'b', 'e', 'r', 'r', 'y']

# sorting lists
li3 = [10,-90,20,70,-111]
veggies = ["carrot","beans","tomato","potato"]

# ascending
li3.sort()
print(li3)

# for descending
veggies.sort(reverse=True)
print(veggies)

rev = [10, 30, 50, 70, 99]
rev.reverse()
print(rev)









