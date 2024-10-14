# 1.number = [1,5,3,2,6] find the missing number

# def find_missing_number(arr):
#     arr.sort()
#     for i in range(arr[0], arr[-1]):
#         if i not in arr:
#             return i
#     return None
#
# number = [1, 5, 3, 2, 6]
# missing = find_missing_number(number)
# print(missing)


# string = "sarbajit" find first duplicate number
# string = "sarbajsit"
# def find_duplicate(s):
#     s = s.lower()
#     duplicates = []
#     for char in s:
#         if s.count(char) >1 and char not in duplicates:
#             duplicates.append(char)
#             break
#     return duplicates
#
# duplicates = find_duplicate(string)
# print(duplicates)

# fno = 1
# sno = 2
# res = fno+sno
#
# while res < 100:
#     print(res)
#     fno = sno
#     sno = res
#     res = fno+sno

#find duplicate word
# string = "sarbajit my name is sarbajit"
#
# def Duplicate_word(s):
#     s1=s.split(" ")
#     for i in s1:
#         if s1.count(i) > 1:
#             return i
#
# result = Duplicate_word(string)
# print(result)

# my_list = [1,3,2,("ss",{55.22,85},["jhj",45,75],"jjj",2331,55),"jk",26]
#
# def find_number(s):
#     numbers = []
#     for item in s:
#         if isinstance(item, (int, float)):  # Check if the item is a number
#             numbers.append(item)
#         elif isinstance(item, (list, tuple, set)):  # If the item is a list or tuple, recurse
#             numbers.extend(find_number(item))
#     return numbers
#
# result = find_number(my_list)
# print(result)

# list1 = [1,2,2,2,3,4,5]
# list2 = [2,2,3]

# common_int = []
# for item in set(list2):
#     count_list1 = list1.count(item)
#     count_list2 = list2.count(item)
#     common_int.extend([item] * min(count_list1, count_list2))
# print(common_int)

# string1 = "racerarcad"
# string2 = "car"

# indexes = []
# for char in string2:
#     index = string1.find(char)
#     if index != -1 and index not in indexes:
#         indexes.append(index)
#         string1 = string1[:index] + ' ' + string1[index + 1:]
# print(indexes)
# output  = [0,5]

# 1.X = [10,20,30] print last 2 values using : operator

# X = [10,20,30]
# print(X[-2:])

# 2.X = [10,20,30] print all elements using : operator

# X = [10,20,30]
# print(X[0:])

# 3.X = [10,20,30,40…100] print 10 30 50 and so on (alternative elements) without using the for loop.
# Hint - use :: operator

# X = [10,20,30,40,50,60,70,80,90,100]
# print(X[::2])

# 4.Store 10,20,30,....980,990,1000 into a list. Hint - use range

# numbers = list(range(10, 1001, 10))
# print(numbers)

# 5.Take a list of 10 elements print elements in reverse order, hint use :: operator

# x=[1,2,3,4,5,6,7,8,9,10]
# print(x[::-1])

# 6.Take a list of 10 elements print elements in reverse order using for loop

# x=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(x)-1,-1,-1):
#     print(x[i])

# 7.Take a list of 10 elements print all elements using for loop

# x=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(x)):
#     print(x[i])

# 8.Show one eg for the property list is mutable

# my_list = [1, 2, 3, 4, 5]
# print("Original list:", my_list)
# my_list[1] = 20
# print("Modified list:", my_list)

# 9.Modify 2nd index element of list with 300

# my_list = [1, 2, 3, 4, 5]
# my_list[1] = 300
# print(my_list)

# 10.Which method do you use to search if a given element is available in the list. Show e.g.
# how do you use it. What happens if the element is not available?

# Sample list
# my_list = [10, 20, 30, 40, 50]

# element1 = 30

# Check if the element is in the list
# if element1 in my_list:
#     print(f"{element1} is in the list.")

# Check if the element is in the list by index

# element2=31
#
# index = my_list.index(element2)
# print(f"{element2} is in the list at index {index}.")
# ValueError: 31 is not in list

# 11. Which method do you use to delete an element present in the list. Show one e.g. how do you use it.

# my_list = [10, 20, 30, 40, 50]
# element = 10
# my_list.remove(element)
# print(my_list)

