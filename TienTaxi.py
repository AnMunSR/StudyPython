# Tinh tien taxi
'''
Neu di tren 120km se duoc giam 10% tren tong so tien
Thue gia tri gia tang la 5% tren tong so hoa don
So tien tra ve duoc lam tron den hang don vi
a. Viet ham taxi_bill(km) de tinh va tra ve so tien di taxi tuong ung voi so
km cho truoc
b. Viet chuong trinh nhap vao chi so km, sau do in ra so tien taxi phai tra
'''


def taxi_bill(km):
    soTien = 0
    if km < 0:
        return soTien
    elif km <= 0.3:
        soTien = 20000 * km
    elif km > 0.3 and km <= 3:
        soTien = 20000 * 0.3 + 18600 * (km - 0.3)
    elif km > 3 and km <= 11:
        soTien = 20000 * 0.3 + 18600 * (3 - 0.3) + 14200 * (km - 3)
    elif km > 11 and km <= 20:
        soTien = 20000 * 0.3 + 18600 * (3 - 0.3) + 14200 * (11 - 3) + 13000 * (km - 11)
    elif km > 20 and km <= 30:
        soTien = 20000 * 0.3 + 18600 * (3 - 0.3) + 14200 * (11 - 3) + 13000 * (20 - 11) + 12000 * (km - 20)
    else:
        soTien = 20000 * 0.3 + 18600 * (3 - 0.3) + 14200 * (11 - 3) + 13000 * (20 - 11) + 12000 * (30 - 20) + 11000 * (
                km - 30)
    if km > 120:
        soTien = soTien * 0.9
    soTien = soTien + soTien * 0.05
    return round(soTien)

# Nhap du lieu dau vao
km = float(input("Nhap so km di duoc: "))
tongTien = taxi_bill(km)
print("Tong tien taxi: ",tongTien,"VND")
