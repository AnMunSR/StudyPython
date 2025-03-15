# Bai tap xu ly list
# Bai 57:
''' 
Nhap vao mot List, hay tim va in ra gia tri am lon
nhat trong L, neu L khong co gia tri am thi in ra 0
'''


# Ham tim gia tri am lon nhat
def timGiaTriAmLonNhat(L):
    temp = 0
    for i in range(0, len(L)):
        if temp == 0:
            if L[i] < temp:
                temp = L[i]
        elif L[i] < 0 and L[i] > temp:
            temp = L[i]
    return temp


L = []
n = int(input("Nhap vao so luong phan tu cua L: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    L.append(i)
print("Danh sach L: ",L)
if timGiaTriAmLonNhat(L) == 0:
    print("Khong co gia tri am trong L")
else:
    print("Gia tri am lon nhat la: ", timGiaTriAmLonNhat(L))




