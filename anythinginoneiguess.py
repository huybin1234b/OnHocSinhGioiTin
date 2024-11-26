import math
def giatrituyetdoi(z): 
    giatrituyetdoi = False
    if z < 0 : 
        z = z * -1 
        giatrituyetdoi = True
    else : 
        giatrituyetdoi = True
    return z

a = int(input("nhập số a ")) 
b = int(input("Nhập số b "))
print("giá trị tuyệt đối của a là ", giatrituyetdoi(a))
print("giá trị tuyệt đối của b là ", giatrituyetdoi(b))
print(giatrituyetdoi(a) , "+" , giatrituyetdoi(b) , "=" , giatrituyetdoi(a) + giatrituyetdoi(b))

