a = int (input("1- sonni kiriting: "))
b = int (input("2- sonni kiriting: "))
c = int (input("3- sonni kiriting: "))
if (a > b and b > c) or (b > a and a > c):
    print ("eng kichik son ", c)
elif (c > a and a > b) or a > c and c > b:
    print ("eng kichik son ", b)
else:
    print ("eng kichik son ", a)
