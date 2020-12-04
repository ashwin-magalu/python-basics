import re  # import for regex
import turtle  # import for turtle

# Variables

""" a = 5
print(a)

b = "Hello"
print(b)

c = True
print(c) """

# *This is a square
""" ashwin_turtle = turtle.Turtle()
ashwin_turtle.forward(100)
ashwin_turtle.right(90)
ashwin_turtle.forward(100)
ashwin_turtle.right(90)
ashwin_turtle.forward(100)
ashwin_turtle.right(90)
ashwin_turtle.forward(100) """
# *This makes a square box by drawing a line

# Functions
''' 
ashwin_turtle = turtle.Turtle()
ashwin_turtle.speed(1)


def square():
    ashwin_turtle.forward(100)
    ashwin_turtle.right(90)
    ashwin_turtle.forward(100)
    ashwin_turtle.right(90)
    ashwin_turtle.forward(100)
    ashwin_turtle.right(90)
    ashwin_turtle.forward(100)
 '''

"""
square()
ashwin_turtle.forward(100)
square() """

# If else Statements

""" elephant_weight = 3000
ant_weight = 0.1

if(elephant_weight > ant_weight):
    square()
else:
    ashwin_turtle.forward(100)
    ashwin_turtle.right(90) """


# While loops

""" ashwin = "happy"

while ashwin == "happy":
    ashwin_turtle.forward(50) """


# For loops

""" for i in range(5, 10):
    print(i)  # 5 6 7 8 9

for count in range(4):
    square() """


# Primitive Data Types

"""
Integers ==> 1 2 3 4
Floats ==> 0.5 2.5
Strings ==> "ABC"
Booleans ==> True False
 """

# Casting ==> Changing from one data type to another data type

""" a = 10
b = 5.4
c = "15"
d = "False"


print(float(a))
print(int(b))
print(str(a))
print(int(c))
print(bool(d)) """

# Strings

""" s = "Hello World"
print(s)  # Hello World
print(s[1])  # e """

# Lists ==> Array (Technically a "Data Structure", but think of it as a data type!)

""" a = [1, 2, 3]

l = [1, 2.3, True, "ABC", [4, 5, 6], {"A": "Hi"}, a]

names = ["Joe", "John", "James"]

print(l)
print(l[5])

print(names)
names.append("Agasthya")
print(names)
names.insert(0, "Vasishta")
print(names)
print(names.pop())
print(names)
names.remove("Joe")
print(names)
names.reverse()
print(names)

numbers = [10, 5, 25, 7, 50, 35]

print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

for number in numbers:
    print(number) """


# Advanced Indexing, Slicing and Striding

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indexing
""" print(digits)
print(digits[0])  # 0
print(digits[len(digits) - 1])  # 9
print(digits[-1])  # 9
print(digits[-len(digits)])  # 0

# Slicing
print(digits[:3])  # [0,1,2]
print(digits[0:3])  # [0,1,2]
print(digits[2:4])  # [2,3]
print(digits[6:])  # [6,7,8,9]
print(digits[0:-1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Striding
print(digits[0:10:1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[0:10:2])  # [0, 2, 4, 6, 8]
print(digits[0:10:3])  # [0, 3, 6, 9]
print(digits[1:10:2])  # [1, 3, 5, 7, 9]
print(digits[10:0:-2])  # [9, 7, 5, 3, 1]
print(digits[10:0:-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(digits[10::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] """

""" for i in range(len(digits) + 1):
    print(digits[0:i]) """
""" 
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 """

""" for i in range(len(digits) - 2):
    print(digits[i: i+3]) """

""" 
[0, 1, 2]
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
[4, 5, 6]
[5, 6, 7]
[6, 7, 8]
[7, 8, 9]
 """

""" window_size = 3
for i in range(len(digits) - (window_size-1)):
    print(digits[i: i + window_size]) """
""" 
[0, 1, 2]
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
[4, 5, 6]
[5, 6, 7]
[6, 7, 8]
[7, 8, 9]
 """

# Split and Join

