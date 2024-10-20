"""
comments :

    1. inline comments  - #
    2. Multiline Comments - '''  '''

"""

# this inline comment

"""

this is for multiline
    in python
"""

# variables :

# storing data values

x = 5

# varible names :

"""
    - must start with letters are underscore
    - cannot start with number
    - can contain letters, numbers, and underscore
    - cannot contain special characters[*,&,%] 
    - cannot be used  in any python keywords
"""
# example of variable names :

my_variable = 100
my_variable_1  = 200
my_variable_1_1 = 300

# 23_my_variable = 23 


# case Sensitive :

Name = "Vijay"
name = "AjithKumar"

NAME = "Silambarasan"
nAME = "Rajinikanth"

"""
print(Name)
print(name)
print(NAME)
print(nAME)
"""
# Multi Words variables Names :


UserfirstName = "GOAT"

"""
1. Camel Case
2. Pascal Case
3. Snake Case

"""

# Camel Case :

userFirstName = "VJ"

# Pascal Case :

UserMiddleName = "Sidhu"

# Snake Case :

User_Last_name = "VLOGS"


# Data Types :

"""


    1. Integer - int
    2. Float - float
    3. Complex - complex
    4. String - str
    5. Boolean - bool

"""

# Numeric Types :

"""

integer = 234 or 500

float = 234.56 or 768.95

complex = 3 + 4j



integer :

    integer is a whole number
    poisitive or negative
    without decimals
    unlimited Length

ex :

number = -5000

print(type(number))

-------------------------

float :

    float is a floating point number
    positive or negative
    with decimals
    unlimited length
    e - Scientific Numbers -> power 10 

ex :

# number = -23.459038438430247943657647564372567

number = 3e2 # 3 * 10 = 30 * 10 = 300 

print(number)
# print(type(number))

"""

# Complex :

"""
    - imaginary and real value part
    -'J' is a imaginary value

"""

# number = 4 + 6j

# print(type(number))

# imag

# print(number.imag)

# Real value :

# print(number.real)


# excer :

"""
Thala = 5 + 4j

Thalapathy = 4 + 5j


Thala_Thalapathy = Thala + Thalapathy


print(Thala_Thalapathy)

"""

# String : Text Data Type

"""
    str 

    Double quotes or single quotes

    Strings are arrays
"""

#          -4  -3  -2    -1  --> Negative index
# Movie = " G   O   A    T"
#           0   1   2    3   --> Poisitive index



# print(type(Movie))

# print(Movie)


# Thalapathy = "The Greatest of All Time"

# print(Thalapathy[-20])

# find out a string length :
"""
len() 

ex :

print(len(Thalapathy))

"""
# Thalapathy = "The Greatest of All Time"

# String Slicing : [start: end(n-1) :step]


"""
print(Thalapathy[0 : 3]) #[0 : (2-1) 1]

"""
# negative index Slicing :

# print(Thalapathy[-5:])

# print(Thalapathy[:20:3])



# String concatenation :

"""
    - We cannot Combine Strings & numbers
    - Only strings are concatenate


# Examples :

a = "CSK"

b = "Dhoni"

# c = 7 

Fav_player = a + " " + b

print(Fav_player)

"""

# String Modification :


"""
    - lower() -> Lowercase
    - upper() -> Uppercase
    - strip() -> Remove White Space
    - replace() -> Replace a String
    - split()  -> Split a String

"""
# Thalapathy = "   The Greatest of All Time   "

# Lower :

"""
lower_case = Thalapathy.lower()

print(lower_case)

# print(Thalapathy.lower())

"""

# Upper :

"""
upper_case = Thalapathy.upper()

print(upper_case)

"""

# Strip :

"""
 Remove White Space

ex :

print(Thalapathy)

print(Thalapathy.strip())

"""

# Replace :
"""

replace(old,new,count)


ex :

Thalapathy = "The Greatest of All Time"

x = Thalapathy.replace("Greatest","Ultimate")

print(x)

# Ex :2

Nature = "Hello World - this World is More Beautiful"

print(Nature.replace("World","Moon",1))


"""

# Split :

"""

split(separator,Maxsplit)

"""

"""
ex:
# Movie = "The Greatest of All Time"

# x = Movie.split()

# print(x)


x = "The Lion is Always Lion"

print(x.split(" ",3))

"""

# Format - String :

"""
format() :

- insert values into String

"""

Name = "Vijay"

Salary = 25000

office = "Google"


# txt = "My name is {2},and my salary is {0},and i'm working in {1}"


# print(txt.format(Salary,office,Name))
#                  0      1      2


# F-string :


"""
x = f"My name is {Name}, and i'm working in {office}"

print(x)

"""

# Boolean Type : bool()

"""
    True
    False

    
True Values in Python :

    any string is true - Except empty string
    any number is true - except 0
    any list ,tuple,set,dict - except empty

ex :

# print(bool(" "))

# print(bool(0))

print(bool([]))

"""

#Operators :

"""
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

"""

# Arithmetic Operators :

"""
Addition       =>  +

Subtraction    =>  -

Multiplication =>  *

Division        =>  /

Floor Division   =>  //

Modulus          =>  %

Exponentiation   =>  **

"""

"""
# Example :

a = 2

b = 3

print( a ** b )  # 2**3 ==> 2 * 2 * 2

"""


# Task :

"""
Number = 23 ,  34

-----


print(Number) 

# Output :  5   7

"""


# Assignment Operator :

"""
    =

    +=

    -=

    /=

    //=

    %=

    *=
"""

# Example :

"""

a = 5

a += 5  #  a = a + 5  =>  a = 5 + 5 = 10

print(a)

"""

# Comparison operator :

"""
    ==   =>  equal 

    !=   =>  Not equal

    >    =>  Greater than

    <    =>  Less than 

    >=   =>  Greater than or equal to

    <=   =>  Less than or equal to



a =  20

b =  20

# Example :

print( a <= b)

"""


