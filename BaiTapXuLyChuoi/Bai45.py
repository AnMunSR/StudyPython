# Bai tap xu ly chuoi
# Bai 45: Nhap vao mot chuoi co dang 3 so nguyen, moi so nguyen cach nhau 1 dau phay
# Tinh tong 3 so nguyen do



import math
from datetime import datetime

s = input("Nhap chuoi s = ")
i = 0
tong = 0
lists = s.split(',')
print(lists)
for i in lists:
    tong += int(i)
print("Tong 3 chu so: ", tong)

