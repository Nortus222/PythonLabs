
import sys


def row(a):
    menu_1 = list(menu.items())

    if a == 0:
        menu_1.sort(key=lambda i: str(i[a]).lower())
    else:
        menu_1.sort(key=lambda i: i[a])

    return menu_1


menu = {"Island Duck": 103, "Fried Eggs": 30, "Lamb Salad": 45, "Smoked Pork": 78, "Pasta": 55,"fried chicken": 50}
print(sys.path)
a = input("Enter 0 to sort by names or 1 to sort by prices: ")
print("Original dictionary is : {}".format(menu))

if a.isdigit():
    a = int(a)
else:
    print("Enter digit\n")

if (a == 1) | (a == 0):
    print("\nSorted dictionary is : \n")
    for i in row(a):
        print("{0}: {1}".format(i[0], i[1]))
else:
    print("Enter 0 or 1\n")



