# Bai tap xu ly list
# Bai 54:
''' 
Nhap vao mot list so nguyen L, nhap vao 2 so nguyen 
duong a va b (a < b < len(L)).
Tim va in ra so nho nhat trong list tu vi tri a den
vi tri b
'''

L = []
n = int(input("Nhap vao so luong phan tu cua L: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

while True:
    a = int(input("Nhap vao so a: "))
    b = int(input("Nhap vao so b: "))
    if a < b < len(L):
        break


# Tim phan tu nho nhat
minA = L[a]
for i in range(a+1,b+1):
    if L[i] < minA:
        minA = L[i]


print("Danh sach L: ",L)
print("Phan tu nho nhat trong doan ({0},{1}) la {2}".format(a,b,minA))