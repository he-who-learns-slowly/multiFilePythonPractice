from function1 import add
from function2 import sub

choice = input("would you like to run function 1 or 2? ")
a = input("enter number 1: ")
b = input("enter number 2: ")

choice = int(choice)
a = int(a)
b = int(b)
if (choice == 1):
    print(add(a,b))
else:
    print(sub(a,b))
