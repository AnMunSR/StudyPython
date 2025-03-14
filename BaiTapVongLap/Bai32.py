# Bai tap vong lap for
# Bai 32: Nhap vao so nguyen duong a va b, in toan bo uoc chung cua a va b 



import math
from datetime import datetime

# Ham tim toan bo uoc chung cua a va b
def uoc(a, b):
    dich = min(a,b)
    for i in range (1 , dich + 1):
        if (a % i == 0) and (b % i == 0):
            print(i, end = ' ')

# Nhap du lieu dau vao
a = int(input("Nhap so nguyen a = "))
b = int(input("Nhap so nguyen b = "))
uoc(a,b)