# Bai tap lenh dieu khien co ban
# Bai 22: Nhap diem toan, van, anh. Tinh trung binh
# >= 8 va khong co mon nao duoi 6.5: "Học sinh giỏi"
# >= 6.5, toan hoac van >= 6.5 va khong co diem nao duoi 5: "Học sinh khá"
# >=5, toán hoac van >= 5 va khong co diem nao < 3.5: "Học sinh trung bình"
# >= 3.5, toan hoac van >= 3.5 va khong co diem nao < 2: "Học sinh yếu"
# "Học sinh kém"

import math
from datetime import datetime

# Ham xep loai hoc sinh
def xepLoai(toan, van, anh):
    tb = (toan + van + anh)/3
    if (tb >= 8) and (toan >= 6.5) and (van >= 6.5) and (anh >= 6.5):
        print("Học sinh giỏi")
    elif (tb >= 6.5) and (toan >= 5) and (van >= 5) and (anh >= 5) and ((toan >= 6.5) or (van >= 6.5)):
        print("Học sinh khá")
    elif (tb >= 5) and (toan >= 3.5) and (van >= 3.5) and (anh >= 3.5) and ((toan >= 5) or (van >= 5)):
         print("Học sinh trung bình")
    elif (tb >= 3.5) and (toan >= 2) and (van >= 2) and (anh >= 2) and ((toan >= 3.5) or (van >= 3.5)):
         print("Học sinh trung yếu")
    else:
        print("Học sinh kém")

# Nhap du lieu dau vao
toan = float(input("Nhap vao diem toan: "))
van = float(input("Nhap vao diem van: "))
anh = float(input("Nhap vao diem anh: "))
xepLoai(toan, van, anh)