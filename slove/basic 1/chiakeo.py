# đây là bài tập của file Screenshoot(631).png 
def sapxepso(a,b,c) : 
    if a>b and a>c :
        if b>c :
            return a,b,c
        else:
            return a,c,b
    elif b>a and b>c :
        if a>c :
            return b,a,c
        else:
            return b,c,a
    else:
        if a>b :
            return c,a,b
        else:
            return c,b,a

a = int(input())
b = int(input())
c = int(input())
a,b,c = sapxepso(a,b,c)
print(a,b,c)
print(a - b -c)
