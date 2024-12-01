d = int(input("Nhập độ dịch chuyển d | Đơn vị hải lí "))
a = int(input("nhập vận tốc của thuyền về đảo (V1) | Đơn vị Hải lí / Giờ "))
b = int(input("nhập vận tốc của thuyền cứu hộ (V2) "))

print("Thuyền này sẽ gặp nhau vào lúc ", round(d / (a + b), 5 ), "giờ")  


