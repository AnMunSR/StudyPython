# Bai tap vong lap while
# Bai 39: Nhap vao so nguyen duong n, dem xem n co bao nhieu
#chu so chan, bao nhieu chu so le


import math
from datetime import datetime

# Ham dem so luong chu so chan, le trong n
def demSoLuong(n):
    le = 0
    chan = 0
    while n > 0:
        temp = n % 10
        if temp % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    return le, chan

# Nhap du lieu dau vao
n = int(input("Nhap vao so n = "))
print("So luong chu so le, chan trong ", n, " la: ", demSoLuong(n))
