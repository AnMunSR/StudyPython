# Bai tap vong lap while
# Bai 41: Nhap vao mot so nguyen duong n, kiem tra xem n co phai so dang 2^k hay khong

import math
from datetime import datetime

# Ham kiem tra n co phai dang 2^k
def kiemTra(n):
    if n <= 0:
        return False
    while True:
        if n % 2 != 0:
            return False
        n //= 2
        if n == 1:
            return True

# Nhap du lieu dau vao
n = int(input("Nhap vao so n = "))
if kiemTra(n) == True:
    print(n,"co dang 2^k")
else:
    print(n,"khong co dang 2^k")