# 12. Insert a new element before 1st index in the list using a method of list, show e.g. of that method

# my_list = [10, 20, 30, 40, 50]
# new_element = 6
# my_list.insert(0, new_element)
# print(my_list)

# 13. Which method do you use to delete an element present in the 1st index of the list? Show code.

# my_list = [10, 20, 30, 40, 50]
# removed_element = my_list.pop()
# print(f"Removed element: {removed_element}")
# print(my_list)

# 14.x=[ (10,20), (30,40), (50,60) ] print element 40

# x = [(10, 20), (30, 40), (50, 60)]
# print(x[1][1])

# 15. In the above example what will happen if we print(x[-1][-1])
# 60

# *******************************************_____ SET _____***********************************

# 1. Create an empty set.

# x = set()
# print(type(x))

# 2. Store 10,20,30 in a set and print 10 using index

# Sets in Python are unordered collections, meaning they do not support indexing like lists or tuples. Therefore, you
# can't access elements of a set using an index.

# 3.Print set elements using for loop

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# for i in x:
#     print(i)

# 4. Set stores elements in insertion order [t/f]
# False

# 5. Sets are faster compared to lists [t/f]
# True

# 6.Which method do you use to add a new element into the set? Show eg

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# x.update([40, 50, 60])
# x.add(20)
# print(x)

# 7.Which method do you use to delete an element from a set? Show eg

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# x.update([40, 50, 60])
# x.discard(60)
# x.remove(3)
# print(x)

# ************************************************   Dictionary   *********************************************

# 1. Dictionary - Take a dictionary insert a new pair k=30

# d = {"a": 2, "b": 20}
# d.update(k=30)
# print(d)

# 2. Dictionary - Print the value of key i

# d = {"a": 2, "b": 20, "i": 40}
# print(d["i"])

# 3. Dictionary - In the dictionary update value of key j with 20

# d = {"a": 2, "b": 20, "j": 40}
# d["j"] = 20
# print(d)

# 4. Dictionary x = {‘i’:10, ‘i’ : 20 } what happens if i print (x)
# SyntaxError

# 5.Dictionary - does it allow duplicate values
# True

# 6. Dictionary - can we get key based on value? Why?

# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# value_to_find = 'c'
# key = None
# for k, v in my_dict.items():
#     if v == value_to_find:
#         key = k
#         break
# print(key)

# 7. Dictionary - print(x[‘i’]) assume that key i is not available, what happens?
# SyntaxError

# 8. Print dictionary keys and values using a for loop.

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")

# 9. How will you print only keys present in the dictionary?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key in my_dict.keys():
#     print(f"Key: {key}")

# 10. How will you print only values present in the dictionary?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for value in my_dict.values():
#     print(f"Value: {value}")

# 11.Which method of dictionary do you use to find if a given key is available in the dictionary or not? Show eg .

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
#
# if 6 in my_dict:
#     print("key is available")
# else:
#     print("key is not available")

# 12. Which method do you use to get the value of a given key from a dictionary? Show eg?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# key = 2
# value = my_dict.get(2)
# print(f"Key: {2} value: {value}")

# 13. Which method do you use to delete a pair from the dictionary based on the given key. Show eg

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# key_to_delete = 2
# value = my_dict.pop(key_to_delete)
# print(f"Removed value: {value}")
# print(f"Modified dictionary: {my_dict}")

# 14. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 10,20

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("i")
# print(y[0], y[1])

# 15. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 20

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("i")
# print(y[1])

# 16. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 50

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("j")
# print(y[1])

# 17. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } print 10

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("a")
# z = y.get("i")
# print(z)

# 18. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } print 200

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("b")
# z = y.get("j")
# print(z)

# 19. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } dictionary a present in dictionary x

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("a")
# print(y)

# ********************************************  Functions default arg kwargs parameters ***************************

# 1. Trainer can ask find output based questions on default parameters

# def greet(name, message="Hello"):
#  return f"{message}, {name}!"
#
# print(greet("Alice"))
# print(greet("Bob", "Hi"))
# print(greet("Charlie", message="Good morning"))

# 2. Trainer can ask how do you call this method (with default parameter)

# 3. What is the data type of args internally

