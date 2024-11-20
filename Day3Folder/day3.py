# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# print("hello from day3")
# name=input("What is ur name?")
# print("Welcome back " +name+"!")   

# num1=int(input("What is the first number to add?"))
# num2=int(input("what is the second number to add?"))

# ans=(num1)+(num2)

# print(" The sum of "+ str(num1)+ " +" + str(num2) + " = "+ str(ans))

# name=input(" What is ur name mister ")
# number=input(" How many pens are u buying my dear customer? " )

# print( name + " bought " + number +"pens.")



# num1=input("What is number 1?")
# num2=input("What is number 2?")

# print(int(num1)*int(num2))


mister1=int(input("what is ur age frfr?"))
miss2=int(input("What is ur age miss frfr"))

if mister1 >= miss2:
    print("pls take care of ur queen")

if mister1<=miss2:
    print("pls take care of mister")
     
     
import random

randomnumber=random.randint(1,2)
usersguess=int(input("guess a number between 1 to 2:"))

if usersguess== randomnumber:
    print("that is very sigma baby of u!")
else:
    print("u are wrong mister u will see ur blood dripping down")