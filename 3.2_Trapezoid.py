'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
print("Hello!")
b1=int(input("What is the First Base of the Trapezoid?"))
b2=int(input("What is the Second Base of the Trapezoid?"))
h=int(input("What is the Height of the Trapezoid?"))
print("Give me one second...")
print(((b1+b2)/2)*h)