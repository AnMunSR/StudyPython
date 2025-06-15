'''
The can cuoc cong dan la day so gom 12 chu so bao gom AAABCCDDDDDD voi AAA la ma tinh thanh,
B la ma gioi tin va ma the ky, CC la 2 chu so cuoi cung cua nam sinh, DDDDDD la mot day to hop
ngau nhien. Thong qua day so nay, co quan quan ly co the xac dinh duoc mot so thong tin cua
nguoi so huu the can cuoc cong dan, gia dinh rang so the CCCD duoc xac thuc theo cac buoc sau:
+ Bat dau tu chu so ngoai cung ben phai, nhan doi gia tri cua moi chu so thu hai
+ Neu nhan doi mot so dan den mot so co hai chu so, tuc la hon hon 9, sau do cong cac chu so
cua tich, de duoc mot chu so
+ Bay gio lay tong cua tat ca cac chu so.
+ Kiem tra xem tong do co chia het cho 10 hay khong (tong modulo 10 bang 0) thi so IMEI la hop
le, neu khac thi no khong hop le.
VD: 079203000009 la so CCCD hop le vi TT la 30 modulo 10 bang 0
a. Hay viet ham is_valid_cccd(cccd) de kiem tra chuoi so cccd nhap vao co phai la so the CCCD
hop le hay khong. Sau do viet ham kiem thu
b. Gia dinh rang so the CCCD bi hu hai va mat mot so o vi tri cuoi cung. Hay viet ham get_all_cccd(atm)
de tra ve danh sach cac so CCCD hop le
'''


# Ham kiem tra cccd hop le
def is_valid_cccd(cccd):
    if not cccd.isdigit() or len(cccd) != 12:
        return False
    total = 0
    rcccd = cccd[::-1]
    for i in range(12):
        temp = int(rcccd[i])
        if i % 2 != 0:
            temp = int(rcccd[i]) * 2
            if temp > 9:
                temp = temp // 10 + temp % 10
        total += temp
    return total % 10 == 0

# Ham kiem tra ve danh sach cac so CCCD hop le
def get_all_cccd(atm):
    lst = []
    for i in range (10):
        s = atm[::-1] + str(i)
        if is_valid_cccd(s):
            lst.append(s)
    return lst



# Nhap du lieu dau vao
def main():
    cccd = input("Nhap can cuoc cong dan: ")
    if is_valid_cccd(cccd):
        print("CCCD hop le!")
    else:
        print("CCCD khong hop le!")
    atm = input("Nhap can cuoc cong dan (bi hu hai cuoi cung): ")
    print("Danh sach can cuoc cong dan hop le: ",get_all_cccd(atm))


if __name__ == "__main__":
    main()
