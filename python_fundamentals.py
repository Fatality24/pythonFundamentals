# Python is an interpreted progamming language, object oriented, for general use 

# In an interpreted programming language - the code is read line with line 
#                                        - slower performance 
#                                        - easier to create and test 


# In python the source code is transformed to bytecode then runned by Python Virtual Machine 

# file.py (source) ---> file.pyc (bytecode) ---> PVM (RUNTIME)


USE_CASES = {
    'DATA_SCIENCE' :'Data science',

    'MACHINE_LEARNING' : 'Machine learning',

    'SYSTEM_ADMINISTRATION' : 'System Administration',

    'DESKTOP_APPLICATIONS' : 'Desktopo Applications',

    'WEB_DEVELOPMENT' : 'Web Development',

    'WEB_CRAWLING' : 'Web Crawling',

    'TESTING' : 'Testing',

    'HACKING' : 'Hacking'
}

# arg comes from arguments 

# kargs comes from key arguments 


# Python follows the same mathematical principles 

sum = 3 + 5
print(sum)
# it will print 8 


multiplication = 10 * 20 
print(multiplication)
# it will print 200


power = 10**2
print(power)
# it will print 10


equation = 5*(2+3) + 10
print(equation)
# it will print 35 


x = 74 % 10
print(x)
# print the remainder, modulo takes the remainder


y = 74 / 10 
print(y)
# print 7.4

z = 74//10
print(z)
# print 7


# There are special parameters asigned in .math 

# Built in parameter in sum()
# Exemple of normal sum()
lst = (1,2,3,4,5)
print(sum(lst)) # 15

#Exemple of sum() with second parameter
# the second parameter 100 makes the sum start from there 

lst = (10,20,30)
print(sum(lst, 100)) # 160


# Function exemple
def sum_of_numbers(*lst, start_ahead= 100):
    for item in lst:
        start_ahead+= item 
    return start_ahead

print(sum_of_numbers(20,30,40,40,start_ahead=50))



# if STATEMENT 
x = True
if x :
    print("condition is true")
    if 10 > 9:
        print("condition is true asked again")
        if 5 < 1:
            print("this statement is true")
        else:
            print("the statement is not true")
else:
    print("condition is not true")

# It will print --->
#condition is true
#condition is true asked again
#the statement is not true

x = False

# It will print --->
# condition is not true



PYTHON_DATA_TYPES = {
    'Integer': [1, 2, 3, 4], # Here you also have Complex and Float
    'Bool': [True, False], # True is mapped to 1 and False to 0 
    'String' : 'This is a string'
    'BinaryTypes' ,# [memoryview, bytearray, bytes]
    'SetTypes' : [frozenset, set],
    'MappingType': dict,
    'SequanceType': [range, tuple, list]
}


LOOGIC_OPERATORS = {
    "or" : "the right side or left side needs to be true",
    "and" : "both sides have to be true",
    "not": "True transforms to False and vice-versa"
}


# TUPLE 

# Tuple is imuttable, that means I cannot .append

tuple = (1,2,3)
print(tuple[0])   #----> the index always starts from 0 
print(tuple)
# it will print 1 because of the index 0 there is the value 1 

print(len(tuple)) # if i print the lenght of the tuple == 3, because there are 3 indexes



# LIST

# LIST is muttable, I can .append it and do alterations to it 

list = [1,2,3,4]

print(len(list))   # ---> the lenght is 4, because there are 4 indexes(0,1,2,3) 
print(list[0])     # ---> the print will show the index of 0, which is 1 

list.append(5)    # ----> In a muttable list I can alter the list 
list.append(True) # ----> I can ADD anything to a list 



# LIST functions 

list_name  = [ ]

list_name.append(10)

new_item = "new_item"
list_name.insert(0, new_item)

list_name.pop() #NOTE  pop() will always "pop" the last element 

len(list_name) # returns the number of items 

list_name.clear()

list_name.sort() 



# LIST exercise

# The program asks the user to enter a number. As long as the user enters numeric values, the program collects them.
# When the user presses the Enter key instead of a numeric value,the program lists the sum of the numbers and starts from new assembly.
# If the user enters a value not suported, a message is listed and the next insertion is taken.

list = [0,]
start = input("Wanna start the program?")
while start:
    nr = input("enter number")
    if nr.isdecimal():
        nr = int(nr)
        list.append(nr)
    elif nr == " ":
        print("You pressed space, here is your sum", list[-1] + list[-2],  " \n if you wanna exit type exit")
    elif nr == "exit":
        start = 0
    else:
        continue

        