""" problems = "broke, pale, short, nerdy"

print(problems)  # broke, pale, short, nerdy

l = problems.split(", ")
print(l)  # ['broke', 'pale', 'short', 'nerdy']

joined = ' and '.join(l)
print(joined)  # broke and pale and short and nerdy

csv = ', '.join(l)
print(csv)  # broke, pale, short, nerdy """

# Tuples

""" t = (1, 2, 3, True, {"a": "Hi"}, [4, 5, 6])

print(t)  # (1, 2, 3, True, {'a': 'Hi'}, [4, 5, 6])
print(t[4])  # {'a': 'Hi'}

credit_card1 = (1234567890123456, "Ashwin M A", "03/22", 678)
credit_card2 = (2345678901234567, "Akshay M A", "05/23", 123)

credit_cards = [credit_card1, credit_card2]
print(credit_cards)
#[(1234567890123456, 'Ashwin M A', '03/22', 678), (2345678901234567, 'Akshay M A', '05/23', 123)]

person1 = ("Ashwin M A", 26, "Biriyani")
person2 = ("Akshay M A", 22, "Kadbu")

persons = [person1, person2] """

""" name, age, fav_food = person1  # unpacking tuples

print(person1)
print(name) # Ashwin M A
print(age) # 26
print(fav_food) # Biriyani
 """

""" for name, age, favFood in persons:
    print(name)
    print(age)
    print(favFood) """
""" 
Ashwin M A
26
Biriyani
Akshay M A
22
Kadbu
 """

# Sets ==> It can't have duplicates in it, It is unordered

''' s = {"blueberry", "rasberry"}
print(s)  # {'rasberry', 'blueberry'}

s.add("strawberry")
print(s)  # {'blueberry', 'strawberry', 'rasberry'}

s.add(4)
print(s)  # {'strawberry', 'blueberry', 4, 'rasberry'}

s.add("blueberry")
print(s)
# {4, 'rasberry', 'strawberry', 'blueberry'} ==> blueberry not added as it was a duplicate


l = [1, 2, 3, 4, 4, 4, 5]
print(l)  # [1, 2, 3, 4, 4, 4, 5]
no_duplicate_set = set(l)
print(no_duplicate_set)  # {1, 2, 3, 4, 5}
no_duplicate_list = list(no_duplicate_set)
list_of_numbers = no_duplicate_list
print(list_of_numbers)  # [1, 2, 3, 4, 5] '''

# Venn Diagram Set Operations

''' library_1 = {"Harry Potter", "Hunger Games", "Lord of the Rings"}
library_2 = {"Harry Potter", "Romeo and Juliet"}

all_books_in_town = library_1.union(library_2)
print(all_books_in_town)
# {'Harry Potter', 'Romeo and Juliet', 'Hunger Games', 'Lord of the Rings'}
common_books = library_1.intersection(library_2)
print(common_books)  # {'Harry Potter'}
diff1 = library_1.difference(library_2)
print(diff1)  # {'Hunger Games', 'Lord of the Rings'}
diff2 = library_2.difference(library_1)
print(diff2)  # {'Romeo and Juliet'}
clear_library_2 = library_2.clear()
print(clear_library_2)  # none
print(library_2)  # set() '''

# Dictionaries (Key, Value pairs) ==> Datastructure

'''
These are really good for:
    Super organized data (mini database)
    Fast as hell (constant time)
 '''

''' groceries = {"tomato": 5, "potato": 3}
print(groceries)  # {'tomato': 5, 'potato': 3}
print(groceries["tomato"])  # 5
print(groceries.get("potato"))  # 3 '''

''' contacts = {"Joe": ["123-456", "joe@email.com", ],
            "Jane": {"num": "987-654", "email": "jane@email.com"}}
print(contacts["Jane"])  # {'num': '987-654', 'email': 'jane@email.com'}
print(contacts["Jane"]["num"])  # 987-654 '''

''' sentence = "I like the name Agasthya, because the name Agasthya is the best"

word_counts = {
    "I": 1,
    "like": 1,
    "the": 3,
} '''

#word_counts["the"] += 1
# print(word_counts)

# dict.items() ==> returns the list containing individual tuple for all key-value pairs
''' print(word_counts.items())  # dict_items([('I', 1), ('like', 1), ('the', 3)]) '''

