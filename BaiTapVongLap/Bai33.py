# Bai tap vong lap for
# Bai 33: Nhap vao so nguyen duong a, kiem tra xem a co phai la so nguyen to hay khong



import math
from datetime import datetime

# Ham kien tra so nguyen to
def kiemTraSoNguyenTo(a):
    if (a < 1):
        return False
    if (a == 2): 
        return True
    for i in range (2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

# Nhap du lieu dau vao
a = int(input("Nhap so nguyen a = "))
if kiemTraSoNguyenTo(a) == True:
    print(a," la so nguyen to!")
else:
    print(a," Khong phai la so nguyen to")