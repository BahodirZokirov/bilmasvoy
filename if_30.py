a = int (input("son kiriting: "))
if a > 1 and a < 1000 and a % 2 == 0:
    if a < 10:
        print ("bir xonali juft ")
    elif a >9 and a < 100:
        print ("iki xonali juft")
    else:
        print ("Uch xonali juft son")
elif a % 2 !=0:
    if a < 10:
        print ("bir xonali toq ")
    elif a >9 and a < 100:
        print ("iki xonali toq")
    else:
        print ("Uch xonali toq")
else:
    print ("Bu son chegaradan tashqarida.")
