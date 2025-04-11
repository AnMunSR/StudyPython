# Bai tap doc ghi file
# Bai 93:
'''

'''

import math

# Ham phan tich thua so nguyen to
def phanTichThuaSoNguyenTo(n):
    i = 2
    thuaSo = []
    while i * i <= n:
        while n % i == 0:
            thuaSo.append(i)
            n //= i
        i += 1
    if n > 1:
        thuaSo.append(n)
    return thuaSo


lst = []
f = open('thuaso.inp')
while True:
    temp = f.readline()
    if temp == '':
        break
    lst.append(int(temp))
f.close()

f1 = open('thuaso.out','w')
for i in range (0,len(lst)):
    templst = phanTichThuaSoNguyenTo(lst[i])
    for j in range(0,len(templst)):
        f1.write(str(templst[j])+" ")
    f1.write("\n")
f1.close()