# LIST exercise

# There is a list of numbers and 2 empty lists, put the odd and even numbers separatly

list = [4567, 678, 24, 55, 9, 5678, 90, 89]

odd = [ ]

even = [ ]

for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("odd = " ,odd)
print("even = " ,even)



# STRING 

# STRING are immutable, you cannot add to them, you have to rewrite them 

string = "thisisastring"

print(string[0])  # ----> I can see the indexes

print(len(string)) # ----> It prints the lenght of my string (0-1-2-3-4-5-6-7-8-9-10-11-12) which is 13 



# THIS IS IMMUTABLE 
a = "123456"
a += "7"
print(a)

# THIS IS MUTABLE
b = [1,2,3,4,5,6]
b.append(7)
print(b)



# INDEXES 

# poisitive indexes start form 0 -----[0,1,2,3,4]
# negative indexes start form -1 -----[-4,-3,-2,-1]

fruits = ["fruits", "mango", "apples", "berries", "bananas"]
print(fruits[0])
# it will print the index of 0 --> fruits

fruits = ["fruits", "mango", "apples", "berries", "bananas"]
print(fruits[-1])
# it will print the index of -1  ---> bananas

fruits = ["fruits", "mango", "apples", "berries", "bananas"]
print(fruits[1:-1])
# it will print the index of 1 to -1  ---> ['mango', 'apples', 'berrys']

fruits = ["fruits", "mango", "apples", "berries", "bananas"]
print(fruits[-4:-1])
# it will print the index of -4 to -1  ---> ['mango', 'apples', 'berrys']

fruits = ["fruits", "mango", "apples", "berries", "bananas"]
print(fruits[-3:-2])
# it will print the index of -3 to -2  ---> ['apples']



# All the cases for indexes, they work for LIST AND TUPLE 

list = [1,2,3,4,5]
print(list[0])  # on the index 0 its the value 1 

list = [1,2,3,4,5]
print(list[-1])  # on the index -1 its the value 5

list = [1,2,3,4,5]
print(list[3])  # on the index 3 its the value 4

list = [1,2,3,4,5]
print(list[::])  # it prints the values of the whole index /// [1, 2, 3, 4, 5]

list = [1,2,3,4,5]
print(list[2:5])  # from the index 2 to the index 5 [3,4,5]

list = [1,2,3,4,5,6,7,8,9,10]
print(list[3:-2])  # from the index 3 to the index -2 // [4,5,6,7,8] //

list = [1,2,3,4,5]
print(list[-5:-2])  # from the index -5 to the index -2 // [1, 2, 3] //

list = [1,2,3,4,5,6,7]
print(list[:5])  # from the index 0 to the index 5 /// ":" is seen as 0 //// [1, 2, 3, 4, 5]

list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(list[::2])  # from the index 0 to the last with 2 breaking  /// [[1, 3, 5, 7, 9, 11, 13] /// 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list[::4])  # from the index 0 to the last with 4 breaking  /// [1, 5, 9, 13]/// 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list[::-1])  # from the last index to the first index   /// [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]/// 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list[::-2])  # from the last index to the first index with 2 breaking   /// [[15, 13, 11, 9, 7, 5, 3, 1]/// 





# RANGE 

x = range(4)
print(x)
# the range is (0,4)


x = range(0,4,1)  # ----> the range starts from 0 to 4 and breaks once 
print(x)
# the range is (0,4) ----> the range is the same but the paramenters are 3--(0,4,1)

x = range(0,25,2)
print(x)
# the range is (0,25,2) with a break from 2 in 2
for n in x:
    print(n)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24


x = range(-12,1)

for n in x:
    print(n)


x = range(-12,1,3)

for n in x:
    print(n)


# Exercise A with range(len())

# Two strings with members 1,2,3 and 4,5,6 are given.
# The third string that will contain the sum must be created from members of the two existing series.

a = [1,2,3]
b = [4,5,6]
c = [ ]

for i in range(len(a)):
    c.append(a[i] + b[i])
pass

print(c)

# NOTE with range(len()) you can iterate the indexes of a LIST



# Exercise B with range(len())

# Lists with x numbers are given 
# The last List that will contain the sum must be created from members of the x existing series.
# You can define your numbers of lists

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [10,11,12]
e = [13,14,15]
f = [16,17,18]
g = [19,20,21]
h = [22,23,24]
i = [25,26,27]
j = [28,29,30]
k = [31,32,33]
l = [34,35,36]

iterate = [ ]

