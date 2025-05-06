'''
 Viet mot chuong trinh chap nhan dau vao ka mot cau, dem so chu cai ca
chu so trong cau do.
 Gia su dau vao: hello world! 123
 Dau ra:
    So chu cai la: 10
    So chu so la: 3
'''

# Nhap du lieu dau vao
s = input("Nhap chuoi dau vao: ")
chuCai = 0
chuSo = 0
for i in range(0, len(s)):
    if s[i].isalpha():
        chuCai += 1
    elif s[i].isdigit():
        chuSo += 1
    else:
        continue
print("So chu cai la: ", chuCai)
print("So chu so la: ", chuSo)