# Logical Operator :

"""
    and

    or

    not

"""

#example :

CSK = 7

RCB = 18

# print( CSK == 45 and RCB == 18)

# print( CSK == 45 or RCB == 18)

# print( not RCB == 45)


# Identity Operator :

"""

is

is not

"""
#Example :

"""
a = ["vijay","Ajith"]

b = ["vijay","Ajith"]

c = a

print( c is a)

"""


# Membership Operator :

"""
in 

not in 

"""

# example :

"""
a = "Lion is always lion"


print("Lionking" not in a)

"""

# Bitwise Operator :

"""
    
    &  - and

    |  - or

    ^  - XOR

    ~  - NOT

    >> - Left shift

    << - Right shift

"""

#example :

# print( 6 & 2) 

"""

6 - 00000000110
2 - 00000000010
----------------
3 - 00000000011

"""

# User input and ouput :

"""
input()


name = input("Enter Your Name : ")

print(name)

"""

# Name Generator :

"""
first_name = input("Enter your First Name : ")

last_name  = input("Enter your Last Name : ")

UserName = first_name[0:3] + last_name[0:3]


print(UserName)
"""


# control flow statements :

"""
    1. Conditonal Statements 
    2. Loops
    3. Control transfer statements

""" 

# Conditional Statemnts :

"""
    1. if
    2. elif
    3. else

    
python syntax :

        indentation 

{

block of code

}

"""

# if statement :
"""

if condition is true then execute the block of code


syntax :

if condition :
    block of code

"""

# ex :

"""
rain = True

if rain == True:
    print("Your school is Leave")

"""

# if and else Statements :

"""
rain = False

if rain == True:
    print("Your school is Leave")

else:
    print("You will go to school")

    """


# if - elif - else Statements :

"""
if condition :
    block of code

elif Condition :
    block of code

elif Condition:
    block of code

else:
    block of code

"""

# Example :

"""

Marks = 85


if Marks > 90:
    print("Grade A")

elif Marks > 70:
    print("Grade B")

elif Marks > 60:
    print("Grade C")

elif Marks > 50:
    print("Grade D")

elif Marks >40:
    print("Grade F")

else:
    print("You are Fail")


"""

# Nested if Statements :

"""
if condition :
    if condition :
        block of code
    else:
        block of code
else :
    block of code

"""

# Example :

"""
name = "ajith"

age = 45

frequent_traveler = True

if age<18:

    if frequent_traveler:
        print("You have a child discount.!")

    else:
        print("You don't have a discount")

elif age >= 60:

    if frequent_traveler:
        print("You have a senior citizen discount.!")

    else:
        print("You don't have a discount")

else :

    print("You don't have valid discount")
"""

# looping Statements :

"""
    For Loop
    While Loop


# For loop :

syntax :

    for item in list_of_items:
        
        # Do somthing for each item

"""


# Example :

"""
Name = "Vikram"

# print(Name[0])
# print(Name[1])
# print(Name[2])



for i in Name:

    print(i) # V i k r a m

"""

# Range() :

"""
range(start,end(n-1),step)

default start value - 0

"""

# ex :


# for i in range(4): # 0 1 2 3
#     print(i)


# for i in range(1,10):

#     print(i)



# for i in range(1,10,2):
#     print(i) # 1 3 5 7 9


# Nested Loops :

# ex :

"""
for i in range(3): # 0 1 2

    for j in range(2): # 0 1

        print(f" i = {i} ==> j = {j}")  #(0,0 - 0,1) (1,0 - 1,1) (2,0 - 2,1)

"""

# while Loop :

"""

 - repeatedly executes a block of code as long as condition is true


 syntax :


    while Condition_is_True:
    
        # Do Something Repeatedly

"""

# Example :

"""
a = 1  # 2 3 4 5

while a < 5:

    print(a) # 1 2 3 4
    
    a += 1  # a = a + 1
    
"""

# Control Transfer Statements :

"""
    Break
    Continue
    Pass

"""

# Break :

"""

    Can stop the loop before it has finished.

"""

# break using For Loop :


"""
food = ["idly","pongal","poori","Dosa","vadai"]


for item in food:

    if item == "poori":
        break

    print(item)

"""


# break using while loop :


"""
 i = 1    # 2 3 4 5

while i < 10 :

    if i == 5:
        break

    print(i)  # 1 2 3 4

    i += 1    # 2 3 4 5

"""


# Continue :

"""
    - can skip the current iteration of the loop.
"""


# example :


# continue using For Loop :

"""
food = ["idly","pongal","poori","Dosa","vadai"]

for item in food:

    if item == "poori":
        continue

    print(item)

"""


# continue using While Loop :

"""
i = 0

while i < 10:

    i += 1

    if i % 2 == 0:
        continue

    print(i) # 1 3 5 7 9

"""

# Pass :

"""
    - does nothing.
    - it's like placeholder

"""

# example :

# pass uing for loop :

"""
food = ["idly","pongal","poori","Dosa","vadai"]

for item in food:
    pass

print("hi")

"""

# pass using while loop :

"""
i = 0  # 1 2 3 4 5


while i < 5 :

    if i == 3:
        pass  # no action

    else:
        print(i) # 0 1 2 4

    i += 1

"""

# difference between iterable and iteration and iterate :

"""
example :

number = [10,20,30,40,50]

    - the list is iterable

    - going through the list one by one is iteration

    - each step of going from one number to next is to iterate


""" 

# Pizza order and bill generation :


"""
small_pizza = 15

medium_pizza = 20

large_pizza = 25

# --------------------


add_pepper_small_pizza = 2

add_pepper_large_or_Medium_size = 3

add_Cheese_any_size = 1

#-----------------------


size = input("What size of Pizza Do you Want? [ S / M / L ] ")

add_pepper = input("Do you Want Pepper? [ Y / N ] ")

add_extra_cheese = input("Do you Want Extra Cheese? [ Y / N ] ")


bill = 0

if size == "S":

    bill += small_pizza

elif size == "M":

    bill += medium_pizza

elif size == "L":

    bill += large_pizza

else:

    print("Invalid Input")



if add_pepper == "Y":

    if size == "S":
        bill += add_pepper_small_pizza

    else:
        bill += add_pepper_large_or_Medium_size



if add_extra_cheese == "Y":

    bill += add_Cheese_any_size



print(f"Your final Bill is ${bill}")


"""


