# Bai tap lap trinh dieu khien
# Bai 20: Nhap vao thang, nam. In ra thang co bao nhieu ngay

import math
nam = int(input("Nhap nam: "))
thang = int(input("Nhap thang: "))
if thang in [1,3,5,7,8,10,11]:
    print("Thang co 31 ngay!")
elif thang in [4,6,9,12]:
    print("Thang co 30 ngay!")
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Thang co 29 ngay!")
    else:
        print("Thang co 28 ngay!")
else:
    print("Thang nhap khong hop le")