# The *args syntax allows the function to accept any number of positional arguments.
# These arguments are collected into a tuple named args.

# 4. What is the data type of kwargs internally

# The **kwargs syntax allows the function to accept any number of keyword arguments.
# These arguments are collected into a dictionary named kwargs.

# 5. How many times can we use args for a given function?

# In a given function definition, you can only use *args once.
# The *args parameter allows the function to accept a variable number of positional arguments, and having more than one such parameter would make it ambiguous as to which arguments belong to which *args parameter. Here is the rule and an example to clarify:

# Rule:
# A function can have only one *args parameter.
# You can, however, have other parameters before and after *args, including regular positional parameters, keyword parameters, and **kwargs.

# 6. How many times can we use kwargs for a given function?


# In a given function definition, you can only use **kwargs once. The **kwargs parameter allows the function to accept a variable number of keyword arguments, and having more than one such parameter would cause ambiguity and is not allowed by Python's syntax rules.
#
# Rule:
# A function can have only one **kwargs parameter.
# You can combine **kwargs with other parameters such as regular positional parameters, default parameters, and *args.

# 7. How many default parameters can we use for a given function?


# In Python, there is no fixed limit on the number of default parameters you can use in a given function. You can define as many default parameters as you need. However, default parameters must be placed after any positional parameters and before any *args or **kwargs in the function definition. Here's a summary of the parameter order and an example with multiple default parameters:

# 8. Def f1(a,b,*c,d=10,**e) : pass call this method and pass 1 to a, 2 to b, 3,4,5 to c and 6
# to d and pass hno=10 street =btm to e.

# def f1(a, b, *c, d=10, **e):
#  print(f"a: {a}")
#  print(f"b: {b}")
#  print(f"c: {c}")
#  print(f"d: {d}")
#  print(f"e: {e}")

# f1(1, 2, 3, 4, 5, d=6, hno=10, street='btm')

# 9. Def f1(x,y,*z=10): pass what happens if we call f1(10) what will be x y z values

# syntax error

# 10. Def f1(x,y,*z=10): pass what happens if we call f1(10,20,30) what will be x y z values

# x: 10
# y: 20
# z: (30,)

# **********************************************   List comprehension:   *****************************************

# 1. Take a list l1 copy all l1 elements into l2

# Using Slice Operator
# l1 = [1, 2, 3, 4, 5]
# # Using Slice Operator
# l2 = l1[:]
# # Using copy() method
# l3 = l2.copy()

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [1, 2, 3, 4, 5]
# print("l3:", l3)  # Output: l2: [1, 2, 3, 4, 5]

# 2. Take a list l1 copy double of each element of l1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x * 2 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 3. Take a list l1 copy each element power 2 of l1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x ** 2 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 4. Take a list l1 copy each element+1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x + 1 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 5. Take a list l1 copy all even numbers into l2

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# l2 = [number for number in l1 if number % 2 == 0]

# print(l2)

# 6. Take name=’palle’ copy all letters into l2 if it is not vowel

# name = "palle"
# vowel=["a", "e", "i", "o", "u"]
# l2 = [i for i in name if i in vowel]
#
# print(l2)

# 7. Copy even numbers from 0 to 11 into a list using comprehension

# Using list comprehension to get even numbers from 0 to 11

# l2 = [number for number in range(12) if number % 2 == 0]
#
# # l2 now contains all the even numbers from 0 to 11
# print(l2)

# ********************************  Lambda expression   *****************************************

# 1. Write a lambda expression which takes one parameter and returns element power 2, call
# that function and print the returned value

# square = lambda x: x ** 2
# result = square(5)
# print(result)

# 2. Write a lambda expression which takes 3 parameters and returns a sum. Call and print.

# sum_three = lambda a, b, c: a + b + c
# result = sum_three(3, 5, 7)
# print(result)

# 3. Write a lambda expression to find the biggest of 2 numbers. Call and print

# max_of_two = lambda a, b: a if a > b else b
# result = max_of_two(10, 20)
# print(result)

# 4. Take a list l1 copy each element+1 into l2 using map() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(map(lambda x: x + 1, l1))
# print(l2)

# 5. Take a list l1 copy all even numbers into l2 using filter() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(filter(lambda x: x%2 == 0, l1))
# print(l2)

