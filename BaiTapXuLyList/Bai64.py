# Bai tap xu ly list
# Bai 64:
''' 
Nguoi ta dinh nghia mot list so nguyen la list chan le,
neu nhu tong 2 phan tu bat ky ben torng list deu la so chan.
Nhap vao mot list so nguyen L va kiem tra xem L co phai
list chan le hay khong
'''

import math

# Ham kiem tra list chan le
def kiemTraListChanLe(L):
    if all(x % 2 == 0 for x in L) or all(x % 2 == 1 for x in L):
        return True
    return False

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
if kiemTraListChanLe(L):
    print("List chan le")
else:
    print("Khong phai list chan le")


