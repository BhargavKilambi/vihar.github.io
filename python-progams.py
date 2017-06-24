"""
1.1
After installing python to open the python shell open
your command prompt or terminal then type in python.
You will be shown the running python version on your machine
as well as few first utilities such as " "help",
"copyright", "credits" or "license" "and a symbol
" >>> " which means python is waiting for your instructions.
"""

####################################################################

"""
1.2 , 1.3
Here is an example let us create a variable "number"
and assign it to value 24.
"""
number = 24
"""
Now we will create a variable "name" and let us assign it
to string "hoppercamp"
Note : Stings always start and end with single/double quotes (' '),(" ")
"""
name = "hoppercamp"

####################################################################

"""
1.4

Let us perform an arithmetic operation on two variables and store it
in another variable "result".
Note : You can type in the same instructions in the python shell.
You can also use python shell as calculator feel free to play with it.
"""
var_a = 5
var_b = 19
result = var_a + var_b
print(result)

# Similarly we can also perform remaining operations
var_x = 9
var_y = 3
subtraction = var_x - var_y
multiplication = var_x * var_y
division = var_x / var_y
remainder = var_x % var_y
print(subtraction)
print(multiplication)
print(division)
print(remainder)
# Note % operator gives remainder of two numbers.
# Prints the value in the result (24)
"""
Now let us do some intresting logical operations in python.
In python boolean values are returned or assigned as True and False.
Lets declare two variables and ask python which variable has is greater.
"""
var_a = 77
var_b = 89
var_a > var_b

# The python shell returns the value False as var_a is less than var_b.
"""
In python camparisions are done using the operator "==", you can
compare numbers, strings, and also booleans.
"!=" is used to check if the variables are not equal.

Now lets declare two variables and check whether they are equal or unequal.
"""
profile_a = 73
profile_b = 92

print(profile_a == profile_b)
print(profile_a != profile_b)
"""
Output :
False
True

(as 73!=92)
Note: "==,!=" operators always returns a boolean value.
"""

####################################################################

"""
1.6
In Python functions are always created the same way:

Notice that the function's first line ends with a colon
and the function body, the line or lines that belong to
the function is indented.
"""


def my_function_name():
    print("this is the function body")


####################################################################

"""
1.7
Functions are called with their function names followed by parentheses "()"

Example:
"""


def hows_dog_barks():
    print("Bow Bow !!!!")


hows_dog_barks()
# Calling function


def person(name, pronoun):
    print("{}'s a genius and {} OK!".format(name, pronoun))


person("Harry", "he's")
person("Natalie", "she's")
person("Avengers", "they're")


def average(num1, num2):
    return (num1 + num2) / 2


avg = average(2, 8)
print(avg)

"""
Output:

Bow Bow !!!!
Harry's a genius and he's OK!
Natalie's a genius and she's OK!
Avengers's a genius and they're OK!
5

"""

####################################################################

"""
1.10

To exit the Python shell, use the functions exit() or quit().
Your shell might also tell you a keyboard shortcut
to use to exit it as well. These are often ctrl-d or ctrl-z.

>>>exit()
"""

####################################################################

"""
1.11

To run a .py file, open your command prompt or terminal and go to
the working directory, now to run a python file we have to use "python" command
followed by filename.py

Example :
Directory : /Users/Hoppercamp/Desktop/
hello_world.py
    print("Hello World !")

Now to run this python file in command prompt or terminal type in
python hello_world.py


"""

###################################################################
"""
2.1
"""
# Creating a variable is always same:

variable_name = "variable value"

# And you can always delete a variable using del keyword:

del variable_name

###################################################################

"""
2.2

The two built-in types of numbers in Python are int and float.
Ints are whole numbers and floats are decimal numbers.

round() is a built-in function that will round a float
to the nearest whole number.

"""
round(2.66)

# Rounds to 3

###################################################################

"""
2.5
Lets create a list which is named as my_list containing
a string, integer, float value.

Note : append,remove functions are built in functions of python
which adds elements to lists and removes elements respectively.
Lists are mutable*

.append(number) - adds number to the end of the list .
.remove(number) - removes number "specified variable" .

"""