for i in range(len(a)):   # NOTE You are actually accesing indexes 
    iterate.append( a[i] +b[i] +c[i] + d[i] +e[i] +f[i] +g[i] +h[i] +j[i] +k[i] +l[i]) # NOTE .append()
pass

print(iterate)


# Exercise C 

# Create a function() that renders a window based on lenght and width

#   $$$$$$$$$
#   $       $
#   $       $
#   $       $
#   $       $
#   $       $
#   $       $
#   $       $
#   $       $
#   $       $
#   $$$$$$$$$
       
def function(width,height,symbol):
    print(symbol * width)
    for i in range(height):
        the_empty_space = width - 2
        height = symbol + " " * the_empty_space  + symbol
        print(height)
    print(symbol * width)


function(10,10,"A")
function(100,100,"%")




# Tuple list with range 

tuple_list = (200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900, True, False, "TEST", 3.14)

print(tuple_list[-6:-1]) # the two points(:) between the range are called a SLICE ----> it will print (1800, 1900, True, False, 'TEST')

print(tuple_list[5:-4]) # (700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900)

print(tuple_list[-7:-4]) # (1700, 1800, 1900)

print(tuple_list[::2]) # (200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, True,'TEST')

# I CAN REVERSE IT 

print(tuple_list[::-1]) # (3.14, 'TEST', False, True, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200)

print(tuple_list[::-2]) # (3.14, False, 1900, 1700, 1500, 1300, 1100, 900, 700, 500, 300)  BUT REVERSE 




# STRING functions

x = "This is an exemple of a string with 24 , True, False, 3.14 and so o^&*() on xxx"

print(list(x)) # ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', 'n', ' ', 'e', 'x', 'e', 'm', 'p', 'l', 'e', ' ', 'o', 'f', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 'w', 'i', 't', 'h', ' ', '2', '4', ' ', ',', ' ', 'T', 'r', 'u', 'e', ',', ' ', 'F', 'a', 'l', 's', 'e', ',', ' ', '3', '.', '1', '4', ' ', 'a', 'n', 'd', ' ', 's', 'o', ' ', 'o', '^', '&', '*', '(', ')', ' ', 'o', 'n', ' ', 'x', 'x', 'x']
print(x.isnumeric()) # False 
print(x.lower()) # this is an exemple of a string with 24 , true, false, 3.14 and so o^&*() on xxx
print(x.count("x")) # 4
print(x.index("x")) # at the index 12 there is "x"
print(x.replace(" ","")) # Thisisanexempleofastringwith24,True,False,3.14andsoo^&*()onxxx
print(x.split("h")) # ['T', 'is is an exemple of a string wit', ' 24 , True, False, 3.14 and so o^&*() on xxx']
print(len(x)) # 79 The lenght of the string 
print(x.isalpha()) # if the characters are from the alphabet returns True if not returns False 


# sep= "%%%%" , end="******"
print("Santa", "Claus", "and",  "his", "friends",sep="%%%%%", end="*********") 
# Santa%%%%%Claus%%%%%and%%%%%his%%%%%friends*********% 




# SET 

# SET is a sequance with UNIQOE characters 

a = {1}
print(type(a)) # class set

sequence = "1234555667779999","radu", "rrrrr", 9, "9", 77, "77", "77"   # SET has always comma(,) between them. If it has two points(:) its DICT 
print(set(sequence))
# {'77', 'rrrrr', '1234555667779999', 9, 77, 'radu', '9'}

sequence1 = "1112222333334444"
print(set(sequence1))
# {'3', '4', '2', '1'}



# Find the smallest number and the biggest number from an unsorted list

l = [23,4,56, 67, 8934, 433, 342]

print(max(l))
print(min(l))

l2 = [23,4,56, 67, 8934, 433, 342,34,1,42,0,23]

sorted = set(l2)
print(sorted)

sorted.add(24)
print(sorted)

sorted.update([0],{24444444})
print(sorted)

sorted.remove(0)
print(sorted)



# UNION OF SETS 
A = {1,2,3,4,5,6,7,8}

B = {9,10,11,12,13,14,15}

print(A | B)         # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(A.union(B))    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# INTERSACTIONS OF SETS 

C = {100,101,102,103,104}

D = {103,104,105,106,107}

print(C & D) # {104, 103}
print(C.intersection(D)) # {104, 103}


# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)




# DICT

# The key has to be always UNIQUE, IF YOU REPET THE KEY it will always access the last one writed !

