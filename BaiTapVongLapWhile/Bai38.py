# Bai tap vong lap while
# Bai 38: Nhap vao so nguyen duong n, dem xem n co bao nhieu chu so


import math
from datetime import datetime

# Ham dem so luong chu so trong n
def demSoLuong(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# Nhap du lieu dau vao
n = int(input("Nhap vao so n = "))
print("So luong chu so trong ", n, " la: ", demSoLuong(n))
