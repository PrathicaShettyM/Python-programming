# Sets : container for storing multiple values in a variable
names = {"John", "Mary", "Dave"}
print(names)

# properties : unordered, immutable(cant update but addition, deletion possible), unindexed, no duplicates, any datatype(mixture is also allowed)

# length
print("length : ",len(names))

# datatype
print("type : ", type(names))

# accessing items of set
for x in names:
    print(x)

# check if the item exists
if "John" in names:
    print("Yes John is present in the set")

# add elements to the list
names.add("Ria")
print(names)

names.add("John")
print(names) # will print the same set becoz sets dont contain duplicates

# add another sequence(a list or a tuple) to the set
# set.update(another_sequence) : add another sequence items to the existing set
names_list = ["Kia", "Wilson"]
names.update(names_list)
print(names)

# removing an item fromt the set
names.remove("Dave")
print(names)

# if u try to remove an item which is not present in the set, then compiler throughs error
# in that case use discard() , so it wont through an error
names.discard("Micheal") # it wont through an error if the value is not present in the set

# joining 2 sets
# method 1: use union()
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
print(s1, s2)

s3 = s1.union(s2)
# print(s3)

# # method 2: using update()
# s1.update(s2)
# print(s1)

# keep only the common items while joining : intersection_update()
# s1.intersection_update(s2)
# print(s1)

# keep all values except duplicates : keep common ones out
# s1.symmetric_difference_update(s2)
# print(s1)

# common elements in 3 arrays
# algo : typecast them into sets, join all the 3 sets using intersection_update

lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 30, 50, 70]
lst3 = [30, 50, 90, 120]

# type-casting lsit into sets
set1 = set(lst1)
set2 = set(lst2)
set3 = set(lst3)
print(set1, set2, set3)

# joining sets : 1 and 2 and storing result in set1
set1.update(set2) # or else use intersection() and store in another variable
print(set1)

# intersection_updating set1 and set3
set1.intersection_update(set3)
print(set1)















