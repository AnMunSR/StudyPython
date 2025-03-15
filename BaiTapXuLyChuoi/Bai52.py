# Bai tap xu ly chuoi
# Bai 52:
''' 
Nhap vao chuoi a va chuoi b
Hay xoa chuoi b trong chuoi a roi in lai chuoi a ra man hinh
(khong dung ham replace)
'''
# Ham xoa chuoi
def xoaChuoi(a,b):
    s = ""
    i = 0
    while i < len(a):
        pos = a.find(b,i) # Tim vi tri cua b trong a bat dau tu vi tri i trong chuoi a
        if pos == -1: # Khong tim thay
            s += a[i:] # Them cac phan tu con la
            break
        s += a[i: pos]
        i = pos + len(b)
    return s
    


# Nhap du lieu dau vao
a = input("Nhap chuoi a: ")
b = input("Nhap chuoi b: ")
print("Chuoi sau khi xoa: ", xoaChuoi(a,b))
