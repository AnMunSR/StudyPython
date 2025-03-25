# Bai tap xu ly dictionary
# Bai 84:
'''
Viet ham co tham so dau vao la mot list L co cac phan tu la chuoi.
Hay tao mot dictionary D ma hoa, voi moi mot phan tu trong L duoc
ma hoa thanh mot con so (theo thu tu tu 0 tang dan len 1 don vi). Sau
do tra ve list da duoc ma hoa
'''

import math


# Ham tao mot dictionary D ma hoa
def taoDict(L):
    D = {}
    n = len(L)
    count = 0
    # Xay dung dictionary ma hoa
    for i in range(0, n):
        if not L[i] in D:  # Tim L[i] co phai la key trong D hay khong
            D[L[i]] = count
            count += 1
    print(D)

    # Xay dung list ma hoa
    L_maHoa = L
    for i in range(0, n):
        if L_maHoa[i] in D:
            L_maHoa[i] = D.get(L_maHoa[i])
    return L_maHoa


# Nhap du lieu dau vao
L = ["den", "vang", "xanh", "vang", "xanh", "do", "hong"]
print(taoDict(L))