# 6. Take a list l1 copy all elements which are greater than 10 into l2 using filter function

# l1 = [1, 2, 3, 4, 5, 10, 16, 19]
# l2 = list(filter(lambda x: x>10, l1))
# print(l2)

# 7. Take a list l1 copy half of each element into l2 using map() function

# l1 = [1, 2, 3, 4, 5, 10, 16, 19]
# l2 = list(filter(lambda x: x>10, l1))
# print(l2)

# 8. Take a list l1 copy all odd numbers into l2 using filter() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(filter(lambda x: x%2 != 0, l1))
# print(l2)

# ***************************************    Class & object:    *****************************************

# 1. Trainer can ask to call methods of a class with object

# 2. Trainer can ask to create a class with some requirements like mentioned in the
# constructor's first question. Trainer has to elaborate the requirements properly.
# Eg: create a patient class and create 2 patient objects with values pno=1,
# pname=ramesh, disease = fever. pno=2, pname=suresh, disease=cold.
# This requires students to create init method also with appropriate parameters. (this
# question can be included in constructor also)

# class Patient:
#     def __init__(self, pno, pname, disease):
#         self.pno = pno
#         self.pname = pname
#         self.disease = disease
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating the patient objects with the specified values
#
# patient1 = Patient(1, "Ramesh", "Fever")
#
# patient2 = Patient(2, "Suresh", "Cold")
#
# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()


# *************************************    Constructor:    ***************************************

# 1. There are 2 students with values sno-1 sname-ramesh sub-python, sno-2 snake=suresh
# sub AI. create a student class with init() and display(). Create above 2 objects and print
# each student object values by calling display() function

# class Student:
#     def __init__(self, sno, sname, sub):
#         self.sno = sno
#         self.sname = sname
#         self.sub = sub
#
#     def display_info(self):
#         print(f"Patient No: {self.sno}")
#         print(f"Patient Name: {self.sname}")
#         print(f"Disease: {self.sub}")
#
# # Creating the patient objects with the specified values
#
# student1 = Student(1, "Ramesh", "python")
# student2 = Student(2, "Suresh", "AI")

# # Displaying the information of each patient
# student1.display_info()
# print()  # Just to add a line break between the outputs
# student2.display_info()

# 2. Same as above question, print student object values with object without calling display()

# class Student:
#     def __init__(self, sno, sname, sub):
#         self.sno = sno
#         self.sname = sname
#         self.sub = sub
#
# student1 = Student(1, "Ramesh", "python")
# student2 = Student(2, "Suresh", "AI")
# print(student1.sno, student1.sname, student1.sub)
# print(student2.sno, student2.sname, student2.sub)

# 3. Calling constructor with parameter, correct way to create object for that class. Trainer
# should ask the code based question on this.

# 4. Can we remove self parameter from init

# False

# 5. Can we place x in place of self parameter in init

# True but not recommended

# 6. Can I overload constructor? What will happen if we overload constructor?

# class Patient:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = args[2]
#         elif len(args) == 2:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = None
#         elif len(args) == 1:
#             self.pno = args[0]
#             self.pname = None
#             self.disease = None
#         else:
#             self.pno = None
#             self.pname = None
#             self.disease = None
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating patient objects with different initialization scenarios
# patient1 = Patient(1, "Ramesh", "Fever")
# patient2 = Patient(2, "Suresh")
# patient3 = Patient(3)
# patient4 = Patient()

# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()
# print()  # Just to add a line break between the outputs
# patient3.display_info()
# print()  # Just to add a line break between the outputs
# patient4.display_info()


# class Patient:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = args[2]
#         elif len(args) == 2:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = None
#         elif len(args) == 1:
#             self.pno = args[0]
#             self.pname = None
#             self.disease = None
#         else:
#             self.pno = None
#             self.pname = None
#             self.disease = None
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating patient objects with different initialization scenarios
# patient1 = Patient(1, "Ramesh", "Fever")
# patient2 = Patient(2, "Suresh")
# patient3 = Patient(3)
# patient4 = Patient()
#
# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()
# print()  # Just to add a line break between the outputs
# patient3.display_info()
# print()  # Just to add a line break between the outputs
# patient4.display_info()


