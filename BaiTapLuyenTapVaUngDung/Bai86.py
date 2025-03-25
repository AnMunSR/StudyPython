# Bai tap luyen tap va ung dung
# Bai 86:
'''
Mot cua hang co cac mon an: Ga ran, Hamburder, CocaCola
Gia cua ga ran la: 30.000d
Gia cua hamburger la: 25.000d
Gia cua cocacola la: 10.000d
Yeu cau nguoi dung nhap vao so luong tung mon an
Sau do in ra hoa don theo dang sau
'''

import math


# Ham in hoa don
def inHoaDon(gaRan, hamburger, cocacola):
    print("Hóa đơn: ")
    print("Gà rán:\t 30.000d x {0}".format(gaRan))
    print("Hamburger:\t 25.000d x {0}".format(hamburger))
    print("Cocacola: \t 10.000d x {0}".format(cocacola))
    print("\nTổng:")
    tongG = 30000 * gaRan
    ftongG = f"{tongG:,} ₫"
    tongH = 25000 * hamburger
    ftongH = f"{tongH:,} ₫"
    tongC = 10000 * cocacola
    ftongC = f"{tongC:,} ₫"
    tong = tongG + tongH + tongC
    ftong = f"{tong:,} ₫"
    thue = tong * 0.05
    fthue = f"{thue:,} ₫"
    tongChung = tong + thue
    ftongChung = f"{tongChung:,} ₫"
    print("Gà rán\t", ftongG)
    print("Humburger\t", ftongH)
    print("Cocacola\t", ftongC)
    print("Tổng trước thuế\t ", ftong)
    print("Thuế(5%)\n", fthue)
    print("Tổng sau thuế\t", ftongChung)


# Nhap du lieu dau vao
print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
print("Mời bạn nhập số lượng từng món ăn: \n")
gaRan = int(input("Gà rán: "))
hamburger = int(input("Hamburger: "))
cocacola = int(input("Cocacola: "))
inHoaDon(gaRan, hamburger, cocacola)
