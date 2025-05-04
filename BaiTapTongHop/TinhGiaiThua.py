'''
Viet chuong trinh co the tinh giai thua cua mot so cho truoc. Ket qua duoc in
thanh chuoi tren mot dong, phan tach boi dau phay. Vi du, so cho truoc la 8
thi ket qua dau ra phai la 40320
'''


# Ham tinh giai thua
def tinhGiaiThua(n):
    if n > 0:
        return n * tinhGiaiThua(n - 1)
    else:
        return 1


# Nhap du lieu dau vao
n = int(input("Nhap so nguyen can tinh giai thua: "))
giaiThua = tinhGiaiThua(n)
print(giaiThua)