# Collections in Python :

"""

    1. List
    2. Tuple
    3. Set
    4. Dictionary
    
"""

# List :

"""

    Country = [ "London","Russia","USA","Germany", True ,23,56.78 ,["apple","orange"]]

    - Used to Store Mutiple items in single variable

    - List items are ordered

    - Changeable

    - Allow Dublicates

    - list items can be any data type

"""

"""
# Orederd :

1   2

3 4 5


a = [ "orange" , "mango" , "apple" ]

        0         1          2

        
# Changeable Means : - Mutable

    we can change,add,remove items in a list after it has been created
"""


# List constructor :

"""

list()


# Ex :

IPL = list(("CSK","MI","RCB","SRH","KKR"))


print(IPL)

print(type(IPL))


"""

# Access List items :

"""

    - using index to print the values
    
    - positive and negative indexing

    - index Slicing

#ex :

#      -5    -4    -3    -2    -1                         

IPL = ["CSK","MI","RCB","SRH","KKR"]

#        0     1    2      3    4


# print(IPL[2])

# print(IPL[-1])


# print(IPL[0 : 3])  #(0 , 3-1 = 2)

# print(IPL[1 : 4])  


# print(IPL[-3 : -1])  

"""

# Membership operator in List :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

print("SRH" in IPL)

"""

# Change List items :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]


IPL[-1] = "DC"

IPL[2 : 4] = ["LSG" , "GT"]

IPL[2 : 5] = ["LSG" , "GT"]

print(IPL)

"""

# Add list Item :


# insert(index,item) :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

IPL.insert(2,"GT")

print(IPL)

"""

# append(item) :

"""

    - is Used to add an element to the end of the list

syntax :

    list_name.append(element)


    list_name :

        list to which the element is added


    element :

        the item that you want to append to the list


    - this method adds a single element to the list

"""

#  ex :

"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

# IPL.append("DC")

IPL.append(["DC","LSG","GT"])

print(IPL)

"""



# Extend :

"""

    - is used to add all elements from an iterable to the end of the current list.


syntax :

    list_name.extend(iterable)


    list_name :

        the list that will be extended


    itereable : 

        whose elements will be added to the list

"""

# Example :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

IPL.extend(["DC","LSG","GT"])

print(IPL)

"""
# ----------------------------------

"""
x = ["a","b","c"]

y = "xyz"

x.extend(y)

print(x)

"""


# Remove List Items :

"""
    1. Remove
    2. Pop
    3. Del
    4. Clear

"""

# Remove :

"""
remove() :

    - remove the specified value

    - More than one item with specified value remove first occurrence.

syntax :

    list_name.remove(value)

"""
# Example :

"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

IPL.remove("RCB")

print(IPL)

"""

# POP :

"""
pop()

    - removes the specified index

    - it removes the last item by default

syntax :

    list_name.pop(index)

"""
# Example :

"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

# IPL.pop(1)

IPL.pop()

print(IPL)

"""

# DEL Statement:

"""
del

    - can be used to delete an element at a specific index or remove slices from the list

syntax :

    del list_name[index]
    
"""

# Example :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]


# del IPL[2]

# del IPL[1 : 4]

del IPL

print(IPL)

"""

# Clear :

"""
clear()

    -  removes all items from the list

    - making it empty.

"""

# example :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

IPL.clear()

print(IPL)

"""

# List Comprehension :

"""
    - is concise way to  create a lists.


Syntax :

    [expression for item in iterable if condition]


expression :

    the value to be added to the new list

item :

    the current item from the iterable.

iterable :

    the collection of items

condition :

    an optional filter that allows you to select which items to include in the new list.

"""

# example :

# Without List Comprehension :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]

empty = []

for item in IPL:

    if "S" not in item:
        empty.append(item)


print(empty)

"""

# With List Comprehension :


"""
IPL = ["CSK","MI","RCB","SRH","KKR"]


empty = [item for item in IPL if "S" in item]

print(empty)

"""

# Example :

"""
x = "Once Upon a Time There Lived a Ghost"

sentence = x.split()


larger_words = [item for item in sentence if len(item)>4]

print(larger_words)

"""


# Tuple: 

"""
    - Immutable ==> Unchangeable

    - Ordered

    - Allow Duplicates

    - Used to store multiple items in a single variable

    - it can be any datatype


mytuple = (100,"Beem",3+4j,True,678.987)

"""
# Constructor :

"""
tuple()


# ex :
x = tuple(("Apple","Orange","Mango"))

print(x)
print(type(x))

"""

# Creating a tuple :

"""
fruits = ("apple","mango","banana")

Teams = "CSK","RCB","MI"

print(Teams)

print(type(Teams))

"""

# Access Tuple Elements :

# Using Index :

"""
players = ("Dhoni","Kohli","Rohit","Pant","Sachin")


# print(players[0])
# print(players[-1])

print(players[1 : 4])

"""
# Tuple Operations :

"""
    1. Concatenation
    2. Repetition
    3. Membership


1. Concatenation :

    using the + Operator


# Example

a = ("dhoni","kohli")

b = ("rohit","pant")

Team = a + b

print(Team)

"""

# Repetition :

"""
    - can repeat elements of tuple using * Operator
"""
# Example :

"""
a = ("dhoni","kohli")

repeat_tuple = a * 2

print(repeat_tuple)

"""

# Membership :

"""
    - using in Operator 


# Example :

a = ("dhoni","kohli")

print("dhoni" in a)

"""