variable_test = "test"
variable_test2 = ("i can put whatever i want here", 12, 45, )

dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": True,
    "key5": False,
    "key6": 2435,
    "key7": 78.98,
    "key8": variable_test,
    "key9": [1,2,3,4,5, True, False],
    "key10": (1,2,3,4,True,False, 3.14),
    "key11": {
        "dictionary2" :{
            "key1.0": "value1.0",
            "key2.0": "value2.0",
            "key3.0": "value3.0",
            "key4.0": True,
            "key5.0": False,
            "key6.0": 2435,
            "key7.0": 78.98,
            "key8.0": variable_test2,

        },
    },

}


print(dictionary["key1"])        # a DICT will always be accese by the key  ---- value1

print(dictionary["key11"]["dictionary2"]["key6.0"])  # I can go as long as i need in the DICT to reach my value ----- 2435




# Changing a value from a key 

x = {"cars": 2, "moto":3, "bicycle":6}
print(x) # {'cars': 2, 'moto': 3, 'bicycle': 6}

x["cars"] = 4
print(x) # {'cars': 4, 'moto': 3, 'bicycle': 6}


print(len(x))
# the lenght of x is 3, there are 3 pairs of key:values 




# Practical exemple of the DICT 

languages = {
    "Ro" : "Ati ales Limba Romana",
    "En" : "English is your selection",
    "Du" : "Sie haben Deutsch gewahlt"
}

choose_language = input("What language do you prefer?")

if choose_language in languages:
    print(languages[choose_language])

# For each key("Ro", "En", "Du") we have a value that we can access


# FUNCTIONS 


def function(parametre, second_parametre): # Here I declare the function with 2 parameters
    print(parametre + second_parametre)   

function(5,6)  # 11     
function("5","6") # 56
function(True,5) # 6
function(True,False) # 1


def return_test(x,y):  # with the return keyword you assign the function with the result
    return x * y

def print_test(x,y):  # here you only print the result 
    print(x + y)

m = return_test(4,5) # you can create a variable to assign the result of the function
print(m)       # you can print the variable assigned to the called function
print(type(m)) # <class 'int'>

print_test(5,9) # here you only call the function, returning print(x + y)
print(type(print_test)) # <class 'function'>



# FIRST CLASS FUNCTION 

def myfunction(f):   # I assign a function as a parameter to another function 
    f("hello world")

myfunction(print)     # In this case I assign the print function 
# hello world 


def my_second_func(i):
    i("enter a word")

my_second_func(input) # In this case I assign the input function 
# enter a word --> (your word here)



# Simple definition 

x = print
x("hello world") # hello world 

y = input
y("enter the word you want to store in y") #enter the word you want to store in y



# Exemples of FIRST CLASS FUNCTIONS 


def shout(text):         # here I pass a string to my function as a paramter 
    return text.upper()  # here I return the string.upper()

def whisper(text):        # here I pass a string to my function as a paramter 
    return text.lower()   # here I return the string.lower()

def greet(func,message):  # here I pass a function to my parameter and the message i want to process in the function 
    return func(message)


print(shout("radu"))         #RADU     # shout will make my text.UPPER() 
print(whisper("RADU"))       #radu     # whisper will make my text.lower() 
print(greet(shout, "radu"))  #RADU     # here i pass the function shout as a parameter and the message I want to process 



# Exercise with FIRST CLASS FUNCTION 

# Calculate the gross salary and the net salary 


def net_salary(salary):
    return salary - 45 * salary/ 100 

def gross_salary(salary):
    return salary + 65 * salary/ 100 

def salary_calculation(function, salary):
    return function(salary)


print(salary_calculation(net_salary, 1000))    #  550.0
print(salary_calculation(gross_salary, 1000))  #  1650.0

# I can even iterate in them
methods_of_calcul = (net_salary, gross_salary)   # I assign them to a list 
for method in methods_of_calcul:                 # I iterate 
    print(salary_calculation(method, 1000))      # I print the function iterated from all the methods declared 


# UNPACKING 

x,y,z = 0,1,2

print(x) #0
print(y) #1
print(z) #2

def return_two_values(x,y):
    return x * 2, y * 2
x, y = return_two_values(3,4)  # Unpacking the values if i need them as  <class 'int'>
print(x) # 6 
print(y) # 8 
print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>



def return_other_two_values(x,y): 
    return x * 5, y * 5 
print(return_other_two_values(3,4))    # (15, 20) 
print(type(return_other_two_values(3,4))) # <class 'tuple'>


# Function in a function 

