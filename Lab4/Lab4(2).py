import random
import numpy

print("\nSet matrix M x N")
m = input("Enter m: ")
n = input("Enter n: ")

if n.isdigit() & m.isdigit():
    m = int(m)
    n = int(n)
    a = [[0] * n for i in range(m)]
    a_1 = a.copy()

    for i in range(m):
        for j in range(n):
            a[i][j] = random.randint(0, 10)

    for i in range(m):
        a_new = set(a[i])

        if len(a_new) != len(a[i]):
            a_1.remove(a[i])

    print("\nOriginal matrix \n {0}\nEdited matrix \n {1}".format(numpy.array(a), numpy.array(a_1)))

else:
    print("M x N must be integer\nTry again")

