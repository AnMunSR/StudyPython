'''
Viet chuong trinh va in gia tri theo cong thuc cho truoc: Q = can([(2*C*D)/H]).
Voi gia tri co dinh cua C la 50, H la 30. D la day gia tri tuy bien duoc nhap
vao tu giao dien nguoi dung, cac gia tri cua D duoc phan cac bang dau phay
VD: gia su chuoi gia tri cua D nhap vap la 100, 150, 180 thi dau ra se la 18, 22, 24
'''

import math


# Nhap du lieu dau vao
C = 50
H = 30
D = [i for i in input("Nhap gia tri dau vao cho D: ").split(',')]

value = []
for i in D:
    temp = int(round(math.sqrt((2*C*float(i))/H)))
    value.append(temp)
print(value)