my_list = ["Horper", 1, 3.4]
my_list.append("Camp")
my_list.remove(1)

print(my_list)

# Output :['Hello', 3.4, 'Camp']

###################################################################

"""
2.6
Tuples are immutable.
We can't append into tuples.
Lets create a tuple containg fruits.
"""
fruits = ('apple', 'mango', 'orange')
print(fruits)
print(type(fruits))

"""
Output:
('apple', 'mango', 'orange')
<type 'tuple'>
"""

###################################################################

"""
2.7
Lets create a set containing first 4 prime numbers
"""

prime_set = {2, 3, 5, 7}
print(prime_set)
print(type(prime_set))

"""
Output:
set([2, 3, 5, 7])
<type 'set'>
"""

###################################################################

"""
2.8
"""

my_dict = {'Language': 'Python', 'Type': 3, 'Topic': 'Dictionary'}
print(type(my_dict))
print(my_dict['Language'])
print(my_dict['Type'])
print(my_dict['Topic'])

"""
Output:
<type 'dict'>
Python
3
Dictionary
"""

###################################################################

"""
3.1
Lets write a if-else program to check whether the given
number is even or odd
"""
num = 23
if(num % 2 == 0):
    print("The given number is even.")
else:
    print("The given number is odd.")

# Output: The given number is odd .

###################################################################

"""
3.2
Stark likes to go to shopping when the temparature is less
than 24 degrees celcius, He likes to swim when the temparature
is in between 25-30 degrees celcius otherwise he stays at home.
Now lets write a if elif else program to suit Starks agenda.
"""
present_temp = 27
if(present_temp < 24):
    print("Stark goes to shopping")
elif(present_temp > 25 & present_temp < 30):
    print("Stark goes to Pool !")
else:
    print("Stark stays at home.")
# if,elif,else for finding greatest of three numbers
a = input()
b = input()
c = input()

if(a > b & a > c):
    print("a is greatest")
elif(b > a & b > c):
    print("b is greatest")
else:
    print("c is greatest")

###################################################################

"""
3.4

Program for printing first 10 natural numbers
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

# Printing first 5 even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if (number % 2 == 0):
        print(number)

###################################################################

"""
3.6
"""
numbers = range(0, 100)
print(type(numbers))
for number in numbers:
    print(number)

###################################################################

"""
3.7
"""
a = 19
while(a < 25):
    print("The value of a is {}".format(a))
    a = a + 1

###################################################################

"""
3.8
Lets break the range until 50 in for loop
using the break keyword.
"""

numbers = range(0, 100)
for number in numbers:
    if(number % 2 == 0):
        print(number)
        if(number == 50):
            break

###################################################################

"""
3.9
"""
for letter in 'Hoppercamp':
    if(letter == 'c'):
        continue
    print('Current Letter :{}'.format(letter))


"""
Output :
Current Letter :H
Current Letter :o
Current Letter :p
Current Letter :p
Current Letter :e
Current Letter :r
Current Letter :a
Current Letter :m
Current Letter :p
Vihars-MacBook-Pro:
"""

###################################################################

"""
3.10
"""
numbers = range(0, 100)


def display_numbers():
    for number in numbers:
        pass


def even_numbers():
    pass


###################################################################

"""
4.1
"""


def hello_world():
    print("Hello World !")


###################################################################

"""
4.2
Function named addition that takes two variables as parameters
and prints the result.
"""


def addition(var_a, var_b):
    result = var_a + var_b
    print(result)


addition(2, 3)

# Output : 5

###################################################################

"""
4.4
"""


def add(var_a, var_b):
    print("The sum of {} and {} is ".format(var_a, var_b))
    return var_a + var_b


add(19, 24)

###################################################################

"""
4.5
"""


def recur_factorial(num):
    if(num < 0):
        print("Factorial doesnt exists for negative numbers ")
    elif (num == 1):
        return num
    else:
        return num * recur_factorial(num - 1)


###################################################################

"""
4.7
"""
a = 100

print("the value of a : {}".format(a))


def num_square():
    a = 5
    print("the value of a : {}".format(a))
    a = 7
    print("the value of a : {}".format(a))
    return a * a


num_square()
print("the value of a : {}".format(a))


###################################################################

"""
4.8
"""

square = lambda x: x * x

print(square(5))


###################################################################

"""
5.1,5.2
Creating a class
Note : Class name should start with capital letter.
"""


class ExampleClass:
    """Docstring (Multiple line comments)"""
    pass


class Car:
    engine_type = "Disel"
    mileage = 19
    weight = 379.32
    condition = True


my_car = Car()
print(type(my_car))
print(my_car.engine_type)
print(my_car.mileage)
print(my_car.weight)
print(my_car.condition)

###################################################################

"""
5.4
"""


class MyClass(object):
    i = 23

    def __init__(self):
        self.i = 19


a = MyClass()
print(a.i)
print(MyClass.i)

# Output : 19
#          23

###################################################################

"""
5.5
class BaseClass:
  Artibutes and methods declararion
