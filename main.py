from function1 import add
from function2 import sub
from function3 import test

choice = input("would you like to run function 1, 2, or 3? ")
a = input("enter number 1: ")
b = input("enter number 2: ")

choice = int(choice)
a = int(a)
b = int(b)
if (choice == 1):
    print(add(a,b))
elif choice == 3:
    print(test(a,b))
else:
    print(sub(a,b))
