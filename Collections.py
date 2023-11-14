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

# extend