class DerivedClass(BaseClass):
  Artibutes and methods declararion

"""


class Car:
    wheels = 4
    engines = 1
    good_mileage = True
    speed = "Normal"

    def sound(self):
        print("Roars !!")


class Sportscar(Car):
    engines = 2
    good_mileage = False
    speed = "Very Fast"

    def sound(self):
        print("Grunts !!")


normal_car = Car()
print(normal_car.wheels)
print(normal_car.engines)
print(normal_car.good_mileage)
normal_car.sound()

race_car = Sportscar()
print(race_car.wheels)
print(race_car.engines)
print(race_car.good_mileage)
race_car.sound()

###################################################################

"""
5.6
"""


class Parent(object):
    def __init__(self):
        self.value = 7

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1


"""
Output:

>>> c = Child()
>>> c.get_value()
8
"""

###################################################################

"""
5.7
"""


class Parent(object):
    def foo(self):
        print("Printing from parent class")


class Derived(Parent):
    def foo(self):
        super(Derived, self).foo()   # calls 'Parent.foo()'


my_class = Derived()
my_class.foo()

# Output: Printing from parent class

###################################################################

"""
5.9
"""
###################################################################

"""
5.10
Abc
"""


class Foo(object):
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def get_iterator(self):
        return iter(self)


###################################################################

"""
6.1

>>> 29 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

"""

###################################################################

"""
6.2
"""

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

###################################################################

"""
6.3
"""

try:
    a = int(input("Enter postitive interer:"))
    if a <= 0:
        raise ValueError("Please enter a positive number")
except ValueError as ve:
    print(ve)


###################################################################

"""
6.5
"""


def greet_person(PersonName):
    if(PersonName == "Captain"):
        raise Exception("we don't like you, Captain")
    print("Hi there {}".format(PersonName))


###################################################################

"""
7.2
Using random module in python
"""

import random

a = random.random()
print(a)

b = random.randint(1, 10)
print(b)

c = random.choice('abcdefghij')
print(c)


###################################################################

"""
7.4
"""
print(dir(list))
print(dir(tuple))

###################################################################

"""
7.5
"""
import time
import calendar


ticks = time.time()
print ("Number of ticks since 04:30am, November 19, 1997:", ticks)

localtime = time.asctime(time.localtime(time.time()))
print("current time :", localtime)

cal = calendar.month(2017, 3)
print("Here is the calendar:")
print(cal)

###################################################################

"""
8.2
"""

my_file = open("foo.txt", "wb")
print("Name of the file: ", my_file.name)
print("Closed or not : ", my_file.closed)
print("Opening mode : ", my_file.mode)
print("Softspace flag : ", my_file.softspace)

###################################################################

"""
8.3
"""

my_file = open("foo.txt", "wb")
print("Name of the file: ", my_file.name)

my_file.close()

###################################################################

"""
8.5
"""

my_file = open("foo.txt", "r+")
str = my_file.read(10)
print("Read String is : ", str)
# Close opend file
my_file.close()

###################################################################

"""
8.6
"""
flowers = open("flowers.txt", "wb")
flowers.write("Rose.\nSunflower.\nJasmine.")

# Close opend file
flowers.close()

###################################################################

"""
8.7
"""

import os

os.makedirs("test/multiple/levels")

fp = open("test/multiple/levels/file", "w")
fp.write("inspector praline")
fp.close()
