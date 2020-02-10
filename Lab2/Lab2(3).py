
n = True

while n == True:
 print("Input A and B (A<B) ")

 a = input("Input A: ")
 b = input("Input B: ")

 if a.lstrip('-').isdigit() & b.lstrip('-').isdigit() :
     a = int(a)
     b = int(b)
     if a<b :
         al = range(a,b+1)
         n = False
         print(sorted(al))
         print("Кількість чисел у проміжку : ", len(al))
     else:
         print("Invalid input (A<B)\nTry Again ")

 else:
     print("Invalid input (Input only numbers)\nTry Again ")


