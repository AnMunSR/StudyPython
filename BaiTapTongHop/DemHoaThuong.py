'''
 Viet mot chuong trinh chap nhan dau vap la mot cau, dem chu hoa, thuong
 Gia su dau vao la: Quan Tri Mang
 Dau ra:
    Chu hoa: 3
    Chu thuong: 8
'''

# Nhap du lieu dau vao
s = input("Nhap chuoi dua vao: ")
chuHoa = 0
chuThuong = 0
for x in s:
    if x.isupper():
        chuHoa += 1
    elif x.islower():
        chuThuong += 1
    else:
        continue
print("Chu hoa: ", chuHoa)
print("Chu thuong: ", chuThuong)
