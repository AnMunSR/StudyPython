'''
 Viet chuong trinh tim tat ca cac so chia het cho 7 nhung khong phai boi so
 cua 5, nam trong doan 2000 den 3200 (tinh ca 2000 va 3200). Cac so thu
 duoc se duoc in thanh mot chuoi tren mot dong, cach nhau bang dau phay
'''

# Ham in ra cac so chia het cho 7 nhung khong phai boi so cua 5
mang = []
for n in range(2000,3201):
    if n % 7 == 0 and n % 5 != 0:
        mang.append(str(n))
print(",".join(mang))

