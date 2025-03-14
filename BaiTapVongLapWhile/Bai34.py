# Bai tap vong lap while
# Bai 34: Nhap vao so nguyen duong a, neu nhap so am thi yeu cau
#nhap lai cho den khi nguoi dung nhap dung so duong.
# Neu nguoi dung nhap dung so duong thi in ra "Ban nhap dung quy tac"



import math
from datetime import datetime

while True:
    a = int(input("Nhap so nguyen duong a: "))
    if a >= 0:
        break
    else:
        print("So a khong phai la so duong. Yeu cau nhap lai!")