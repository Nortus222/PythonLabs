
from math import *

n = True

while n == True :

 x = input("Input X: ")
 y = input("Input Y: ")

 if x.lstrip('-').replace('.','',1).isdigit() & y.lstrip('-').replace('.','',1).isdigit() :
    x = float(x)
    y = float(y)

    numerator = exp(2*x) + sin(y)

    if 3.8 * x + y > 0:
        denomenator = log(3.8 * x + y)

        if denomenator != 0:
            print("R = ", round(numerator/denomenator,2))
            n = False
        else:
            print("Entered values is unusable\nTry again")

    else:
        print("Entered values is unusable\nTry again")
 else:
     print("Entered values is unusable (Must be numbers)\nTry again ")




