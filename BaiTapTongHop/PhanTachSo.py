'''
Viet chuong trinh chap nhan mot chuoi so, phan tach bang dau phay tu giao
dien dieu khien, tao ra mot danh sach va mot tuple chua moi so
'''

# Nhap du lieu dau vao
str = input("Nhap chuoi so dau vao: ")
data = str.split()
print(data)
tup = tuple(data)
print(tup)
print(type(data))
print(type(tup))