# Bai toan nhap lieu va toan tu co ban:
# Bai5: Nhap vao so nguyen a, neu a la so chia het cho 3 va nam trong khoang tu 50-100 thi in ra True, nguoc lai in ra False

import math
a = int(input("Nhap vao so nguyen a: "))
if a % 3 == 0 and a >= 50 and a <= 100:
    print("True")
else:
    print("False")