# Packing and Unpacking :

# Example :

"""
Players = "Dhoni","Kohli","Rohit","Pant"

CSK,*RCB,MI = Players

print(CSK)
print(RCB)
print(MI)

"""

# Tuple Methods :

"""
    index
    count

Index :

    - returns the index value of the first occurrence of the specified value 


# Example :

a = (10 , 20, 43, 20 )

print(a.index(20))

"""

# Count :
"""
    - returns the number of occurrences of the specified value in the tuple

# Example :

a = (10 , 20, 43, 20 )

print(a.count(20))

"""


# Set :

"""
    - Unordered

    - Unindexed
    
    - Mutable

    - Do not Allow Duplicates

myset = {100, 34.5 , "SuperStar",True}

"""
# Constructor :

"""
set()


# Example :

myset = set((1,"Sample",30,50))

print(myset)
print(type(myset))

"""

# Duplicates Not Allowed :
"""
    - True and 1 are considered the same value
    - False and 0 are considered the same value


# Example :

Myset = {"CSK","RCB",1,"CSK","LSG",True}

print(Myset)

"""

# Adding and Removing Set items :

# ADD :

"""
add() :

    - Adds an element to the set.

""" 
# EX :

"""
Movie = {"GOAT","Vettaiyan","Amaran","Brother"}

Movie.add("Lubber Bandhu")

print(Movie)

"""
# REMOVE :

"""
    remove()
    discard()
    pop()
    clear()
"""
# remove() :

"""
     - Removes an element from the set.

"""
# Example :

"""
IPL = {"CSK","MI","RCB","KKR","SRH"}

# IPL.remove("KKR")

# IPL.remove("LSG")

print(IPL)

"""

# Discard() :

"""
IPL = {"CSK","MI","RCB","KKR","SRH"}

# IPL.discard("SRH")

IPL.discard("LSG")

print(IPL)

"""

# Pop() :

"""
IPL = {"CSK","MI","RCB","KKR","SRH"}

IPL.pop()

print(IPL)

"""

# clear():

"""
IPL = {"CSK","MI","RCB","KKR","SRH"}

IPL.clear()

print(IPL)

"""

# Set Operations :

"""
Union() :

    It returns a new set with elements from both sets.
    
"""

# Example :

"""
a = {10,20,30}

b = {40,50,60}

# c = a.union(b)

c = a | b

print(c)

"""

# Intersection : (Common Elements)

"""
a = {10,20,30}

b = {30,40,50}

c = a & b

print(c)

"""

# Difference :(Elements in a but not in b)

"""
a = {10,20,30}

b = {30,40,50}

c = a - b

print(c)

"""

# looping in a set :

"""
team = {"CSK","MI","RCB"}

for i in team:
    print(i)

"""

# Dictionary :

"""
    - Key = value Pair

    - Ordered

    - Changeable 

    - do not allow dublicates [keys]

mydict = { "Name" : "Murugan" , "Age" : 23, "Address":"Chennai"}

"""
# Example :

"""
mydict = { "Name" : "Murugan" , "Age" : 23, "Address":"Chennai"}

print(mydict)

print(type(mydict))

"""
# Constructor :

"""
dict()

"""
# Example :

"""
products = dict(Bread = 50 , Jam = 40 , Apple = 120)

print(products)

"""
# Accessing values :

"""
Products = {"Bread" : 50,"Jam":40,"Apple":120}

print(Products["Jam"])

"""

# Add items :

"""
Products = {"Bread" : 50,"Jam":40,"Apple":120}

Products["Maaza"] = 60

print(Products)

"""

# Update :

"""
Products["Jam"] = 80

print(Products)

"""

# GET Method : get(key)

"""
Products = {"Bread" : 50,"Jam":40,"Apple":120}

a = Products.get("Apple")

print(a)

"""
# Remove Dictionary items :

"""

pop()
popitem()
clear()
del

"""

# pop() :

# Products = {"Bread" : 50,"Jam":40,"Apple":120}

"""
Products.pop("Jam")

print(Products)

"""

#popitem()

"""
Products.popitem()

print(Products)

"""

# Clear()

"""
Products.clear()

print(Products)

"""

# Del :

"""
del Products

print(Products)

"""
# Dictionary Methods :

"""
1. keys()
2. values()
3. items()

"""

# Keys() :

'''
Products = {"Bread" : 50,"Jam":40,"Apple":120}

Product_key = Products.keys()

print(Product_key)

'''

# values()

"""
Products = {"Bread" : 50,"Jam":40,"Apple":120}

Product_values = Products.values()

print(Product_values)

"""

# items() :

"""
Products = {"Bread" : 50,"Jam":40,"Apple":120}

print(Products.items())

"""


# Nested Dictionary :

"""
Product1 = {"Bread":50}

Product2 = {"Jam":40}

Product3 = {"Apple":120}


Products = {
            "P1" : Product1,
            "P2":Product2,
            "P3":Product3
            }

print(Products["P1"]["Bread"])

"""

# Simple Banking Project :

"""
balance = 500


while True:

    print("\n Welcome to The Simple Banking System..!")

    print(" 1 - Deposit ")
    print(" 2 - Withdraw ")
    print(" 3 - Check Balance ")
    print(" 4 - Exit ")

    choice = input("Choose Your Option [ 1 - 4 ] : ")

    if choice == "1":

        amount = float(input("Enter Your Deposit Amount : "))

        balance += amount

        print(f"${amount} Deposited Successfully..!")

    
    elif choice == "2":

        amount = float(input("Enter Amount to Withdraw : "))

        if amount <= balance:
            balance -= amount

            print(f"${amount} Withdrawn Successfully..!")

        else:
            print("Insufficient Balance..!")

    elif choice == "3" :

        print(f"Your Current Balance is ${balance}.")

    elif choice == "4" :

        print("Existing the System. Have a Nice Day..!")
        break


    else :
        print("Invalid Option..! Please Choose Correct Option..!")

"""


