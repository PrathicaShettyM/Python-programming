# Strings
# they are a sequence of characters that is written '',"",''' '''
# they are immutable 
print("This is a string")
print('This is also string')
print('''And This is also a string''')

name1 = 'College Wallah'
name2 = "Physics wallah"
name3 = '''MBA Wallah'''
print(name1, name2, name3)
print(type(name1), type(name2), type(name3))

'''
This is a multiline string
'''
text = "Hello, World"
print(text[0], text[3], text[5], text[-1]) # negative indexing for accessing elements from last

# traversing a string
for i in name1:
    print(i)
print()

# List comprehension
lst = [char for char in name2]
for i in lst:
    print(i)
    
# len()
print("Length of string name1: ",len(name1))

# accessing the substring 
print("substring1: ", name1.find('e')) # returns the index
print("substring2: ", name1.find('z')) # returns -1 if not present

# find a char/substring in a string
print(name1.find('e')) # returns index of the 1st occurence of the character/string
print(name1.find(' '))

# SLICING : get a part of the string
# syntax : [start: end+1] (inclusive : exclusive(so take end+1))

print("Slicing a string:",name1[2:6])
print("Slicing a string:",name1[:6]) # if start is not mentioned then it takes substring from 0 to n-1
print("Slicing a string:",name1[3:]) # if end is not mentioned then it takes substring from n to last index

# nagative slicing
print("Negative slicing a string:", name2[-3:]) # if only start is mentioned it takes from -3 to starting character
print("Negative slicing a string:",name2[-3:-1])

# covert to upper case
str = "new york"
str1 = str.upper()
print("To Upper case:",str1)
 
# convert to lower case
str2 = str1.lower()
print("To lower case:",str2)

# for capitalising the 1st character
str3 = str2.capitalize()
print("Capitalise 1st character: ", str3)

# strip: used to strip the trailing whitespaces in the beginning and ending of the string
# doesn't remove spaces in between the characters
str4 = "         hello    world    "
print(str4)
print("Strip:", str4.strip())

# replace: replace old substring with new substring 'count' no. of times
'''
Here virat occurs at 2 places, if the count is '1' 1st virat is placed by "gill" or else if the count is 2,
then both the places virat will be replaced by "gill"
'''
str5 = "Hello virat, welcome virat"
print("replace:")
print(str5.replace("virat","gill", 1))

# split: used to split the string into a "list" of sub-strings
# syntax: string.split(separator, maxsplit)
# separator can be anything like " ", "*","-" bu tby default it is whitespace
# maxsplit: how many times we want to separate the substring, by default it is the no. of times the separator occurs

s = "apple mango banana grapes strawberry"
ss = "apple_ibm_microsoft_adobe"
sss = "iphone-macbook-ipad"
s1 = s.split()
print("split:")
print(s1)
print(ss.split("_"))
print(sss.split("-", 1))

# concatenate: join 2 strings
s2 = "Hello "
s3 = "Good morning"
print(s2+s3)

# format: used to insert variable values in a string
student_name = "Prathica"
math_test_marks = 50
math_quiz_marks = 10
str6 = "The student name is {p}, and he is a maths topper, his math marks in test is {m} and his quiz marks is {q}".format(p = student_name, m = math_test_marks, q = math_quiz_marks)
print(str6, "he is also invincible")

# Escape Characters
# there are some special character which are used to print some non-printable/ reserved characters in strings
print("Don\'t go to exam hall without maths practise")
print("\\this is because /n \r it gets \t too \b horrible")

print("Practise time: ")
textt = "The unexpected always happens"
print(textt)
print(len(textt))
print(textt.find('pp'))
print(textt[:11])
print(textt.replace('always','never'))
text2 = "no matter wht"
new_text = textt+text2
print(new_text)

# 1. string palindrome
'''
approach:
1. remove whitespaces between string
2. convert to lower case for uniformity
3. reverse and find palindrome
'''
def check_palindrome(str):
    #clean the string
    clean_str = (str.replace(" ", "")).lower()
    # reverse the string
    reverse_string = str[::-1]
    return clean_str == reverse_string

print(check_palindrome("malayalam"))
print(check_palindrome("amla"))

'''
1. mcq
str1 = "poWer"
str1.upper()
print(str1)

output: poWer not POWER beacuse we are printing 'str1' not 'str1.upper'
in upper function original string doesn't change
'''