# dict.keys() ==> returns the list of keys
''' print(word_counts.keys())  # dict_keys(['I', 'like', 'the']) '''

# dict.values() ==> returns the list of values
''' print(word_counts.values())  # dict_values([1, 1, 3]) '''

# dict.pop() ==> removes mentioned key and its value from dictionary
''' word_counts.pop("I")
print(word_counts)  # {'like': 1, 'the': 3} '''

# dict.popitem() ==> removes the last item from the dictionary
''' word_counts.popitem()
print(word_counts)  # {'I': 1, 'like': 1} '''

# dict["key"] =value ==> Adds key and value at the end of the dictionary
''' word_counts["Agasthya"] = 2
print(word_counts)  # {'I': 1, 'like': 1, 'the': 3, 'Agasthya': 2} '''

# dict.clear() ==> wipe out the entire disctionary
''' word_counts.clear()
print(word_counts)  # {} '''

# print(sorted(list(word_counts.values())))  # [1, 1, 3]


# Mutability ==> Changeable
''' 
Lists => Mutable
Tuples => Immutable
Dictionaries => Mutable
Keys in Dictionaries => Immutable
Ints => Immutable
Floats => Immutable
Strings => Immutable
Boolean => Immutable
OrderedDictionaries => Mutable
Sets => Mutable
 '''


# List Comprehension

''' names = ["Jennifer", "Susan", "Jane", "Sophie"]
l = []

for person in names:
    l.append(person)
print(l)  # ['Jennifer', 'Susan', 'Jane', 'Sophie']

print([person for person in names])  # This is list comprehension
#['Jennifer', 'Susan', 'Jane', 'Sophie']

l = []
for person in names:
    l.append(person + ' dumped me')
print(l)
# ['Jennifer dumped me', 'Susan dumped me', 'Jane dumped me', 'Sophie dumped me']

# This is list comprehension
print([person + ' dumped me' for person in names])
#['Jennifer dumped me', 'Susan dumped me', 'Jane dumped me', 'Sophie dumped me'] '''

''' movies_and_ratings = {"Interstellar": 9,
                      "Dark Knight": 3, "50 Shades": 4, "Iron Man": 10}
l = []

for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        l.append(movie)
print(l)  # ['Interstellar', 'Iron Man']

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])
#['Interstellar', 'Iron Man'] '''


# Regex

# Email Address Text Scrapper


''' text = "A random string"
pattern = re.compile("A random string") # It search for a whole string
result = pattern.search(text)
print(result)  # <re.Match object; span=(0, 15), match='A random string'> '''

''' text = "A random string"
pattern = re.compile("[ABCrs]")
# Search for first single letter match, it is case sensitive
result = pattern.search(text)
print(result)  # <re.Match object; span=(0, 1), match='A'> '''

''' text = "A random string"
pattern = re.compile("[c-m]")
# Search for first single letter match in a specified range, it is case sensitive
result = pattern.search(text)
print(result)  # <re.Match object; span=(5, 6), match='d'> '''

''' text = "A random string"
pattern = re.compile("[A-Ec-m]")
# Search for first single letter match in a specified range, it is case sensitive
result = pattern.search(text)
print(result)  # <re.Match object; span=(0, 1), match='A'> '''

''' text = "rAndom9 string"
pattern = re.compile("[a-zA-Z0-9]+")
# Search for first single word match in a specified range, it is case sensitive
result = pattern.search(text)
print(result)  # <re.Match object; span=(0, 7), match='rAndom9'> '''

''' text = "A random string, MyName123@website.com, some more random text"
pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+")
# Search for first single word match in a specified range with @,. etc, it is case sensitive
# \ here is used to escape .
result = pattern.search(text)
print(result)  # <re.Match object; span=(17, 38), match='MyName123@website.com'> '''

''' text = "A random string, My.Name_123@website.com, some more random text, YourName-888@company.net"
pattern = re.compile("[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-z]+")
# Search for words that match in a specified range with @,. etc, it is case sensitive
# '\' here is used to escape .
result = pattern.findall(text) 
print(result)  # ['My.Name_123@website.com', 'YourName-888@company.net'] '''