# Functions :

"""
    - set of instructions is called as a function

    - a reusable block of code that performs a specific task or set of tasks.


There are Two Types :

    1. Built-In Functions
    2. User-Defined Functions


"""
# Built-in Functions :
"""
    print()
    input()
    len()
    list()
    tuple()
    type()

"""

# User Defined Function :

"""
Syntax :

def function_name():
    # code to be executed


def - Keyword
function_name - Name of the function
(): - Parameter or Argument


"""

#Example :

"""
# Declare a function :

def Marriage():
    print("I do")

# Calling a function 

Marriage()    
Marriage()
Marriage()

"""

# types of concepts in function :

"""

    1. Void Function :
    
        returns Nothing

            1. With Argument
            2. Without Argument


    2. Non Void Function:

        it has somthing to return

            1. With Argument
            2. Without Argument

"""

# Void Function :

# Without Argument :

"""
def Addition():

    a = 10
    b = 20

    c = a + b # 10 + 20 = 30

    print(c)


print(Addition())

"""

# With Argument :

"""
def Addition(a,b): # (a,b) - Parameter

    c = a + b 

    print(c)

    return


print(Addition(10,20))  # Arguements

"""
# Example For with Argument :


"""
def Marriage(Ponnu,Mappillai):

    print(f"{Ponnu} - Weds - {Mappillai}")


Marriage("Jothika","Surya")

Marriage("Shalini","Ajith")

Marriage("Vijay","Sangeetha")

"""

# Non Void Function :

# Without Argument :

"""
def Addition():
    a = 10
    b = 20
    c = a + b # 10 + 20 = 30

    return c


print(Addition())

"""

# With Argument :


"""
def Addition(a , b):

    c = a + b

    return c

x = int(input("Enter Num1 : "))
y = int(input("Enter Num2 : "))

print(Addition(x,y))

"""

# Moudles :

"""

    - a modules is a file that contains code(variables,functtion,class etc...)


types of modules :

    three types of modules :

        1. Buit-in Modules
        2. External Modules
        3. User Defined Modules

"""

# Create a module :

# 1. Create a file with .py extension
# 2. Write your code in that file
# 3. Save the file
# 4. Import the module in your main file
# 5. Use the module in your main file


# import :

"""
import module1


print(module1.Actor)

"""

"""
# from module1 import Actor

from module1 import *

print(Actor)

myfun()

"""

# rename a module :

"""
import module1 as Mango

print(Mango.Actor)

"""


# Random Module :
"""
    is used to generate random numbers and performs random selections.


    random()
    randint()
    uniform()
    choice()
    shuffle()
    sample()

"""

# 1. random() :

"""
    returns a random float between 0.0 to 1.0

"""

#example :

"""
import random

random_float = random.random()

print(random_float)

"""

# 2. randint(a,b) :

"""
    returns a random integer

"""

#example :

"""
import random

print(random.randint(1, 10))

"""

# 3. uniform(a,b) :

"""

    - spcifi the numbers between to create a random float

"""

# example :

"""
import random

print(random.uniform(5,10))

"""

# 4. choice(sequence) :

"""
- returns a random element from a non-empty sequence.
- sequence can be a list, tuple, string, or set.

"""
# example :

"""
import random

print(random.choice([1, 2, 3, 4, 5]))

"""

# Shuffle() :

"""
    - shuffles the sequnce in place
"""

# Examxple :

"""
import random


IPL = ["CSK","MI","RCB","KKR","SRH"]


random.shuffle(IPL)


print(IPL)

"""

# 6. Sample(population, k):

"""
    select unique elements from the population
"""

#example :

"""
import random

IPL = ["CSK","MI","RCB","KKR","SRH"]

sample_items = random.sample(IPL,2)

print(sample_items)

"""

# Rock Paper Scissors Game :

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

"""
0 - Rock
1 - Paper
2 - Scissors

"""

"""
User_Choice = int(input("What Do You Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))

# print("User Choice : ",User_Choice)


Computer_Choice = random.randint(0 , 2)

# print("Computer Choice : ",Computer_Choice)


game = [rock,paper,scissors]

if User_Choice>=3 or User_Choice <0: # 3456 or -1-2
    print("You Type Wrong")

else:

    print("User Choose : \n",game[User_Choice] )

    print("Computer Choose : \n",game[Computer_Choice])

    if User_Choice == 0 and  Computer_Choice == 2: #  Rock - Scissors
        print("Rock Smashes Scissors! You Win!")

    elif Computer_Choice == 0 and User_Choice == 2: #  C => Rock - U => Scissors
        print("Rock Smashes Scissors! You Lose!")

    elif Computer_Choice > User_Choice : # C => 1 2 -  U => 0 1
        print("You Lose!")

    elif User_Choice > Computer_Choice : # U => 1 2  -  C => 0 1
        print("You Win!")

    elif User_Choice == Computer_Choice :
        print("It's a Tie!")


"""

# Grocery  Shop :

"""
import grocery_operations as go

while True:

    print("\n1. Add Items")
    print("2. Remove Items")
    print("3. View Items")
    print("4. Display Total Cost")
    print("5. Exit")


    choice = input("Enter Your Choice : ")

    if choice == "1" :

        name = input("Enter Product Name : ")
        price = float(input("Enter Product Price : "))

        go.Add_items(name,price)

    elif choice == "2" :
        
        name = input("Enter Product Name : ")

        go.Remove_items(name)


    elif choice == "3" :
        
        go.Display_items()


    elif choice == "4" :
        
        go.Total_cost()


    elif choice == "5" :
        
        print("Exit the program...")
        break

    else:
        print("Invalid Choice...")

"""


# Programming paradigm : 

"""

    - is a style or way of thinking about writing code and organizing code.


    1. Imperative
    2. Declarative
    3. Object-Oriented
    4. Functional
    5. Procedural
    6. Logic

"""

# OOPS => Object Oriented Programming :

