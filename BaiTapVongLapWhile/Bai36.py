# Bai tap vong lap while
# Bai 36: Nhap vao A, tim n nho nhat sao cho:
# 1 + 1/2 + 1/3 +...+ 1/n > A



import math
from datetime import datetime

# Ham tim n
def timN(A):
    s = 0
    n = 1
    while s <= A:
        s += 1/n
        n += 1
    return n - 1

# Nhap du lieu dau vao
A = float(input("Nhap A = "))
print("n nho nhat la: ",timN(A))