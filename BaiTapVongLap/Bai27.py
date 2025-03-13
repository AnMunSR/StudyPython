# Bai tap vong lap for
# Bai 27: Viet chuong trinh in ra man hinh tam giac co do cao h duoc nhap tu ban phim
#         *
#       *   *
#      *     *
#     *********



import math
from datetime import datetime

# Ham in tam giac can rong
def tamGiacCanRong(h):
    for i in range(h):
        if i == 0: # Hang dau tien
            print(" " * (h-1) + "*")
        elif i == h - 1: # Hang cuoi
            print("*" * (2 * h - 1))
        else:
            # Cac dong o giua chi in dau va cuoi
            print(" " * (h - i - 1) + "*" + " " * (2 * i -1) + "*")

# Nhap du lieu
h = int(input("Nhap vao do cao h = "))
tamGiacCanRong(h)

