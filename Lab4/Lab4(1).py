import random

n = input("Enter the length of the list : ")

if n.isdigit():
    n = int(n)
    a = random.sample(range(100), n)
    b = random.sample(range(100), n)
    c = [i for i in range(0, n)]

    for i in range(0, len(a)):
        if b.index(b[i]) % 2 == 0:
            c[i] = b[i]

        if a.index(a[i]) % 2 != 0:
            c[i] = a[i]

    print("a list - {0}\nb list - {1}\n\nc list - {2}".format(a, b, c))

    if n % 2 == 0:
        c = "".join(str(random.sample(range(100), int(n/2))).lstrip("[").rstrip("]"))

        print("\nnew c str list - {}".format(c))

    else:
        c = "".join(str(random.sample(range(100), int(n / 2))).lstrip("[").rstrip("]"))
        print("""You entered odd number ,so the length of the list will be rounded 
        to less number\nNew c str list - {}""""".format(c))
else:
    print("The length must be integer\nTry again")

