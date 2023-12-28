a = float (input("1- sonni kiriting: "))
b = float (input("2- sonni kiriting: "))
c = float (input("3- sonni kiriting: "))
if (a < b and b < c) or (c < b and b < a) :
    print(2*a, 2*b, 2*c)
else :
    print(-a, -b, -c)
print (a, b, c)
