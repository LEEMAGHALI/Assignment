# -*- coding: utf-8 -*-
"""Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BYaG8IYAz1ibH4h9V6JXHQmemwy_SlVY

Assignment 1: Write a function to multiply two numbers and use it in the calculator function. The function name should be 'multiply_two_numbers'
"""

def multiply_two_numbers ():
    print("this function multiplies two numbers")

multiply_two_numbers()

def multiply_two_numbers(a,b):
    print(a*b)

multiply_two_numbers(5,3)

def add_two_numbers(a,b):
  print(a+b)

def subtract_two_numbers (a,b):
    print (a-b)

def calculator(a,b, operation):
  if operation == "add":
     add_two_numbers(a,b)
  elif operation == "subtract":
     subtract_two_numbers(a,b)
  elif operation == "multiply":
     multiply_two_numbers(a,b)
  else:
         print("Please input some integer values and specify your operation as 'add', 'subtract' or 'multiply'")

calculator(15,20, "add" )

calculator (12,45, "subtract")

calculator (52,3, "multiply")

calculator(10, 20, "add", "subtract")

calculator(10, "20", "add")

"""#ASSIGNMENT 2
Assignment 2: Based on the above error, modify our calculator function to ensure that the arguments passed when calling the function are integers so that we can perform our operations without any errors

"""

calculator(10, 20, "subtract")
#REMOVE ONE OF "ADD' OR "SUBTRACT" TO  MAKE IT THREE TARGUMENTS INSTEAD OF FOUR

calculator(10, 20, "add")
#REMOVE THE QUOTES FROM THE NUMBER 20 BECAUSE IT MAKES IT A STRING INSTEAD OF AN INTEGER

"""Assignment 3


Create a class called 'Humans' with methods to print the following:

The height of the human
The weight of the human
The Age of the human
The name of the human
Create instances of your class and modify or delete the properties on the objects.

Make the 'name' a private variable. (reading around private and public variables and methods)
"""

def display_height():
  print('The height of the human is 25')

def display_weight():
  print('The weight of the human is 256')

def display_age():
  print('The age of the human is 30')

def display_name():
  print('The name of the human is Halima')

def Humans():
  #display the height of the human
  display_height()
  #display the weight of the human
  display_weight()
  #display the age of the human
  display_age()
  #display the name of the human
  display_name()

Humans()

class Humans:
  def display_name(my_class_instance):
    print("my name is Halima")
  def display_age(my_other_class_instance):
    print("my age is 24")
  def display_height(my_other_other_class_instance):
    print("my height is 25")
  def display_weight(my_other_other_other_class_instance):
    print("my weight is 256")

Human1 = Humans()
Human1.display_name()

Human1.display_age()

Human1.display_height()

Human1.display_weight()