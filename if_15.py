a = int (input("1- sonni kiriting: "))
b = int (input("2- sonni kiriting: "))
c = int (input("3- sonni kiriting: "))
if (a > b and b > c):
    print (b, a )
elif (b > a and a > c):
    print (a, b)
elif (c > a and a > b):
    print (a, c)
elif a > c and c > b:
    print(c, a)
elif c > b and b > a:
    print(b, c)
else:
    print (c, b)
