# Bai tap doc ghi file
# Bai 94:
'''

'''

import math


# ham tach chu va so thanh 2 chuoi rieng biet
def tachChuoi(s):
    chuoi = []
    so = []
    for i in range(0, len(s)):
        if s[i].isalpha():
            chuoi.append(s[i])
        else:
            so.append(s[i])
    return chuoi, so


# Nhap du lieu dau vao
s = ""
f = open('chuoi.inp')
while True:
    temp = f.readline()
    if temp == '':
        break
    s = temp
f.close()
chuoiChu, chuoiSo = tachChuoi(s)

f1 = open('chuoi.out','w')
for i in range (0,len(chuoiChu)):
    f1.write(str(chuoiChu[i]))
f1.write("\n")
for i in range (0,len(chuoiSo)):
    f1.write(str(chuoiSo[i]))
f1.close()