"""
    Class
    Object

    Inheritance
    Encapsulation
    Abstraction
    Polymorphism

"""
# Class :

"""
    - A Blueprint or Template for Creating Objects.

    - it defines Attributes[data or variables] and Methods[Functions]

Syntax :

class Class_Name:
    
    # Body of class :
        Attributes
        Methods

"""

# Example :

"""
class House:

    color  = "Maroon"
    num_bedrooms = 4
    num_bathrooms = 3

    def Switch_On(self):
        print("Light is On")

"""

# Object :

"""
    - an Object is an Instance of a Class

Syntax:

Object_Name = class_name()

"""

"""
Antilia = House()

print(Antilia.color)
print(Antilia.num_bedrooms)
print(Antilia.num_bathrooms)

"""

# Key Concepts :

# Class :

"""
    blueprint for creating object.

    - think of it as a plan for building something.

    ex :

        CAR 
"""
# Attributes :

"""
    These are the properties or Characterstics of an object.

    - the car might have attributes like,
    - color
    - model
    - year
    - Wheel

    1. Class Attributes :

        - These are the attributes that are common to all objects of a class.
        - They are defined inside the class definition.

    2. Instance Attributes

        - They are usally initialized in the Constructor.
        - They are unique to each object of a class.
"""

# Methods :

"""
    These are the actions that an Object can Perform
    They are like Functions but belong to an object

    - a Drive => Method could Make the Car Move
    - a Stop => Method could Make the Car Stop
"""

# Constructor : (__init__) : initialize
"""
    - a Special Method that initializes the objects Attributes
    - When the object is Created 
    - It is called automatically

    When You create a new car object,you can give is a color and model the
    Constructor initializes those values

"""

#Self :

"""
    - self is a Reference to the Current Instance of a Class.

    instance Reference :

        it allows to each object to reference it's own data and metods.

"""

# Object :

"""
    An instance of a Class.

    it's like Creating an Actual Car based on the Car Blueprint.

    My_car = Car()
"""

"""
class Car:

    #Class Attribute :
    Wheel = 4

    #Constructor :

    def __init__(self,color):
        #Instance Attributes :
        self.Color = color

    # Methods

    def Drive(self):
        print("The Car is Moving")

    def Stop(self):
        print("The Car has Stopped")

    def Show(self):
        print(f"Car Color : {self.Color}")
        print(f"Car Wheel : {self.Wheel}" )




#Object :

Audi = Car("Blue")

# Accessing Attributes :
# print(Audi.Wheel)
# print(Audi.Color)

# Audi.Drive()
# Audi.Stop()

# Audi.Show()


BMW = Car("Black")

BMW.Show()

"""


# Inheritance :

"""
    - Passing on features from one thing to another

    - in programming ,Allows one class to get attributes and methods from another class
        
    - children inherting traits from their parents

"""
#example :

"""
class Animal:

    def Sound(self):
        print("Animals Makes a Sound.")


class Dog(Animal):

    def Bark(self):
        print("Dogs are Barking.")


UnderDog = Dog()

UnderDog.Sound()

"""

# Types Of Inheritance :

"""
    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hierarchical Inheritance
    5. Hybrid Inheritance  

"""

#1. Single Inheritance :

"""
    - a child class inherit from just one parent Class.
"""
# Example :

"""
class Father:

    def car(self):
        print("Father's Car..!")


class Son(Father):

    def bike(self):
        print("Son's Bike..!")


vijay = Son()

vijay.car()
vijay.bike()    

"""

# Multiple Inheritance :

"""
    - a child class inherits from more than one parent class.
"""
#Example :

"""class Father:

    def car(self):
        print("Father's Car..!")


class Mother:

    def Scooty(self):
        print("Mother's Scooty..!")


class Son(Father,Mother):

    def bike(self):
        print("Son's Bike..!")



Ajith = Son()


Ajith.car()
Ajith.Scooty()
Ajith.bike()

"""

#Example 2 :

"""
class Phone:

    def Call(self):
        print("Make a Call..!")


class Camera:

    def Picture(self):
        print("Take a Picture..!")



class SmartPhone(Phone,Camera):

    def Internet(self):
        print("Access Internet..!")

"""

# Multilevel Inheritance :

"""
    - invoke a chain of inheritance

    - when a child class become a parent for another class

"""

#Example :

"""
class Grandfather:

    def Bulletcart(self):
        print("Grandfather is driving a Bullet Cart..!")


class Father(Grandfather):

    def Car(self):
        print("Father is driving a Car..!")


class Son(Father):

    def Bike(self):
        print("Son is driving a Bike..!")


class Grandchild(Son):

    def Cycle(self):
        print("Grandchild is driving a Cycle..!")



Sanjay = Grandchild()

Sanjay.Bulletcart()
Sanjay.Car()
Sanjay.Bike()
Sanjay.Cycle()

"""

# 4. Hierarchical Inheritance :

"""
    - Multiple Child Classes Inherits From a Single Parent Class.
"""

#example :

"""class Father:

    def Car(self):
        print("Father is driving a Car..!")


class Son(Father):
    
    def Bike(self):
        print("Son is driving a Bike..!")

class Daughter(Father):

    def Scooty(self):
        print("Daughter is driving a Scooty..!")



surya = Son()

surya.Car()
surya.Bike()


jothika = Daughter()

jothika.Car()
jothika.Scooty()

"""

#example 2 :

"""
class Bank:

    def Service(self):
        print("Bank Service is available..!")


class Loan(Bank):

    def Offer_Loan(self):
        print("Loan is available..!")


class Saving_Account(Bank):

    def Open_account(self):
        print("Saving Account is available..!")

"""

# Hybrid Inheritance :

"""

 - Combination of more than one type of inheritance.

"""

# Example :


