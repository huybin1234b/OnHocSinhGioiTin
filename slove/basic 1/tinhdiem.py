# đây là bài giải của problem Screenshoot (632).png
r = int(input("Viết thứ hạng của bạn ở đây ")) 
if 0 > r <= 10 : 
    point = 10
elif 11 >= r < 21 : 
    point = 9
else :
    point = 0
print("Bạn được ", point, "điểm")