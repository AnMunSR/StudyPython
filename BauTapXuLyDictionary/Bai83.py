# Bai tap xu ly dictionary
# Bai 83:
'''
Viet ham dua vao 1 dictionary co cac phan tu co key la chuoi, tim va
tra ve gia tri cua key co do dai lon nhat
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
    if len(i) > len(maxKey):  # Ham .get(): lay value trong dict1 ung voi key i
        maxValue = dict1.get(i)
        maxKey = i
print("Phan tu co key lon nhat la: Key : {0} va Value : {1}".format(maxKey, maxValue))
