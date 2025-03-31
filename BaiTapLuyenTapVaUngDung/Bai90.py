# Bai tap luyen tap va ung dung
# Bai 90:
'''
Phong doan COLLATZ
Gia su ta co mot so n
Phong so CoLLATZ hoat dong nhu sau:
Neu n la so chan, thi ta chia n cho 2 (n/2)
Neu n la so le, thi  ta nhan cho 3 roi + 1 (3n + 1)
Phong doan hoat dong cho den khi nao n = 1
Yeu cau: Nhap vao so nguyen duong m, hay in ra day phong doan COLLATZ
tu 1 den m (moi mot phong doan ta in tren 1 dong, moi mot so cach
nhau mot dau phay)
'''

import math


def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

m = int(input("Nhập số nguyên dương m: "))
if m <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    for i in range(1, m + 1):
        print(", ".join(map(str, collatz(i))),end=',')
