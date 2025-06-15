'''
So Armstrong la so ma tung chu so trong do luy thua voi so chu so cua no bang
chinh no. VD: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27, thi 153 la so Armstrong
a. Hay dinh nghi ham is_armstrong(n) de xac dinh xem n co phai la so Armstrong
hay khong
b. Hay dinh nghia ham list_n_armstrong(n) de tra ve danh sach n so Armstrong dau tien
c. Cho danh sach mot day so voi so luong bat ky my_list, hay viet ham get_armstrong(my_list)
de tra ve danh sach cac so la so Armstrong duoc sap xep theo thu tu tu be den lon
va khong trung nhau.
d. Cho mot tap tin chua van ban my_test_1.txt. Hay viet ham get_frequency(path_to_file),
ham tra ve mot tu dien voi key la so Armstrong, value la so lan xuat hien cua key tuogn ung
trong van ban, dong thoi luu lai tu dien vao tap tin D:\get_frequency.log
e. Viet ham main de kiem thu cac cau a,b,c,d
'''
from collections import Counter
from itertools import count
from operator import countOf


# Dinh nghia cac ham

# Dinh nghia ham is_armstrong(n)
def is_armstrong(n):
    chuoiSo = [int(s) for s in str(n)]
    doDai = len(chuoiSo)
    tongSo = sum([so ** doDai for so in chuoiSo])
    return tongSo == n


# Cau b
def list_n_armstrong(n):
    result = []
    for i in range(0, n):
        if is_armstrong(i):
            result.append(i)
    return result


# Cau c:
def get_armstrong(my_list):
    result = sorted({i for i in my_list if is_armstrong(i)})
    return result


# Cau e:
def get_frequency(path_to_file):
    f = open(path_to_file,'r')
    f1 = open('get_frequency.log','w')
    lst = []
    while True:
        temp = f.readline()
        if temp == '':
            break
        lst.append(int(temp))
    result = [i for i in lst if is_armstrong(i)]
    temp = Counter(result)
    for key, value in temp.items():
        f1.write(f"{key}:{value}\n")
    f1.close()
    f.close()

# Cau e:
def main():
    path_to_file = "my_test1.txt"
    print("Cau a: Kiem tra so Armstrong")
    so = int(input("Nhap so n: "))
    if is_armstrong(so):
        print("So ",so," la so Armstrong")
    else:
        print("So ",so," khong phai so Armstrong")
    print("Cau b: Tra ve danh sach n so Armstrong dau tien")
    print(list_n_armstrong(200))
    print("Cau c: Tra ve danh sach cac so Armstrong sap xep theo tu tu tang dan, khong trung ")
    my_list = [12,10,371,150,153,10,371]
    print(get_armstrong(my_list))
    print("Cau d: Tra ve mot tu dien voi key la so Armstrong, value la so lan xuat hien, ghi vao tap frequency.log")
    get_frequency(path_to_file)

if __name__ == "__main__":
    main()