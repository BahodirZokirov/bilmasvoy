a = int (input("A nuqtani kiriting: "))
b = int (input("B nuqtani kiriting: "))
c = int (input("C nuqtani kiriting: "))
if abs(a - b) < abs(a - c):
    print(f"A nuqtaga eng yaqin nuqta B, orasidagi masofa {abs(a-b)}")
elif abs(a - b) == abs(a - c):
    print(f"A nuqta B va C nuqtalardan baravar uzoqlikda. or.mas {abs(a-b)}")
else:
    print(f"A nuqtaga eng yaqin nuqta C, orasidagi masofa {abs(a-c)}")
