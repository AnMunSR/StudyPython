# Bai tap xu ly chuoi
# Bai 47: Nhap vao mot chuoi, hay dem xem trong chuoi co bao nhieu ki tu in hoa
#bao nhieu ky tu in thuong, bao nhieu ki tu so


s = input("Nhap vao chuoi s: ")
countHoa = 0
countThuong = 0
countSo = 0
for i in range(0, len(s)):
    if s[i].islower():
        countHoa += 1
    elif s[i].isupper():
        countThuong += 1
    elif s[i].isdigit():
        countSo += 1
print("So ky tu thuong, hoa, so lan luot la: ", countThuong, countHoa, countSo)
