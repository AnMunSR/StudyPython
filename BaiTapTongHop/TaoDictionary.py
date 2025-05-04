'''
Voi so nguyen n nhat dinh, hay viet chuong trinh de tao ra mot dictionry
chua (i,i*i) nhu la so nguyen tu 1 den n (bao gom ca 1 va n) sau do in ra
dictionary nay.
VD: gia su n = 8: {1:1, 2: 4, 3: 9. 4: 16,...}
'''


# Ham tao dictionary
def taoDictionary(n):
    diction = dict()
    for i in range(1, n + 1):
        diction[i] = i * i
    return diction


# Nhap du lieu dau vao
n = int(input("Nhap so nguyen n: "))
print(taoDictionary(n))
