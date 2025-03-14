# Bai tap vong lap while
# Bai 35: Nhap n. Cho S(k) = 1 + 2 + 3 +...+ k
# Tim k so cho S(k) lon nhat nhung nho hon n



import math
from datetime import datetime

# Ham tim k
def timK(n):
    k = 0
    s = 0
    while(s + k + 1 < n):
        k += 1
        s += k
    return k

# Nhap du lieu dau vao
n = int(input("Nhap n = "))
print("S(k) lon nhat nhung nho hon n ung voi k = ", timK(n))