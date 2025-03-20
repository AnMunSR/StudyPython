# Bai tap xu ly list
# Bai 70:
'''
Nhap vao mot list L co cac phan tu bao gom chuoi, so nguyen, hay kiem tra cac phan
tu trong L co phai la chuoi va so xen ke nhau khong, neu co thi ta tien hanh tao mot
list K moi co cac phan tu nhu sau:
K[i/2] = L[i] * L[i+1] (voi i chan)
'''

import math


def kiem_tra_xen_ke(L):
    # Kiểm tra danh sách có xen kẽ số và chuỗi không
    for i in range(len(L)):
        if i % 2 == 0 and not isinstance(L[i], str):  # Chỉ số chẵn phải là chuỗi
            return False
        if i % 2 == 1 and not isinstance(L[i], int):  # Chỉ số lẻ phải là số nguyên
            return False
    return True

def tao_list_K(L):
    if not kiem_tra_xen_ke(L):
        return "Danh sách không xen kẽ số và chuỗi!"

    K = []
    for i in range(0, len(L) - 1, 2):  # Duyệt chỉ số chẵn
        K.append(L[i] * L[i + 1])  # Nhân chuỗi với số
    return K

# Nhập danh sách L
L = [ "A", 3, "B", 2, "C", 4 ]

# Kiểm tra và tạo danh sách K
result = tao_list_K(L)

# In kết quả
print("Danh sách K:", result)

