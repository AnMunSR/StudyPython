# Bai tap vong lap for
# Bai 30: Nhap vao so nguyen dong a, dem so uoc cua a



import math
from datetime import datetime

# Ham tinh uoc
def uoc(n):
    count = 0
    for i in range (1 , n + 1):
        if (n % i == 0):
            print(i, end = ' ')
            count += 1
    print("\nSo uoc cua ", a,": ",count)

# Nhap du lieu dau vao
a = int(input("Nhap so nguyen a = "))
uoc(a)
