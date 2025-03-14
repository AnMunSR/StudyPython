# Bai tap vong lap while
# Bai 42: Day so fibonacci la day so duoc dinh nghia nhu sau: 1, 1, 2, 3, 5, 8, 13,...
#voi 2 so ke tiep bang tong hai so truoc do
# Nhap vao A, hay tim so trong day so fibonacci lon nhat nhung khong vuot qua A


import math
from datetime import datetime

# So fibonacci
def soFibonacci(A):
    if A < 1:
        return 0
    f0 = 1
    f1 = 1
    f2 = 0
    while f2 <= A:
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f0
        


# Nhap du lieu dau vao
A = int(input("Nhap vao so A = "))
print("So fibonacci lon nhat <= A:", soFibonacci(A))
