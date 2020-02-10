
def_str = bytearray(input("Input string with 's' or '#s' symbols: \n"), "UTF -8")

if not def_str:
    print("Enter something")
else:
    if (def_str.islower()) & ((b"s" in def_str) | (b"#s" in def_str)):
        print("Edited string is: {}".format(def_str.replace(b"#s", b"#").replace(b"s", b"#s").decode("UTF -8")))
    elif (b"s" in def_str) | (b"#s" in def_str) | (b"S" in def_str) | (b"#S" in def_str):
        print("Edited string is: {}".format(def_str.replace(b"#s", b"#").replace(b"s", b"#s").replace(b"#S", b"#").replace(b"S", b"#S").decode("UTF -8")))
    else:
        print("Enter string with 's' or '#s' symbols")







