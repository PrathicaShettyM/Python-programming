# Dictionary: store key value pairs
student_record = {
    "mark zukerburg": 1892,
    "bill gates": 8973,
    "elon musk": 7463,
    "sunder pichai": [123423,
                      232434]
}
print(student_record)
print(type(student_record))
print(len(student_record))
'''
Properties:
1. ordered
2. changeable
3. unindexed
4. duplicates not allowed(keys are unique)
5. any datatype

'''
# access elements of dictionary
print(student_record["bill gates"])
print(student_record.get("mark zukerburg"))

# print the keys
print(student_record.keys())

# update
student_record["bill gates"] = 98700
print(student_record)

# add elements
student_record["jensen"] = 10000
print(student_record)

# add a dictionary to a dictionary
more_students = {
    "kia":12900
}
student_record.update(more_students)
print(student_record)

# remove elements
student_record.pop("jensen")
print(student_record)

# remove the last added item
student_record.popitem()
print(student_record)

# enpty the dictionary: clear all the entries
# student_record.clear()
# print(student_record)

# loop through the dictionary

# print only the keys
for i in student_record:
    print(i, end=" ") 

# print only the values
for i in student_record:
    print(student_record[i], end=" ")

# print both keys and values
for i,j in student_record.items():
    print(i,j)
    
# nested dictionaries
phones = {
    "area1":{
        "x1":1,
        "y1":2
    },
    "area2":{
        "x2":3,
        "y2":4
    }
}
# aceesing elements in nested dictionaries
print(phones["area1"]["y1"])
print(phones["area2"]["x2"])

# q1. find the sum of all the items in the dictionary
ip = {
    'a':100,
    'b':200,
    'c':300
}
sum_ip = 0
for i in ip:
    sum_ip += ip[i]
print("Sum of all elements: ",sum_ip)
# one shot answer using built in functions
print(sum(ip.values()))

'''
q2. diven a string and a number 'n', we need to mirror the characters from the Nth position up to the length of
the string in alphabetical order. in mirror operation we change the characters from 'a' to 'z', 'b' to 'y' and so on..
''' 
'''
use dictionary for this like {a:z,b:y...}
use zip to combine the lists [a,b,c..] and [z,y,x...] into a dictionary
'''

input_string = input("Enter the string: ")
n = int(input("Enter the number: "))

# create dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1] # from z to a
dictionary = dict(zip(alphabets, reverse_alphabets)) #create a dictionary

# finding substring for mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# mirror the substring
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dictionary[suffix[i]]
    
res = prefix+mirror
print(res)

















