import os
import shutil
import re
import pickle
import shelve


cwd = os.getcwd()
home = "/Users/igor/"

os.chdir(home)

print("1", "-"*60)

try:
    os.mkdir("Lab7")
    print("Folder {} created".format(os.path.abspath("Lab7")))
except FileExistsError:
    print("Folder {} already exist".format(os.path.abspath("Lab7")))

os.chdir(os.path.abspath("Lab7"))


print("2", "-"*60)

try:
    os.mkdir("Sherstiuk")
    print("Subfolder {} created".format(os.path.abspath("Sherstiuk")))
except FileExistsError:
    print("Subfolder {} already exist".format(os.path.abspath("Sherstiuk")))

os.chdir(os.path.abspath("Sherstiuk"))


print("3 ", "-"*60)

try:
    shutil.copyfile(home + "PycharmProjects/for_lab_7/1.txt", os.path.abspath("Sherstiuk") + "/1.txt")
    print("File copied")
except OSError:
    print("Failed to copy file")

os.chdir("/Users/igor/Lab7/Sherstiuk/")

f = open(os.path.abspath("1.txt"), "rb")
b = os.path.getsize(os.path.abspath("1.txt"))
a = int(b/3)

print("File {0} size - {1}".format(f.name, b))


f1 = open("1part1.txt", 'wb')

tmp1 = f.read(a)

f1.write(tmp1)
print("File {} size - {} ".format(f1.name, os.path.getsize("1part1.txt")))

f1.close()

f2 = open("1part2.txt", 'wb')
f2.write(f.read(a))
print("File {} size - {} ".format(f2.name, os.path.getsize("1part2.txt")))
f2.close()

f3 = open("1part3.txt", 'wb')
f3.write(f.read(a))
print("File {} size - {} ".format(f3.name, os.path.getsize("1part3.txt")))
f3.close()

f.close()

fn = open(os.path.abspath("1.txt"), "r", encoding="cp1251")

startStr = int(input("Enter number of line to start reading: "))
numStr = int(input("Enter number of lines to read: "))
finStr = startStr + numStr
i = startStr

p = re.compile(r"(?<=[\.?!])(.*?)(?=[\.?!])", re.S | re.I | re.DOTALL)

fnew = open("result.txt", "w", encoding="utf-8")

arr = p.findall(fn.read())

while i < finStr:
    if arr[i] == '' or arr[i] == '.':
        i += 1
        finStr += 1
    else:
        fnew.write(arr[i])
        i += 1

fnew.close()
fn.close()


print("4 ", "-"*60)

os.chdir(home)

try:
    os.mkdir("Lab5")
    print("Folder {} created".format(os.path.abspath("Lab5")))
except FileExistsError:
    print("Folder {} already exist".format(os.path.abspath("Lab5")))

menu = {"Island Duck": 103, "Fried Eggs": 30, "Lamb Salad": 45, "Smoked Pork": 78, "Pasta": 55, "fried chicken": 50}

f = open("/Users/igor/Lab5/lab5.txt", "wb")
pickle.dump(menu, f)
f.close()

f = open("/Users/igor/Lab5/lab5.txt", "rb")
a = pickle.load(f)
a["Pork salad"] = 60

fn = open("/Users/igor/Lab5/lab5New.txt", "wb")
pickle.dump(a, fn)
f.close()
fn.close()

print("5 ", "-"*60)

os.chdir(home)

try:
    os.mkdir("Lab6")
    print("Folder {} created".format(os.path.abspath("Lab6")))
except FileExistsError:
    print("Folder {} already exist".format(os.path.abspath("Lab6")))

menu = {"Island Duck": 30, "Fried Eggs": 13, "Lamb Salad": 26, "Smoked Pork": 37, "Pasta": 18, "Fried chicken": 29,
        "Avocado Toast & Poached Eggs": 15,"Specialty Bread Sample Plate": 14, "Smoked Salmon Platter": 22,
        "Steel Cut Oatmeal": 12, "Yogurt Parfait": 7, "Creamy Tomato": 16, "Baby Green Salad": 11,
        "Chopped Salad": 10, "Chicken Papaya Salad": 9, "Avocado Toast & House Salad": 12, "Roasted Turkey Breast": 22,
        "Classic French Tuna Salad": 25, "Grilled Cheese & Tomato Soup": 19, "Turkey Pesto": 27,
        "Roasted Eggplant Italiano": 8}

with shelve.open("/Users/igor/Lab6/lab_6") as db:
    db.update(menu)

try:
    shutil.move("lab_6", "/Users/igor/Lab6/lab_6")
except FileNotFoundError:
    print("File not found")

with shelve.open("/Users/igor/Lab6/lab_6") as db:

    try:
        db.pop("Island Duck")
    except KeyError:
        print("No key found")

    db["Toasts"] = 8
    db.update({"Mashed potato": 12})
    print("Database: {}".format(list(db.items())))


os.chdir(cwd)