"""
class Product:

    def Show_Product(self):

        print("Product is available..!")



class Electronics(Product):

    def Show_Elec_Product(self):

        print("Electronics Product is available..!")



class Clothing(Product):

    def Show_Cloth_Product(self):

        print("Clothing Product is available..!")



class OnlineStore(Clothing,Electronics):

    def show_all_products(self):

        print("Show All Electronics and Clothing Products..")




Shop = OnlineStore()

Shop.show_all_products()

Shop.Show_Cloth_Product()

Shop.Show_Elec_Product()

"""

# File Handling :

"""
files Should be handled as binary or text:

    't' - Text Mode => Default Mode

    'b' - Binary Mode

    

Open() : # Open(fileName,Mode)

    - key function for working with files in python
    - Takes two Parameters
    - fileName : Name of the file to be opened
    - Mode : Mode in which the file is to be opened


    There are Four Different mode :

        1. Read    - 'r'
        2. Write   - 'w'
        3. Append  - 'a' -> HelloWorld
        4. Create  - 'x'



Read :

    Default Value
    Opens a file for reading
    Error if file does not exist.


Write :

    - Opens a file for writing
    - creates the file if it does not exist
    - will overwrite the entire file


Append :

    - Opens a file for Appending
    - Creates the file if it does not exist.


Create :

    - Creates the Specified File
    - returns an error if the file exists

"""

"""
read() :

    - this Method for reading the content of the file.
    - it returns the content of the file as a string.
    - by default the read() method returns the whole text
    - but you can also specify how many characters you want to return

"""

#  Open a file :

# Example 1 :

"""
# f = open("sample.txt",'rt')

# f = open("sample.txt",'r')

f = open("sample.txt")

# print(f.read())

data = f.read(5)

print(data)

"""

# Example 2 :

"""
f = open("sample.txt")

print(f.read(3))

print(f.read()) # it will continue after the three letters.

"""

# ReadLine :
"""
    - Return Oneline
"""
# Example :

"""
f = open("sample.txt")

print(f.readline())
print(f.readline())
print(f.readline())

"""

# Readlines :

"""
    - returns a list
    - Containing each line in the file as list item.

"""
# Example :

"""
f = open("sample.txt")

print(f.readlines())

"""

# Looping :

"""
f = open("sample.txt")

for i in f:
    # print(i)
    print(i.strip()) # strip() is used to remove the newline character.

"""

# Close files :

"""
close()
    
    - a good practice to always close the file.
"""

# Example :

"""
f = open("sample.txt")

print(f.readline())

f.close()

print(f.readline())

"""
# Write Mode :

"""
    - write 
    - will overwrite existing content

    
write() :
    - write() function is used to write the content to the file.
    - It does not return anything.
"""

# Example :

"""f = open("GOAT.txt",'w')

f.write("Welcome to Python Bootcamp")

f.close()

"""
# Example : 2
 
"""
f = open("GOAT.txt",'w')

f.write("Welcome to six Days Python Bootcamp")

f.close()

"""

# Append Mode :

"""
    - Append
    - will add new content to the existing content
    - a = append
    - append to the end of the file

"""

# Example :

"""
f = open("GOAT.txt",'a')

f.write(" You have to learn a lot from this Bootcamp..")

f.close()

"""

# Create Mode :

"""
    - Create a new file
    - x = create

"""

# Example :

# f = open("Avengers.txt",'x')


# Find a mode in File handling : ==> mode

"""
f = open("sample.txt",'a')

# print(f.mode)  # Output : 'r'  # Read mode

print(f.mode)

"""

# readable():

"""
    - Used to check whether the specified file is readable or not.
    - Returns True if the file is readable, otherwise returns False.
    - it will take no parameter.

"""
# Example :

"""
f = open("GOAT.txt",'a')

print(f.readable())

"""

# With Statement - Contex Manager :

"""
    - it simplifies the management of common resources like file streams.

    - if we access the file in outside the block it will through the error.

syntax :

    with open(filename) as variable_name:
        # code to be executed


""" 

# Example :

"""
with open('sample.txt') as f:
    # print(f.read())
    print(f.readline())


# Outside the block :

print(f.read())

"""
# Closed :

"""
    - is a boolean attribute which tell us whether or not the file is closed.
"""

# Example :

"""
with open('sample.txt') as f:

    # f.close()
    # print(f.closed)

    if f.closed:
        print("File is closed")
    else:
        print("File is Not Closed")

"""

# Binary Files :

"""
    - 'b' - binary files

    - 'rb' - Read Binary files

    - 'wb' - Write Binary files

    - 'ab' - Append Binary files

"""

# Example For image - read and write


# Read image

"""
f = open("Mahi.jpg",'rb')

data = f.read()

# print(data)


# Write Image :

x = open("Dhoni.jpg","wb")

x.write(data)

x.close()

"""


# Read Video :

"""
f = open("Manasilayoo.mp4",'rb')

data = f.read()


# Write video :

v = open("Vettaiyan.mp4","wb")

v.write(data)

v.close()

"""

# Delete a file Using File Handling :

"""
    - to delete a file,you must import os module
"""
# Example :

"""
import os

# os.remove("Avengers.txt")


# Check if the file is exist or not :

if os.path.exists('Manasilayoo.mp4'):
    os.remove("Manasilayoo.mp4")
else:
    print("File does not exist")

"""

# Delete a folder in File Handling :

"""
    - You can remove only empty folders.
"""
# Example :

"""
import os

os.rmdir("BootCamp")

"""

# Exception Handling :

"""
    - When an Errors Occurrs or Exception as we call it,python will normaly stop and 
    generate an error message.


    1. Try
    2. Except
    3. Finally
    4. Else

Try :

    Test the block of code for Errors.

Except :

    Handle the Errors

Else :

    Excute the Code When There is No error

Finally :

    Excute the code regardless of the result try and except block
"""

# Example :

"""
try:

    print("Marvel")

    print("HI")

except:

    print("Name is Not Defined")

else:
    
    print("This is Else Block")

finally:

    print("Finally i'm a Mixture Uncle..")

"""

