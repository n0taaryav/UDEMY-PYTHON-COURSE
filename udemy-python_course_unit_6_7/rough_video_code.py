#variables
ex_var = 5
tjkd22 = 4

#data types
float = 1.3
int = 4
bool = True

#comments

# comments are fun

#math operators
addition = 1+1 #2
substraction = 2-1 #1
multiplication = 3*2 #6
division = 4/2 #2

exponentiation = 4**4 #256
floor_divison = 16 //5 #3
modulo = 7 %3 #1

#assaignment operators
add_assaign = 5
add_assaign += 7

sub_assaign = 5
sub_assaign -= 13

mul_assaign = 5
mul_assaign *= 15

div_assaign = 5
div_assaign /= 20

#print
example = 2.1
example2 = 2
example3 = False

print(example)
print(example2)
print(example3)

print(2019)

print((4+5) * 3)

#more on floats
exp = (123+280)/100
print(exp)

#round
exp3 = 2.12+3.13
print(round(exp,2))

#strings
ex_1 = "hello" + 'world'
ex_2 = "1230"
ex_3 = "$#%^&@*(#)"
ex_4 = "Hello World"
print(ex_4[1])
print("apple"[2])

#string slicing

sliceing_ex = "Oranges"

print(sliceing_ex[:3])
print(sliceing_ex[2:5])
print(sliceing_ex[4:])

#concatenation

print("apple" + " " + "pie" )

ex_41 = "AB" + " CD" + "EF"
print(ex_41[:2])
print(ex_41[3:6])

unchanged = "Hello world"
sliced = unchanged[:4]
print(sliced)
print(unchanged)

#functions
def function_name():
    print("hello")

function_name()


#function with parameter
def ex_1 (parameter):
    print("hello" + parameter )

ex_1("world")

def ex_2 (parameter1, parameter2, parameter3):

    print(parameter1 + parameter2 + parameter3)

ex_2(1 , 2 , 3)


def ex_3 (num1 = 4, num2 = 3):
    print(num1 * num2)

ex_3(3)
ex_3(3,4)

#importing modules

import random
print(random.randint(1, 10))

from random import randint
print(randint(1, 100))


from random import *
print(random())


#variable scope

example = "hello world"

def test_variable_scope():
    example = "bye world"
    return example

print(test_variable_scope())
print(example)


#def loc_ex():
   ## breakfast = "cake"
    ##return breakfast

##loc_ex()
##print(breakfast)

#flow control

print(4>3)
print(3<1)
print(9>=9)
print(8<=10)
print(10 != 100)
print(9 != 9)
print(10 == 10)
print(100 == 23)

print("hello" == "hello")

#strings control
all_low = "hello world"

print(all_low.upper())
print(all_low)

all_up = "HELLO WORLD"
print(all_up.upper())
print(all_up)

#
print("{} world".format("hello"))
