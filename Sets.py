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
















