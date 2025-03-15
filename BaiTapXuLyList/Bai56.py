# Bai tap xu ly list
# Bai 56:
''' 
Nhap vao mot list so nguyen L, tim va in ra gia tri
duong dau tien cua list, neu khong co gia tri duong
in ra -1
'''


# Ham tim gia tri duong dau tien
def timGiaTriDuongDauTien(L):
    temp = 0
    for i in range(0, len(L)):
        if L[i] > temp:
            return i
    return -1


L = []
n = int(input("Nhap vao so luong phan tu cua L: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    L.append(i)
print("Danh sach L: ",L)
print("Vi tri chua gia tri duong dau tien la: ", timGiaTriDuongDauTien(L))




