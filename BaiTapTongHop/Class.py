'''
Dinh nghia mot class co it nhat 2 method:
    getString: de nhan mot chuoi do nguoi dung nhap vao tu giao dien dieu khien
    printString: in chuoi vua nhap sang chu so
Them cac ham kiem tra don gian de kiem tra method cua class
'''
from ftplib import print_line


class ChuoiDauRa(object):
    def __init__(self):
        self.s = " "

    # Ham getString
    def getString(self):
        self.s = input("Nhap chuoi: ")

    # Ham printString
    def printString(self):
        print_line("Ket qua: ")
        print(self.s.upper())

dauVao = ChuoiDauRa()
dauVao.getString()
dauVao.printString()