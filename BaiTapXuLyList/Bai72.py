# Bai tap xu ly list
# Bai 72:
'''
Nhap vao mot list L co cac phan tu la chuoi
Hay tim ra chuoi co vi tri ky tu in hoa lon nhat
'''

import math


def vi_tri_in_hoa_lon_nhat(s):
    """Tìm vị trí lớn nhất của ký tự in hoa trong chuỗi s"""
    vi_tri = -1
    for i, char in enumerate(s):
        if char.isupper():
            vi_tri = i  # Cập nhật vị trí lớn nhất
    return vi_tri

def tim_chuoi_co_vi_tri_in_hoa_lon_nhat(L):
    """Tìm chuỗi có vị trí ký tự in hoa lớn nhất trong list L"""
    chuoi_max = None
    vi_tri_max = -1

    for chuoi in L:
        vi_tri = vi_tri_in_hoa_lon_nhat(chuoi)
        if vi_tri > vi_tri_max:
            vi_tri_max = vi_tri
            chuoi_max = chuoi

    return chuoi_max if chuoi_max else "Không có chuỗi nào chứa ký tự in hoa!"

# Nhập danh sách L từ người dùng
L = ["hello", "PyThon", "coDinG", "ExampleTest"]

# Tìm chuỗi có vị trí ký tự in hoa lớn nhất
result = tim_chuoi_co_vi_tri_in_hoa_lon_nhat(L)

# In kết quả
print("Chuỗi có vị trí ký tự in hoa lớn nhất:", result)

