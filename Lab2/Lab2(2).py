
n = True

while n == True :

 a = input("Input A: ")
 b = input("Input B: ")
 if a.lstrip('-').replace('.','',1).isdigit() & b.lstrip('-').replace('.','',1).isdigit() :
     a = float(a)
     b = float(b)
     n = False
     print("Сума квадратів = ", a**2 + b**2)
     print("Квадрат суми = ", (a + b)**2)

     if a**2 + b**2 > (a + b)**2:

         print("Сума квадратів більше ніж квадрат суми")

     elif a**2 + b**2 < (a + b)**2:

         print("Сума квадратів меньша ніж квадрат суми")

     else:

         print("Сума квадратів дорівнює квадрату суми")

 else :
    print("Invalid input (Input only numbers)\nTry again ")