def error_message():       # I can create a function to be called by other functions 
    print("error message, division by 0 is not possible")


def division(a,b):
    if b == 0:
        error_message()  # here i call my function()
    else:
        print(a // b)



division(5,0)  # error message, division by 0 is not possible



# Recursive function 

def function(x):
    print(x)
    x -= 1
    if x > 0:
        function(x)   # the function is called inside the function making recursion 


function(5)
#1
#2
#3
#4
#5


# Factorial 

def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n-1)


print(factorial(4)) # 24




# Function overwriting

def function(a, b = 78, c = True): # I can alocate function parameters from the definition 
    return a + b + c 

x = function(3,4,5)  # I can overwrite the parameters
print(x)  # 12 (3 + 4 + 5) 

y = function(4) # I can call the function only with the parameter I need 
print(y) # 83 (4 + 78 + 1 )


# Anoter function exemple of overwriting 

def function(a=8 , b=2, c=4):
    print(a,b,c)

function(c = 6, b = 9, a = 38)  # I can overwirte and assign as I want 


# Another function exemple

def this_is():
    return('this is the sum')

def the_sum(x,y):
   return(x + y)

print(this_is(), the_sum(5,6)) # this is the sum 11



# Lambda / Anonymous function 
# Lambda is a function used in very little scopes

func2 = lambda x,y : x + y

func3 = lambda x,y,z : max(x,y,z)

x = lambda a : a*30

print(func2(3,4)) # 7
print(func3(100,200,300)) #300
print(x(11)) # 330





# Exercise 1

# Check if list contains an integer, use a function 

def check_if_x_exist(x, lst):  
    if x in lst:
        print("the value is in the list")
    else:
        print("the value is not in the list")

check_if_x_exist(3, [1,2,3])  # the value is in the list


# Exercise 2

# Check if list contains an integer, use a function 

def check(x, y):
    if x in y:
        print("its in the list ")
    else:
        print("its not in the list")


check(3, (1,2,3,4))  # y becomes a tuple 

check(3, [1,2,3]) # y becomes a list 

check(3, {3: "radu"})  # y becomes a key in a dict 



# Check if the word is palindrom 

# Def: palindrom is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurse terrun.

def palindrom(parametre1):
    if parametre1 == parametre1[::-1]:
        print("its palindrom")
    else:
        print("its not")

palindrom("caiac")  # its palindrom 
palindrom("crred")  # its not 



# Check if a word is an anagram

# Def: Anagram is a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

x = "ola"
x1 = "lao"
x2 = "alo"

def is_anagram(param1, param2):
    if set(param1) == set(param2):
        print("is anagram")
    else:
        print("its not")

is_anagram(x,x1)




# Mapping

# Python program to demonstrate working of map

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))    # [2, 4, 6, 8]



# Second exemple 

# We map how many values we want to a function 

def addition(x,y,z,k):     # FUNCTIONS
    return x + y + z + k

def subtraction(x,y,z,k):
    return x - y - z - k

def multiplication(x,y,z,k):
    return x * y * z * k

def division(x,y,z,k):
    return x / y / z / k


numbers_for_x = (1,2,3,4,5,6)                   # NUMBERS WE MAP 
numbers_for_y = (10,20,30,40,50,60)
numbers_for_z = (100,200,300,400,500,600)
numbers_for_k = (1000,2000,3000,4000,5000,6000)

add = map(addition,numbers_for_x,numbers_for_y,numbers_for_z,numbers_for_k)     # Mapping the function with the numbers  
sub = map(subtraction,numbers_for_x,numbers_for_y,numbers_for_z,numbers_for_k)
mul = map(multiplication,numbers_for_x,numbers_for_y,numbers_for_z,numbers_for_k)
div = map(division,numbers_for_x,numbers_for_y,numbers_for_z,numbers_for_k)

print(tuple(add))                                                                   # Printing the results 
print(tuple(sub))
print(tuple(mul))
print(tuple(div))



# Stringify 
# Transform an int to str 

# Version 1
l = [1,2,3,4,5]
l_stringify = []

for item in l:
    l_stringify.append(str(item))
print(l_stringify)


# Version 2 

l2 = [1,2,3,4,5]

def stringify(item):
    return str(item)

print(list(map(stringify,l2)))


# Version 3 

l3 = [1,2,4,5,6,7]
print(list(map(lambda x: str(x),l3)))

# I can also use .filter to put obligations 
print(list(map(lambda x: str(x),l3))) # ['1', '2', '4', '5', '6', '7']
print(list(map(lambda x: x > 3  ,l3))) # [False, False, True, True, True, True]
print(list(filter(lambda x: x > 3  ,l3)))  # [4, 5, 6, 7]



