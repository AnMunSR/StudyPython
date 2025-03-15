# Bai tap xu ly list
# Bai 55:
''' 
Nhap vao mot list so nguyen L, hay kiem tra xem tat ca
cac phan tu trong mang co bang nhau hay khong, neu co 
thi in ra True, khong thi in ra False
'''


# Ham kiem tra co bang nhau khong
def kiemTraBangNhau(L):
    temp = L[0]
    for i in range(1,len(L)):
        if L[i] != temp:
            return False
    return True


L = []
n = int(input("Nhap vao so luong phan tu cua L: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    L.append(i)
print("Danh sach L: ",L)
if kiemTraBangNhau(L):
    print("True")
else:
    print("False")



