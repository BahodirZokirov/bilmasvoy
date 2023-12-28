print("nuqta koordinatalarini kiriting: ")
x = int (input("x ni kiriting: "))
y = int (input("y ni kiriting:"))
if x == 0 and y == 0:
    print(0)
elif x != 0 and y == 0:
    print(1)
elif x == 0 and y != 0:
    print(2)
else:
    print(3)
