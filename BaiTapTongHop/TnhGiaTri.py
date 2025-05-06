'''
 Viet chuong trinh tinh tinh gia tri cua a+aa+aaa+aaaa voi a la so duoc
nhap vao boi nguoi dung
 Gia su a duoc nhap vao la 1 thi dau ra la: 1234
'''

# Nhap du lieu dau vao
a = int(input("Nhap so a: "))
v1 = int("%s" % a)
v2 = int("%s%s" % (a, a))
v3 = int("%s%s%s" % (a, a, a))
v4 = int("%s%s%s%s" % (a, a, a, a))
print(v1 + v2 + v3 + v4)
