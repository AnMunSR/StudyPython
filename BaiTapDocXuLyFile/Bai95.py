# Bai tap doc ghi file
# Bai 95:
'''

'''

import math

# Nhap du lieu dau vao
a = [0] * 1001  # Tao day so den chi so 1000
a[1] = a[2] = a[3] = 1
for i in range(4, 1001):
    a[i] = a[i - 1] + a[i - 3]
lst = []

# Doc file
f = open('dayso.inp')
while True:
    temp = f.readline()
    if temp == '':
        break
    lst.append(temp)
f.close()

# Ghi file
f1 = open('dayso.out', 'w')
for i in range(0, len(lst)):
    temp = a[int(lst[i])]
    f1.write(str(temp) + '\n')
f1.close()
