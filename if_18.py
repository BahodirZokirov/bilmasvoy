a = float (input("1- sonni kiriting: "))
b = float (input("2- sonni kiriting: "))
c = float (input("3- sonni kiriting: "))
if a == b or a == c or c == b:
    if a == b:
        print (3)
    elif a == c:
        print (2)
    else:
        print (1)
else :
    print ("Ikkita o'zaro teng son yo'q!!!")
