# Bai tap vong lap while
# Bai 37: Nhap mot day so nguyen, ngung nhap khi nguoi 
#dung nhap -1
# Sau khi nhap xong, in ra so lon nhat, nho nhat trong nhung so vua nhap


import math
from datetime import datetime

# Nhap du lieu dau vao
listA = []
while True:
    a = int(input("Nhap phan tu: "))
    if a == -1:
        break
    listA.append(a)

print(listA)
listA.sort()
print("So lon nhat: ",listA[len(listA)-1])
print("So nho nhat: ",listA[0])