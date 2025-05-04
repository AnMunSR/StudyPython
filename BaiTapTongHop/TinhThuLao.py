'''
Viet chuong trinh nhap: so gio lam moi tuan, thu lap tren moi gio lam tieu
chuan, tu do tinh ra so tien thuc linh cua nhan vien. Biet rang: so gio tieu
chuan moi tuan la 44 gio, va moi gio vuot chuan duoc tra gap ruoi so voi gio
lam chuan
'''

# Nhap du lieu dau vao
soGioLam = float(input("Nhap so gio lam: "))
thuLaoTheoGio = float(input("Nhap thu lao theo gio: "))
luong = 0
if soGioLam <= 44:
    luong = soGioLam*thuLaoTheoGio
else:
    luong = 44 * thuLaoTheoGio + (soGioLam - 44) * thuLaoTheoGio * 2
print("Luong: ",luong)