# 7. Can we create object without calling constructor

# You can use object.__new__ to create an instance without invoking the __init__ method.
# This method is lower-level and is used to allocate memory for a new instance without initializing it.

# class Patient:
#     def __init__(self, pno, pname, disease):
#         print("Initializing...")
#         self.pno = pno
#         self.pname = pname
#         self.disease = disease
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Create an object without calling the __init__ method
# patient = object.__new__(Patient)
#
# # Manually setting attributes
# patient.pno = 1
# patient.pname = "Ramesh"
# patient.disease = "Fever"
#
# # Displaying the information of the patient
# patient.display_info()


# 8. What is the sequence of object creation and constructor call?

# In Python, the sequence of object creation and constructor call involves several steps,
# primarily handled by two special methods: __new__ and __init__. Here's a detailed explanation of the sequence:
#
# Sequence of Object Creation and Constructor Call
# Object Creation (__new__ method):
#
# The __new__ method is the first step in the object creation process.
# It is responsible for creating a new instance of the class.
# __new__ is a static method that takes the class as its first argument,
# followed by any additional arguments that will be passed to the __init__ method.
# __new__ returns a new instance of the class.
# Object Initialization (__init__ method):
#
# After __new__ creates the instance, the __init__ method is called to initialize the instance.
# __init__ is an instance method that takes the newly created instance as its first argument (conventionally named self),
# followed by any additional arguments passed to the constructor.
# __init__ does not return anything; it modifies the instance in place.
# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         print("Creating instance (calling __new__)")
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self, value):
#         print("Initializing instance (calling __init__)")
#         self.value = value
#
#     def display_value(self):
#         print(f"Value: {self.value}")
#
# # Creating an instance of MyClass
# obj = MyClass(10)
#
# # Displaying the value
# obj.display_value()

# 9. Can we call a constructor after creating an object?

# In Python, the constructor (__init__ method) is called automatically when a new instance of a class is created.
# Once an object is created, calling the constructor directly in the same way as during object creation is not possible.
# However, there are a few ways to achieve similar functionality:

# class MyClass:
#     def __init__(self, value):
#         print("Initializing instance")
#         self.value = value
#
#     def display_value(self):
#         print(f"Value: {self.value}")
#
# # Creating an instance of MyClass
# obj = MyClass(10)
# obj.display_value()
#
# # Reinitializing the same instance
# obj.__init__(20)
# obj.display_value()


# 10. For one object how many times will the constructor be called? Can we call a constructor multiple times for one object?

# In Python, the constructor (__init__ method) is called automatically when an object is created.
# For one object, the constructor is called exactly once during the object's creation.
# Once the object has been created, the constructor is not called again automatically for that object.
# However, you can manually call the __init__ method on an existing object,
# but this is not the same as creating the object again; it is just a method call that can reinitialize the object's attributes.

# 11. Is it mandatory for every class to have constructor

# No, it is not mandatory for every class to have a constructor (__init__ method) in Python.
# If you don't explicitly define a constructor in your class, Python provides a default constructor for you.
# Default Constructor
# If you don't define a constructor in your class, Python automatically provides a default constructor.
# This default constructor doesn't do anything beyond what's necessary to create an instance of the class.

# 12. If we create 10 objects for a class, how many times will the constructor be called?

# If you create 10 objects for a class in Python, the constructor (__init__ method) will be called exactly 10 times,
# once for each object being created.

# class MyClass:
#     def __init__(self, value):
#         print("Constructor called with value:", value)
#         self.value = value
#
# # Creating 10 objects of MyClass
# objects = [MyClass(i) for i in range(10)]

# *******************************************   Encapsulation   **************************************************

# 1. Give one example where you have used encapsulation. (students must explain an example).

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self._balance = balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount} into account {self.account_number}")
#         else:
#             print("Invalid deposit amount")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew {amount} from account {self.account_number}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount")
#
#     def get_balance(self):
#         return self._balance
#
#
# # Creating a bank account object
# account1 = BankAccount("12345")
#
# # Depositing and withdrawing money
# account1.deposit(1000)
# account1.withdraw(500)
#
# # Accessing balance using the getter method
# print("Account balance:", account1.get_balance())


