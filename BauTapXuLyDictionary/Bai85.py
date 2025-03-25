# Bai tap xu ly dictionary
# Bai 85:
'''
Viet ham co tham so dau vao la mot dictionary, hay tao mot dictionary moi
hoan doi gia tri va key cua dictionary dau vao, roi tra ve dictionary moi
do. Neu sau khi hoan doi co 2 key trung nhau, ham tra ve None
'''

import math


# Ham hoan doi key va value cua dictionary
def hoanDoiKeyVaValueDict(D):
    D1 = {}
    for i in D:
        D1[D.get(i)] = i
    if len(D1) < len(D):
        return None
    return D1


# Nhap du lieu dau vao
D = {}
n = int(input("Nhap vao so luong phan tu cua dict: "))
for i in range(0, n):
    keyD = input("Nhap key: ")
    valueD = input("Nhap value: ")
    D[keyD] = valueD
print(D)
print("Dict sau khi hoan doi: ", hoanDoiKeyVaValueDict(D))
