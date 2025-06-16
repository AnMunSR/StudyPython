'''
Viet mot lop co ten Movie dai dien cho moi phim trong kho phim. Moi phim co cac thuoc tinh
sau: title: ten phim (CHARLIE'S ANGELS); direcor: dao dien (Elizabeth Banks); actor: dien vien
chinh (Kristen Stewart, Naomi Scott, Ella Balinska); year: nam phat hanh (2019); rating: diem
danh gia cua phim
Lop Movie cung co cac phuong thuc sau:
+ read(): tra ve mot bo gom 2 phan tu la so luong dao dien va so luong  dien vien cua phim
+ __str__(): tra ve mot chuoi mo ta phim nay theo ten phim, year va rating (vi du: "Nhung thien
than cua Charlie san xuat nam 2019 co diem danh gia la 4.5")
'''


class Movie:
    # Ham khoi tao
    def __init__(self,title, director, actor, year, rating):
        self.title = title
        self.director = director
        self.actor = actor
        self.year = year
        self.rating = rating

    # Ham read
    def read(self):
        num_director = 1 if self.director else 0
        num_actor = len(self.actor)
        return (num_director, num_actor)

    # Ham str
    def __str__(self):
        print(f"{self.title} cua {self.director} san xuat nhung nam {self.year} co diem danh gia la {self.rating}")


m1 = Movie("Hoang Hoa Tham","Tran Minh Mang","Hoa Chi Minh",2004,4.5)
m1.read()
m1.__str__()