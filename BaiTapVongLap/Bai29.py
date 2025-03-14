# Bai tap vong lap for
# Bai 29: Nhap so nguyen duong a, in toan bo uoc cua a



import math
from datetime import datetime

# Ham tinh uoc
def uoc(n):
    for i in range (1 , n + 1):
        if (n % i == 0):
            print(i, end = ' ')

# Nhap du lieu dau vao
a = int(input("Nhap so nguyen a = "))
uoc(a)
