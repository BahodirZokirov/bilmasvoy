a = int (input("1- sonni kiriting: "))
b = int (input("2- sonni kiriting: "))
c = int (input("3- sonni kiriting: "))
d = int (input("3- sonni kiriting: "))
if (a == b and b == c) or (a == d and a == c) or (c == b and c == d) or (b == a and a == d) or (a == b and b == c and c == d) :
    if a == b and b == c and a != d :
        print (4)
    elif a == b and b == d and a != c:
        print (3)
    elif a == c and c == d and a != b:
        print (2)
    elif b == c and c == d and d != a:
        print (1)
    else:
        print ("To'rtta son o'zar teng.")
else :
    print ("Uchta o'zaro teng son yo'q!!!")
