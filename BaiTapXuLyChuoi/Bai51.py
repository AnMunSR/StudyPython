# Bai tap xu ly chuoi
# Bai 51:
''' 
Nhap vao mot chuoi so nguyen, hay chuyen so sang chuoi, roi dat
dau cham phan tach mot chuoi 3 chu so (phan cach phan ngan)
roi in ra man hinh
'''
# Ham phan tach chuoi
def phanTach(s):
    count = 0
    lst = []
    for i in range(0, len(s)):
        if count == 3:
            lst.append('.')
            count = 0
        count += 1
        lst.append(s[i])
    s1 = " ".join(lst)
    return s1


# Nhap du lieu dau vao
n = int(input("Nhap vao chuoi so nguyen: "))
s = str(n)       # Chuyen so nguyen sang dang chuoi
print("Phan tach: ",phanTach(s))


