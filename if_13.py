a = int (input("1- sonni kiriting: "))
b = int (input("2- sonni kiriting: "))
c = int (input("3- sonni kiriting: "))
if (a - b > 0 and b - c > 0) or (c - b > 0 and b - a > 0):
    print("o'rtadagi son ", b)
elif (b - a > 0 and a - c > 0) or (c - a > 0 and a - b > 0):
    print("o'rtadagi son ", a)
else:
    print("o'rtadagi son ", c)
