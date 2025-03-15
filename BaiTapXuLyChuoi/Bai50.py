# Bai tap xu ly chuoi
# Bai 50:
''' 
Nhap vao mot chuoi, kiem tra chuoi do co phai la mot chuoi mat khau
manh hay khong (mot chuoi mat khau manh can co it nhat 1 ky tu dac biet
, 1 ki tu in hoa, 1 con so, 1 chu thuong va do dai phai lon hon 6)
'''
# Ham isalnum: kiem tra co phai ki tu chu hoac so khong

# Ham kiem tra mat khau co phai mat khau manh hay khong
def matKhauManh(s):
    if len(s) <= 6:
        return False
    countHoa = 0
    countThuong = 0
    countSo = 0
    countDacBiet = 0
    for i in range(0, len(s)):
        if s[i].islower():
            countHoa += 1
        elif s[i].isupper():
            countThuong += 1
        elif s[i].isdigit():
            countSo += 1
        elif not s[i].isalnum():
            countDacBiet += 1
    if (countHoa >= 1 and countThuong >= 1 and countDacBiet >= 1):
        return True
    else: 
        return False


# Nhap du lieu dau vao
s = input("Nhap chuoi can kiem tra s:")
if matKhauManh(s):
    print("Mat khau manh!")
else:
    print("Mat khau yeu!")
