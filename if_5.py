a = int (input("1 - sonni kiriting:"))
b = int (input("2 - sonni kiriting:"))
c = int (input("3 - sonni kiriting:"))
if a > 0 and b > 0 and c > 0:
    print ("Uchalasi ham musbat")
elif (a > 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c > 0):
    print("ikkitasi musbat, bitta manfiy")
elif (a > 0 and b < 0 and c < 0) or (a < 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c < 0):
    print("bittasi musbat, ikkita manfiy")
else:
     print ("Uchalasi ham manfiy")
