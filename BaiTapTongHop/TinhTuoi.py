'''
Tinh tuoi dua tren ngay thang nam sinh nhap vao
VD: Nhap vap ngay thang nam sinh dang y/m/d, hay tinh tuoi cua nguoi nay
'''

from datetime import datetime

while True:
    ngaySinh = input("Nhap vao ngay thang nam sinh: ")
    try:
        ngaySinh = datetime.strptime(ngaySinh,"%d/%m/%Y")
        break
    except ValueError:
        print("Ngay sinh khong hop le. Vui long nhap lai")

print("Tuoi hien tai: ",end=' ')
namHienTai = datetime.today().year
namSinh = ngaySinh.year
print(namHienTai - namSinh)