# Arbitrarily parameters in functions 

# when I use the * in front of the parameter I already assign a tuple 
# arbitararily parameters are always last declared 

def test(*parameters):
    print(parameters)
    for item in parameters:
        print(item)

test("radu", "mircea", "ioan", "costel")
# ('radu', 'mircea', 'ioan', 'costel')
# radu
# mircea
# ioan
# costel


# ** is dict
def parameters_again(*p1, **parameters):
    print(p1, parameters)

parameters_again("Radu", "mircea", "albert",house="radu", house1="mircea")
# the first parameters are assigned to a tuple and the rest to a dict 
# ('Radu', 'mircea', 'albert') {'house': 'radu', 'house1': 'mircea'}


def function_test(p1,*parameters):
    print(parameters)

function_test("santa","claus","and","his","friends")
# ('claus', 'and', 'his', 'friends')
# "santa" becomes hard assigned to p1

function_test("radu")
# "radu " becomes hard assigned to p1 and the * remain empty 
# ()


def function_test2(p1,p2,p3,*parameters):
    print(parameters)

function_test2("radu","mircea","costel","alex","angelo")
# p1,p2,p3 are hard assigned and the rest go to a tuple 
# radu mircea costel ('alex', 'angelo')



def function_test2(p1,p2,p3,*parameters):
    print(p1,p2,p3,parameters)

function_test2("radu","mircea","costel","alex","angelo")
# radu mircea costel ('alex', 'angelo')


# as a note this is not necessarily wrong 
def parameters_again(p1,p2):
    print(p1, p2)

parameters_again((2,3,45,6),{"key":"value"})
# (2, 3, 45, 6) {'key': 'value'}


# One function with all type of parameters(values, tuple, dict)

def function_parameters_again(p1,p2,*parameters, **parameters2):
    print(p1)
    print(p2)
    print(parameters[0])
    print(parameters[1])
    print(parameters2["key"])



function_parameters_again(
    "this is p1", 
    "this is p2",
    "this is the 0 index fropm list",
    "this is the 1 index from list",
    key="this is the value of the key"
)

# this is p2
# this is p1
# this is the 0 index fropm list
# this is the 1 index from list
# this is the value of the key


# Exercise 
# Complete the function so that the sum of numbers to be equal 
# to n arbitary numbers


# easy way 
def suma1(*parameters):
    print(sum(parameters))

suma1(4,5,7,888,7)
# 911


# hard way 
def suma2(*parameters):
    suma = 0 
    for item in parameters:
        suma += item
    print(suma)

suma2(2,3,4,32,1,3)
# 45 


# Exercise 2
# Complete the function so that the sum or the prod of numbers to be equal 
# to n arbitary numbers

from math import *
def suma_prod(operation,*numbers):
    if operation == "+":
        print(sum(numbers))
    elif operation == "*":
        print(prod(numbers))
    else:
        print("only sum and prod accepted")


suma_prod("+", 5,3) # 8
suma_prod("*", 2,3) # 6



# I can make operations with functions 

def function1(n1,n2):
    return n1 * n2

def function2(n1,n2):
    return n1 - n2

def function3(n1,n2):
    return n1 + n2

result = function1(3,3) + function2(5,3) + function3(3,4)

print(result) # 18



# Another exemple of a function with arbitary parameters 

def fun(*par1,**par2):
    print(par1)
    print("par2",par2)
    return (min(par1)+min(par1))/2

print(fun(213,312,31,2,key="value"))

# (213, 312, 31, 2)
# par2 {'key': 'value'}
# 2.0







# Additional exercises 

# Create the following program 
# Enter the brute_salary, enter if the salary is from an it_employee or a part_time_employee
# Calculate the net_salary for a normal employee, where the taxes are 45%
# For iT , the taxes are 10% smaller
# for parti_time, they have a tax exemption of 5%


x = int(input("how many gb your hard_drive has"))
hard_drive = 1024
my_hard_drive = x * hard_drive



picture = 3
video = 15

client_pic = input("how many pictures do you need to install?")
if client_pic == " ":
    client_pic = 0
else:
    client_pic = int(client_pic)





client_video = input("ho wmany videos do you need to install?")
if client_video == " ":
    client_video = 0
else:
    client_video = int(client_video)

free_space = my_hard_drive - ((picture * client_pic) + (video * client_video))
print(free_space)





















