# Bai tap vong lap for
# Bai 28: nhap vao n. Tinh S = 1 + 2 + 3 +...+ nn



import math
from datetime import datetime

# Ham tinh tong S = 1 + 2 + 3 +...+n
def tinhTong(n):
    s = 0
    for i in range (1 , n + 1):
        s += i
    return s

# Nhap du lieu dau vao
n = int(input("Nhap so nguyen n = "))
print("Tong = ", tinhTong(n))
