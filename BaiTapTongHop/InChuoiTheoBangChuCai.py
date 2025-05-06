'''
 Viet mot chuong trinh chap nhan chuoi tu do nguoi dung nhap vao, phan
tach nhau boi dau phay va in ra nhung tu do thanh chuoi theo thu tu
bang chu cai, phan tach nhau bang dau phay
 VD: gia su chuoi duoc nhap la: without,hello,bag,world thi dau ra se la:
bag,hello,without,world
'''

# Nhap du lieu dau vao
chuoi = [x for x in input("Nhap chuoi dau vao (cac tu ngan cach bang ,): ").split(',')]
print("Chuoi chua sap xep: ", chuoi)
chuoi.sort()
print("Chuoi sau khi sap xep: ", ','.join(chuoi))
