# Bai tap xu ly chuoi
# Bai 49: Nhap vao mot chuoi, hay tach toan bo ky tu so trong hcuoi ra roi tinh tong cua chung

s = input("Nhap vao chuoi s: ")
tong = 0
for i in range(0, len(s)):
    if s[i].isdigit():
        tong += int(s[i])
print("Tong cua cac chu so trong chuoi la: ", tong)
