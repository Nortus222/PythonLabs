
from math import *

print("Input x: ")
x = float(input())
print("Input y: ")
y = float(input())
numerator = exp(2*x) + sin(y)
denomenator = log(3.8 * x + y)
print(denomenator)
print(numerator)

if denomenator != 0 :
    print(numerator/denomenator)
else:
    print("Entered values is unusable")
