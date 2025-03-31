# Bai tap doc ghi file
# Bai 92:
'''

'''

import math


# Ham chuyen tu nhi phan sang thap phan
def chuyen2Sang10(n):
    tong = int(n,2) # Chuyen chuoi nhi sang thap
    return tong


lst = []
f = open('2to10.inp')
while True:
    temp = f.readline()
    if temp == '':
        break
    lst.append(temp)
f.close()

f1 = open('2to10.out', 'w')
for i in range(0, len(lst)):
    temp = chuyen2Sang10(lst[i])
    f1.write(str(temp) + '\n')
f1.close()