"""
Error = dir(locals()['__builtins__'])

print(Error)

print(len(Error))

"""

"""
There are some types of Error :

    Zero Division Error
    Name Error
    Index Error
    Value Error
    Key Error
    Attribute Error
"""

# Zero Division Error :

"""
try:
    a = 10
    b = 0
    c = a / b
    print(c)

except ZeroDivisionError as e:
    print("Error : ", e)

# except Exception as e:
#     print("Error : ", e)
    
"""

# Name Error :


"""
try:
    name = "Surya"
    print(age)

except NameError as e:
    print("Error : ", e)

"""

#Example :

"""
try:
    number = int(input('Enter Any Number : '))

except Exception as e:
    print("Error : ", e)

else:
    print("You Have Entered : ", number)

finally:
    print("Program Finished")

"""

# ATM in Exception Handling :


"""
balance = 1000  # User Account Balance


try:

    withdrawal_amount = int(input("Enter The Amount to Withdraw : ")) #Asking for input

    if withdrawal_amount > balance:

        raise ValueError("Insufficient Balance") # Manually raising an Exception
    
    if withdrawal_amount <= 0:

        raise ValueError("Amount Must be Greater than Zero") # exception for invalid input
    
    balance -= withdrawal_amount
    print("Withdrawal Successful. Remaining Balance is : ", balance)

except ValueError as e:
    print("Error : ", e) #handling exceptions by printing the msg

finally:
    print("Thank You For Using The ATM.")

"""

# Project : 1 

# Title : Contact Book

"""
def add_Contact(fileName):

    name = input("Enter Contact Name : ")
    phone = input("Enter Contact Number :")

    with open(fileName,'a') as file:

        file.write(f"{name} - {phone}\n")

    print("Contact Added.!")



def view_Contact(fileName):

    with open(fileName,'r') as file:

        contacts = file.readlines()

        for contact in contacts:

            print(contact.strip())




fileName = "Contacts.txt"

while True:
    
    choice = input("1. Add Contact\n2. View Contact\n3. Exit\n Enter Option : ")


    if choice == "1":
        add_Contact(fileName)
    
    elif choice == "2":

        view_Contact(fileName)

    elif choice == "3":
        break

    else:
        print("Invalid Choice. Please Try Again.")

"""


# ToDo List :


"""
def add_task(fileName):

    task = input("Enter New Task : ")

    with open(fileName,'a') as file:

        file.write(f"{task}\n")

    print("Task Added Successfully..!")


def view_tasks(fileName):

    with open(fileName,'r') as file:

        tasks =file.readlines()

        if tasks:
            print("Tasks : ")

            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task.strip()}")

        else:
            print("No Tasks Available..!")


def remove_task(fileName):

    view_tasks(fileName)

    task_no = int(input("Enter the Task Number to Mark as Done : "))

    with open(fileName,'r') as file:
        tasks = file.readlines()

    with open(fileName,'w') as file:
        
        for i , task in enumerate(tasks,start=1):

            if i !=  task_no: 
                file.write(task)

    print("Your Task Marked as Done.")


File_Name = "todo.txt"

while True :
    
    choice = input("1. Add Task\n2. View Task\n3. Remove Task\n4. Exit\nEnter the Option : ")

    if choice == "1":
        add_task(File_Name)

    elif choice == "2":
        view_tasks(File_Name)

    elif choice == "3":
        remove_task(File_Name)

    elif choice == "4":
        break

    else:
        print("Invalid Choice. Please Try Again.")

"""


# User Registration Projcet :

"""
def register_user(fileName):

    userName = input("Enter UserName : ")
    password = input("Enter Password : ")

    with open(fileName,'a') as file:

        file.write(f"{userName},{password}\n")

    print("User Registered Successfully..!")


def login_user(fileName):

    userName = input("Enter UserName : ")
    password = input("Enter Password : ")

    with open(fileName,'r') as file:

        users = file.readlines()

        for user in users:

            stored_username,stored_password = user.strip().split(',')

            if stored_username == userName and stored_password == password:

                print("Login Successfully..!")
                
                return

    print("Login Failed..! \nInvalid Credentials..!")


File_Name = "Users.txt"

while True:

    choice = input("1. Register\n2. Login\n3. Exit\n Enter Your Option : ")

    if choice == "1":
        register_user(File_Name)

    elif choice == "2":
        login_user(File_Name)

    elif choice == "3":
        break

    else:
        print("Invalid Choice. Please Try Again.")

"""


# Employee Management Project :

"""
1. Add Employee
2. Romove Employee
3. Update Employee
4. Display Employee
5. Save to File
6. Load to File
7. Exit
"""

# Excute the code Here :

Employees = {}

def add_employee(emp_id,name,age,department,salary):

    Employees[emp_id] = {
        "Name": name,
        "Age": age,
        "Department": department,
        "Salary": salary
    }

    print(f"Employee {name} added Successfully..!")


def view_employee():

    if Employees:
        for emp_id, emp_data in Employees.items():
            print(f"Employee ID : {emp_id} ==> Details : {emp_data}")

    else:
        print("No Employees Available..!")


def remove_employee(emp_id):

    # try:
        emp = Employees.pop(emp_id)
        print(f"Employee {emp['Name']} removed Successfully..!")


while True:

    print("\n Welcome To Employee Management System : ")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Display Employee")
    print("5. Save to File")
    print("6. Load to File")
    print("7. Exit")


    choice = input("\nEnter Your Option : ")


    if choice == "1":
        
        emp_id = input("Enter Employee ID : ")
        name = input("Enter Employee Name : ")
        age = input("Enter Employee Age : ")
        department = input("Enter Employee Department : ")
        salary = input("Enter Employee Salary : ")

        add_employee(emp_id,name,age,department,salary)


    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        view_employee()

    elif choice == "5":
        pass

    elif choice == "6":
        pass

    elif choice == "7":
        break

    else:
        print("Invalid Option. Please Try Again.")