# 2. What is the advantage of using encapsulation self and super:

# Encapsulation

# Data Hiding:
# Encapsulation allows you to hide the internal state of an object and restrict direct access to its attributes from outside the class.
# This prevents accidental modification of the object's state and helps maintain data integrity.

# Abstraction:
# By exposing only the necessary functionality through methods,
# encapsulation allows you to abstract away the implementation details of a class.
# Users of the class interact with its public interface without needing to know how it's implemented internally.

# Modularity:
# Encapsulation promotes modularity by grouping related data and behavior into a single unit (class).
# This makes it easier to understand, maintain, and reuse code.

# self

# Instance Reference:
# In Python, self is used inside instance methods to refer to the instance (object) itself.
# It allows you to access the object's attributes and methods within the class definition.

# Instance-specific Operations:
# Using self, you can perform operations on instance variables,
# allowing each instance to have its own state and behavior.
# This is crucial for creating multiple objects with different characteristics based on the same class definition.

# super

# Parent Class Access:
# super allows you to call methods from the superclass (parent class) within a subclass (child class).
# This is useful when you want to extend or override methods inherited from the parent class while still maintaining their original behavior.

# Method Resolution Order (MRO):
# super helps ensure that methods are called in the correct order in the class hierarchy.
# It follows the Method Resolution Order defined by the C3 linearization algorithm,
# ensuring that methods are resolved consistently across the inheritance chain.

# Advantages of Using Encapsulation, self, and super

# Code Organization: Encapsulation, self, and super help organize code into logical units (classes and methods),
# making it easier to understand and maintain.

# Code Reusability: Encapsulation allows you to create reusable class definitions with well-defined interfaces.
# self enables the creation of reusable instance methods that operate on instance-specific data.
# super facilitates code reuse by allowing subclasses to extend or override behavior inherited from parent classes.

# Data Integrity:
# Encapsulation prevents accidental modification of object state by restricting direct access to attributes.
# This helps maintain data integrity and reduces the risk of bugs caused by unexpected changes to object state.
# Inheritance and Polymorphism: self and super are essential for implementing inheritance and polymorphism in Python.
# They allow you to create class hierarchies and implement subclass-specific behavior while leveraging code from parent classes.

# *************************************   self and super   ****************************************

# 1. What exactly does self contain?

# Instance Attributes:
# self contains all the instance attributes of the class.
# These attributes define the state of each individual object created from the class.

# Instance Methods:
# self allows access to instance methods within the class.
# These methods can operate on the instance's attributes and perform various actions based on the object's state.

# Instance-specific Operations:
# self enables instance-specific operations, meaning each instance of the class can have its own distinct data and behavior.
# Methods defined using self can access and modify instance attributes, allowing for customized behavior based on the object's state.

# 2. Trainer can ask any code on find output on self() or super() Inheritance:

# ***********************************    Inheritance   *******************************************

# 1. In the inheritance, if we create an object for child class, which class constructor will be called?

# When an object of the child class is created in an inheritance scenario,
# the constructor of the child class is called first. However, if the child class's constructor uses super().__init__(),
# the constructor of the parent class will also be called

# 2. How do you call a parent class constructor which has parameter x from the child class constructor, show code.

# class Parent:
#     def __init__(self, x):
#         self.x = x
#         print(f"Parent class constructor called with x = {x}")

# class Child(Parent):
#     def __init__(self, x, y):
#         super().__init__(x)  # Call the parent class constructor with parameter x
#         self.y = y
#         print(f"Child class constructor called with y = {y}")

# # Create an object of the Child class
# child = Child(10, 20)


# 3. How do you call a parent class constructor which does not have parameters from the child class constructor, show code.

# 4. How do you call parent class methods from child class? Show code

# 5. How do we access the parent class self.x variable in child class methods? Show code

# 6. Can we access parent class instance variables with child class object? Show code

# 7. Can we access parent class methods with child class object? Show code

# 8. Show eg for multiple inheritance

# 9. How many types of inheritances supported in python

# 10. What is function ambiguity, show code. Which class method will be executed in case of function ambiguity

# *****************************************   Types of variables   ************************************************

# 1. Trainer can ask code to find output or find error while printing local variables and global variables.

