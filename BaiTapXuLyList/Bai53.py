# Bai tap xu ly list
# Bai 53:
''' 
Nhap vao mot list so nguyen L, tim va in ra gia tri lon nhat
'''


lst = []
n = int(input("Nhap vao so luong phan tu cua list: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    lst.append(i)

print("Lst chua sap xep: ", lst)

# Tim phan tu lon nhat
for i in range(0,n-1):
    for j in range (i+1, n):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j], lst[i]

print("Lst sau khi da sap xep: ",lst)
print("Phan tu lon nhat trong lst: ",lst[len(lst)-1])