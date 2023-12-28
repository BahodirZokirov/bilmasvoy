a = int (input("1- sonni kiriting: "))
b = int (input("2- sonni kiriting: "))
c = int (input("3- sonni kiriting: "))
if (a > b and b > c):
    print (c, a )
elif (b > a and a > c):
    print (c, b)
elif (c > a and a > b):
    print (b, c)
elif a > c and c > b:
    print(b, a)
elif c > b and b > a:
    print(a, c)
else:
    print (a, b)
