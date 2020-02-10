from os.path import join

def_str = input("Input string (with multiple spaces): \n")

if not def_str :
    print("Enter anything")
else:
    edited_str = " ".join(def_str.split())
    print("Edited string is: {}".format(edited_str))


