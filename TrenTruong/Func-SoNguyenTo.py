import math
def songuyento(n):
    if n<2:
        return False
    uoc = 0
    for i in range(2,n+1):
        if n % i == 0:
            uoc+=1
    if uoc==1:
        return True
    return False
def sosieunguyento(m):
    while m>0:
        if songuyento(m)==False:
            return False
        m=m//10
    return True

def daonguocso(n):
    S = 0
    while n>0:
        S = S * 10 + n % 10
        n = n // 10
    return S
        


n=int(input("nhập số n "))
y=int(input("nhập số y ")) 

for i in range(n,y+1):
    if songuyento(daonguocso(i)) == True:
        print(i)
    
    
    

