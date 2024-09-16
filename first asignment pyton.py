# 1. explain the key features of Python that make it a popular choice for programming

# ans. Python is popular due to its simple, readable syntax and dynamic typing,
     #  which make it easy to learn and use.
     #It offers an extensive standard library and supports multiple programming paradigms,
     #enhancing its versatility for web development, data science, AI, and more.
     # It has many significant features like easy to learn, powerful, versatile, open source,
     # portable, and extensible.


# 2 . Describe the role of predefined keywords in Python and provide examples of how they are used in a
     # program .
# ans.
#Predefined keywords in Python, also known as reserved words, are words that have special meaning and are part of
# the language's syntax.These keywords cannot be used as identifiers (variable names, function names, etc.) because
# they are reserved for specific syntactic constructs. They help define the structure and flow of a Python program.

# Examples
import keyword
print(keyword.kwlist)
# When you run this code, Python will show you a list of its keywords.
# another example: ( if ,elif and else keywords used for conditional statement)
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


#3.Compare and contrast mutable and immutable objects in Python with examples.
#ans.
# I) Mutable objects : Mutable objects can be changed after their creation. Examples include lists, dictionaries,
                        # sets, and custom objects.
my_list = [1, 2, 3]
my_list.append(4)  # Modifying the list
print(my_list)     # Output: [1, 2, 3, 4]


# II) Immutale objects : Immutable objects cannot be changed after their creation. Examples include integers,
                         # floats, strings, and tuples.
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)  # Creates a new tuple
print(my_tuple)  # Output: (1, 2, 3)
print(new_tuple) # Output: (1, 2, 3, 4)


#4. Discuss the different types of operators in Python and provide examples of how they are used.
# ans. In Python, operators are special symbols that perform operations on variables and values.
# A . Arithmetic operator - used to perform mathematical operations.
      # i) additon (+)
a = 5
b = 3
print(a + b)  # Output: 8

     # ii) subtraction (-)
print(a - b)  # Output: 2

     # iii) Multiplication (*)
print(a * b)  # Output: 15

    # iv) Division (/)
print(a / b)  # Output: 1.6666666666666667

     # v) Floor Divison (//)
print(a // b)  # Output: 1

      # vi) Exponentiation (**)
print(a ** b)  # Output: 125

# B. Comparsion operators - used to compare two values. They return a Boolean result (True or False).
     # i) Equal (==)
print(a == b)  # Output: False
     # ii) Greater Than (>)
print(10 > 5)  # Output: True
     # ii) Less Than (<)
print(10 < 5)  # Output: False

     # iii) Greater Than or Equal To (>=)
print(a >= b)  # Output: True

      #iv) Less Than or Equal To (<=)
print(a <= b)  # Output: False


# C. Logical Operators :  used to combine conditional statements.
        # i) AND (and): Returns True if both statements are true.
x = True
y = False
print(x and y)  # Output: False

       # ii) OR (or): Returns True if at least one of the statements is true.
print(x or y)  # Output: True

       # iii) NOT (not): Reverses the result, returns False if the result is true.
print(not x)  # Output: False


# 5 . explain the concept of type casting in Python with examples
# ans . """Conversion of one type of data to another is called type casting
# types of type casting are implicit type conversion and explicit type conversion"""

# i) implicit type converion - where python itself converts one data type to another

num_int = 10   # Integer
num_float = 2.5  # Float

# Adding integer and float, result is automatically cast to float
# example :
result = num_int + num_float

print(result)        # Output: 12.5
print(type(result))  # Output: <class 'float'>

# ii) explicit type conversion - where the user converts one  data type to another
#example :
num_int = 10
num_float = float(num_int)

print(num_float)        # Output: 10.0
print(type(num_float))  # Output: <class 'float'>

# 6. How do conditional statements work in Python? Illustrate with examples
# ans.  Conditional statment allows computer to excute  a certain condition only if it is true .
       # These statements include if, elif, and else, which help control the flow of a program.

# i) if statement :
# example :
age = 18
if age >= 18:
    print("You are eligible to vote.")

# ii) else  statment :
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# iii) elif statement :
# exanple :
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# iv) nested statement :
# example:
marks = 96
if marks >= 80:
    print("you will gwt a new phone ")
    if marks >= 95:
        print("you can go for a trip")

else :
    print('no phone for a month')



# 7)  Describe the different types of loops in Python and their use cases with examples.
# """i) for loop : for loop is a loop that repeats something in a given range .The for loop is used to iterate over a
# sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence."""

# use cases : Iterating over elements of a list or a tuple
             # Iterating over characters in a string
              # Iterating over keys or values in a dictionary
              # Executing a block of code a specific number of times

# example :
for i in range (1,6):
    print(i)

# ii) while loop :The while loop repeatedly executes a block of code as long as a specified condition is true.

# use cases : Repeating a block of code an unknown number of times until a condition is met
             # Creating an infinite loop that runs until externally interrupted (with a break statement, for example)
             # Implementing loops where the termination condition is more complex than simple iteration

# example :
m = 1
while n <= 5 :
    print(n)
    n += 1

# iii) Nested Loops :Loops can be nested within each other.
# This means you can have a for loop inside a while loop or a while loop inside a for loop, and so on.

# use cases :a) Iterating over multi-dimensional data structures (such as lists of lists)
             # b) Performing complex operations that require multiple levels of iteration

# example :
for i in range (1,4):
    for j in range (1,11):
        print(j,end = " ")
    print()










