# Bai tap leh dieu khien co banban
# Bai 21: Nhap vao ngay, thang, nam. Hay tinh va in ra xem ngay
#nhap vao cach dau nam bao neu ngay (gia su nam do khong nhuannhuan)

import math
from datetime import datetime

# Ham tinh so ngay chenh lenh
def chenhLech(ngay):
    # Chuyen doi chuoi ngay dau vao thanh doi tuong datetime
    inputDate = datetime.strptime(ngay,"%d-%m-%Y")

    # Tao ngay dau  nam
    ngayDauNam = datetime(inputDate.year,1,1)

    # Tinh ngay chenh lech
    ngayChenhLech = (inputDate - ngayDauNam).days
    return ngayChenhLech

ngay = input("Nhap vao ngay thang nam (dd-mm-yyyy): ")
print("So ngay chenh lech la: ", chenhLech(ngay))
