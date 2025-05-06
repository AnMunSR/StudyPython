'''
 Su dung mot danh sach de loc cac so le tu danh sach duoc nguoi dung
nhap vao.
 Vi du: 1,2,3,4,5,6,7,8,9 thi dau ra la 1,3,5,7,9
'''

# Nhap du lieu dau vao
s = input("Nhap chuoi so dau vao (cac so cach nhau bang dua phay): ")
soLe = [ x for x in s.split(',') if int(x) % 2 != 0]
print(','.join(soLe))
