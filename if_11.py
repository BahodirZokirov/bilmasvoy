a = int (input("1 - sonni kiriting:"))
b = int (input("2 - sonni kiriting:"))
if a - b > 0:
    if a - b == 0:
        print (0)
    else:
        print (f"a = {a}, b = {a}")
else:
    if a - b == 0:
        print (0)
    else:
        print (f"a = {b}, b = {b}")
print(a, b)
