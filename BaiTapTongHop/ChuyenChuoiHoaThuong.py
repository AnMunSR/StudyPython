'''
 Viet mot chuong trinh chap nhan chuoi la cac dong duoc nhap vao, chuyen
cac dong nay thanh chu in hoa va in ra man hinh.
 Gia su dau vao la:
Hello world
Practice makes perfect
 Thi dau ra se la:
HELLO WORLD
PRACTICE MAKES PERFECT
'''


# Nhap du lieu dau vao
danhSach = []
while True:
    s = input("Nhap chuoi: ")
    if s:
        danhSach.append(s.upper())
    else:
        break
for i in danhSach:
    print(i)
