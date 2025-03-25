# Bai tap xu ly dictionary
# Bai 82:
'''
Viet ham dua vao 1 dictionary co cac phan tu la so nguyen, tim va
tra ve key co gia tri lon nhat
'''

import math

# Nhap du lieu dau vao
dict1 = {}
n = int(input("Nhap so luong phan tu cua dictionary: n = "))
for i in range(0, n):
    k = input("Nhap key: ")
    v = int(input("Nhap value: "))
    dict1[k] = v

print(dict1)

maxValue = next(iter(dict1.values()))  # Lay value cua phan tu dau tien trong dict
maxKey = next(iter(dict1.keys()))  # Lay key cua phan tu dau tien trong dict
for i in dict1:
    if dict1.get(i) > maxValue:  # Ham .get(): lay value trong dict1 ung voi key i
        maxValue = dict1.get(i)
        maxKey = i
print("Phan tu lon nhat co key la {0} va value {1}".format(maxKey, maxValue))
