# TUPLES : used to store multiple items in a variable

colors = ("orange","blue","green","red")
print(colors)

# another way to create a tuple
numbers = tuple(("1"))
nums = list("1")
print(numbers)
print(nums)

# properties of TUPLES:
# 1.Ordered 
# 2.Immutable : but lists mutable
# 3.Duplicates allowed 
# 4.any datatype 
# 5.mix of different datatypes
# Note : tuple of 1 item shd be followed by a " , " or else it will treat it as int or str


# tuple of 1 item the right way
fruits = ("apple",)

# datatype of tuple
print(type(colors))

# length of tuple
print(len(colors))

# accessing tuple items
print(colors[1])    #positive indexing(2nd element)
print(colors[-1])   #negative indexing(last element)

# range indexing : tplName[startIdx:endIdx+1]
print(colors[1:3]) # with +ve indexing
print(colors[-2:]) # with -ve indexing

# check if an item is in a tuple
if "red" in colors:
    print("Red is present in the tuple")
if "black" not in colors:
    print("Black is not present in the tuple")

# traversing in a tuple
for i in colors:
    print(i,end=" ")
print()

# concating 2 tuples
more_colors = ("yellow","pink")
colors = more_colors + colors
print(colors)

# unpacking a tuple: add the tpl items into separate variables
tpl = ("item1","item2","item3") # give only 3 variables or else it will throw an error
itm1,itm2,itm3 = tpl
print(itm1)
print(itm3)
print(itm2)

# Reverse a tuple
#  reversed() : to iterate through a sequence in a reversed order

# method 1 : direct 
tpl2 = (1,2,3,4,5,6)
for i in reversed(tpl2):
    print(i, end=" ")
    
# method 2 : algo
# algo : tuples are immutable, so first store them in a list and then type cast it into a tuple
listRev = []
for i in tpl2:
    listRev.append(i)  # appending list items in a list

outputTpl = tuple(listRev) #typecaste a list into a tuple
print("\n", outputTpl)

# question
print((1,2) + (3,4))
# this is concatinate not add them

