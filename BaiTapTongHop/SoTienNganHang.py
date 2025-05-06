'''
 Viet chuong trinh tinh so tien thuc cua mot tai khoan ngan hang dua
tren nhat ki giao dich duoc nhap vao tu giao dien dieu khien
 Dinh dang nhat ki duoc hien thi:
    D 100
    W 200
(D la tien gui, W la tien rut ra)
'''

# Nhap du lieu dau vao
tongSoTien = 0

while True:
    s = input("Nhap nhat ki giao dich: ")
    if not s:
        break
    values = s.split(' ')
    kiTu = values[0]
    soTien = int(values[1])
    if kiTu == 'D':
        tongSoTien += soTien
    elif kiTu == 'W':
        tongSoTien -= soTien
    else:
        continue
print("Tong so tien trong tai khoan: ",tongSoTien)