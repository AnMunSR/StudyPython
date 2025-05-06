'''
 Viet mot chuong trinh tim tat ca cac so trong doan 1000 va 3000 (tinh ca
2 so nay) sao cho tat ca cac chu so trong so do la so chan. In cac so
tim duoc thanh cac chuoi cach nhau boi dau phay
'''

# Nhap du lieu dau vao
danhSach = []
for i in range(1000, 3001):
    i = str(i)
    if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0) and (int(i[3]) % 2 == 0):
        danhSach.append(i)
print(','.join(danhSach))
