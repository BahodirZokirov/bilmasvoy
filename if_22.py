print("nuqta koordinatalarini kiriting: ")
x = int (input("x ni kiriting: "))
y = int (input("y ni kiriting:"))
if x !=0 and y != 0:
    if x > 0 and y > 0:
        print("Birinchi chorak.")
    elif x > 0 and y < 0:
        print("To'rtinchi chorak.")
    elif x < 0 and y > 0:
        print("Ikkinchi chorak.")
    else:
         print("Uchinchi chorak.")
else:
    print ("Bu nuqta o'qlarda yotadi.")
