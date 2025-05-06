'''
 Viet mot chuogn tirnh chap nhan dau vao la chuoi cac so nhi phan 4 chu
so, phan tach boi dau phay, kiem tra xem chung co chia het cho 5 khong.
Sau do in cac so chia het cho 5 thanh day phan tach boi dau phay
 Vi du dau vao la: 0100,0011,1010,1001
 Dau ra se la: 1010
'''

import math

# Nhap du lieu dau vao
chuoiNhiPhan = [x for x in input("Nhap chuoi nhi phan: ").split(',')]
danhSach = []
for x in chuoiNhiPhan:
    x = x.strip()
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i]) * math.pow(2, len(x) - i - 1)
    if sum % 5 == 0:
        danhSach.append(x)
print(','.join(danhSach))