# 2. Trainer can ask code to find output or find error while printing instance variables and class variables.

# 3. Can we access class variables with self or object?

# 4. Can we access instance variables with class name?

# 5. Which variables are shared among all objects of the same class?

# 6. Which variables are present as separate copy in every object?

# 7. Which variables are created only once?

# ******************************************   Types of methods   *********************************************

# 1. Trainer can ask code on find output or find error on calling instance methods, static methods and class methods

# 2. Trainer can ask how to call different methods code

# 3. Can we access instance variables inside a class method?

# 4. Can we access instance variables inside a static method/

# 5. Can we access class variables inside an instance method?

# 6. Can we call class method with object

# 7. Can we call static method with object

# 8. What is the difference between static method and class method?

# 9. Instance method or class method, which one is faster?

# ************************************************   Split or join    ***************************************
# 1. Trainer can ask any coding find output related question on split() join()

# 2. X = ‘a,b,c,d’ store these elements into a list using split()

# 3. X = ‘py#palle#banglore’ store py, palle, bangalore into a list

# 4. X = ‘palle py bangalore’. Store these three words into a list

# 5. If i want to split a word based on spaces is it mandatory to pass the separator?

# 6. What is the return type of split() function.

# 7. X = (‘palle’, ‘py’) join these 2 words into a string and print

# 8. X = [‘palle’,’py’] i want to store palle#py into a string how will you do it

# 9. x = [‘p’,’a’,’l’] res=’*’.join(x) print(res) find output

# ***********************************************    Exceptions   ********************************************
# 1. Write one e.g. for exceptions with files. Open a file in c: and write ‘hi’ into the file.
# How will you handle permission error if O.S is not allowing to create file.

# 2. Write one e.g. for exceptions with files. Open a file in h: drive. Assume that h: drive is not there which exception will be thrown?
# How will you handle that exception?

# 3. Write one e.g. for exceptions with files. Open an existing file from d: drive and print all
# the lines present in that file. Which exception do you need to handle?

# 4. What happens if we don't handle an exception

# 5. If an exception occurs in try block, and if we are handling that except block, will the
# remaining lines of the try block be executed?

# 6. If an exception occurs in the except block, will it execute the remaining lines of the except block?

# 7. If an exception occurs in the finally block, will it execute the finally block completely?

# 8. Can i use try-except inside try (is nested try blocks allowed)

# 9. Can i use try-except inside except block

# 10. Can i use try-except inside finally block

# 11. If there is an exception in the try block, and if we are not handling that exception,
# in that case the finally block will be executed or not?

# 12. If an exception occurs in the try block, and we are handling a different exception in the
# except block what will happen?

# 13. Can one try block can have multiple except blocks?

# 14. Is it possible to have a try without except block?

# 15. How will you handle generic exceptions?

# 16. Show code for finally block with files example. Students must write code for reading
# content from a file and close the file in the finally block.

# *************************************************      Re     **********************************************

# ^ - starting
# $ - ending
# + - 1 or more
# * - 0 or more
# ? - 0 or 1
# . - any character
# [ ] - set of letters
# 1. Write code to find if a given text starts with word palle

# 2. Write code to find if a given text ends with word python

# 3. Write code to find if a given text starts with palle and ends with python and in between 0 or more letters

# 4. Find how many digits are there in a given text

# 5. Find how many small letters are there and how many capital letters are there in a given text

# 6. In a given text print all words starting with he and ending with o, and in the middle it has 1 or more letters.

# 7. search for a sequence that starts with "he", followed by 0 or more (any) characters, and ends with "o":
# print all those words from a given text

# s = "jagAJHfgdfhgGBNHfGJjaga"
# ucount = 0
# lcount = 0
# upper = []
# lower = []
# for x in s:
#     if x.isupper():
#         ucount+=1
#         upper.append(x)
#     elif x.islower():
#         lcount+=1
#         lower.append(x)
# print(upper)
# print(lower)
# print(ucount)
# print(lcount)

# l1 = [1,2,3,4]
# l2 = ["one","Two","Three"]
# result = dict(zip(l1,l2))
# print(result)
# r1 = result.keys()
# r2 = result.values()
# print(list(r1))
# print(list(r2))





