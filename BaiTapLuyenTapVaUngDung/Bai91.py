# Bai tap luyen tap va ung dung
# Bai 91:
'''
Mot khach san co N phong doi duoc danh so tu 1 den N va M doan khach
Voi moi doan khach, ta xep moi cap khach cua doan vao mot phong trong theo thu tu tang dan
Neu doan khach co so nguoi le thi nguoi khach cuoi cung duoc xep vao mot phong trong tiep theo
Neu da het phong con trong thi ta se xep khach vao nhung phong moi chi co 1 khach theo thu tu tang dan
In ra so khach cua moi phong sau khi xep
Gia su khong co 2 doan khach nao den cung mot luc
'''

import math


def allocate_rooms(N, groups):
    rooms = [0] * N  # Khởi tạo danh sách phòng với số khách ban đầu là 0

    for group in groups:
        count = group  # Số người trong đoàn

        # Xếp khách vào các phòng trống trước theo từng cặp
        for i in range(N):
            while count >= 2 and rooms[i] == 0:  # Chỉ xếp cặp khách vào phòng trống
                rooms[i] = 2
                count -= 2
            if count == 1 and rooms[i] == 0:  # Nếu còn 1 khách lẻ, xếp vào phòng trống tiếp theo
                rooms[i] = 1
                count -= 1
                break

        # Nếu vẫn còn khách, xếp vào phòng đã có 1 người
        for i in range(N):
            if count == 0:
                break
            if rooms[i] == 1:  # Xếp khách vào phòng đã có 1 người
                rooms[i] = 2
                count -= 1

    print(", ".join(map(str, rooms)))


# Đọc dữ liệu đầu vào
N = int(input("Nhập số phòng: "))
M = int(input("Nhập số đoàn khách: "))
groups = [int(input(f"Nhập số khách của đoàn {i + 1}: ")) for i in range(M)]

allocate_rooms(N, groups)

