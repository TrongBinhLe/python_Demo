import random
import math

site_name = 'programiz.pro'
print(site_name)

# assigning a new value to site_name
site_name = 'apple.com'

print(site_name)

#Assigning multiple values to multiple variables
a, b, c = 5, 3.2, 'Hello'

print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello

#If we want to assign the same value to multiple variables at once, we can do this as:
site1 = site2 = 'programiz.com'

print (site1)  # prints programiz.com
print (site2)  # prints programiz.com

      # II. Python Literals

      # III. Python Type Conversion
# III.1 Python Implicit Type Conversioninteger_number = 123
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#III.2  Explicit Type Conversion

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


      # IV. Python Input
numb = int(input("Please enter the number: "))
print(numb)
print('Data type of num:', type(numb))

      #V. Arithmetic Operators in Python
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b) 

      #VI. PYTHON FLOW CONTROL

#VI.1 Python if...else Statement
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# VI.2 Pyhotn for Loop  
      #1. 
languages = ['Swift', 'Python', 'Go']

# Start of loop
for lang in languages:
    print(lang)
    print('-----')
# End of for loop

print('Last statement')

# VI.3  Python while Loop

number = 1

while number <= 3:
    print(number)
    number = number + 1
 

 #using pass trong python

n = 10

# use pass inside if statement
if n > 10:
    pass

# VII. Python Numbers, Type Conversion and Mathematics

#VII.1 Python Numeric Data Type

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

#VII.2 Number Systems
print(0b1101011)  # prints 107

print(0xFB + 0b10)  # prints 253

print(0o15)  # prints 13


#VII.3 Python Random Module

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())

#VII.4 Python Mathematics

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

#VII.5 Python List
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)


languages = ('Python', 1 , 'C++')

# access the first item
print(languages[1])   # Python

# access the third item
print(languages[2])   # C++
#VII.6 Python Tuple

