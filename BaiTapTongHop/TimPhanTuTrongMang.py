'''
  Viet mot chuong trinh co 2 chu so X, Y nhan gia tri tu dau vao va tao
 ra mot mang 2 chieu. Gia tri phan tu trong hang thu i va cot thu j
 cua mang phai la i*j
  Luu y: i = 0, 1, ..., X - 1; j = 0, 1, ..., Y - 1
'''

# Nhap du lieu dau vao
X = int(input("Nhap so dong: X = "))
Y = int(input("Nhap so cot: Y = "))
maTran = [[0 for col in range(Y)] for row in range(X)]
for i in range(X):
    for j in range(Y):
        maTran[i][j] = i * j

print("Ma tran: ")
print(maTran)
