# Bai tap luyen tap va ung dung
# Bai 89:
'''

'''

import math

from itertools import combinations


def max_material(U, V, A, B):
    n = len(A)
    max_quantity = 0.0

    for (i, j) in combinations(range(n), 2):
        # Mua từ công ty i bằng đô-la và công ty j bằng Euro
        quantity1 = (U / A[i]) + (V / B[j])

        # Mua từ công ty j bằng đô-la và công ty i bằng Euro
        quantity2 = (U / A[j]) + (V / B[i])

        # Cập nhật kết quả lớn nhất
        max_quantity = max(max_quantity, quantity1, quantity2)

    return f"{max_quantity:.2f}"


# Ví dụ sử dụng
U, V = 100, 50
A = [5, 10, 8]
B = [4, 6, 7]
print(max_material(U, V, A, B))
