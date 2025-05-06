'''
 Viet mot chuong trinh chap nhan dau vao la mot chuoi cac tu tach biet boi
khoang trang, loai bo cac tu trung lap, sap xep theo thu tu bang chu cai
roi in chung
 Gia su dau vao la: hello world and practice makes perfect and hello world again
 Thi dau ra la: again and hello makes perfect practice world
'''

# Nhap du lieu dau vao
chuoi = [x for x in input("Nhap chuoi dau vao: ").split(' ')]
danhSach = sorted(list(set(chuoi)))
print(' '.join(danhSach))

