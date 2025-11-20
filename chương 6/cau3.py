from random import randrange
import random # Import cho các hàm random


def TaoMaTran(m, n):
    """1. Khởi tạo Ma Trận M x N với các phần tử ngẫu nhiên (0-99)."""
    D = []
    for i in range(m): # Lặp qua số hàng (m)
        row = []
        for j in range(n): # Lặp qua số cột (n)
            # randrange(100) tạo số ngẫu nhiên từ 0 đến 99
            row.append(randrange(100)) 
        D.append(row)
    return D

def XuatMaTran(D):
    """2. Xuất toàn bộ Ma Trận ra màn hình."""
    print("--- MA TRẬN ĐƯỢC TẠO ---")
    for row in D:
        for element in row:
            # Dùng f-string để căn lề phải trong 4 ký tự cho đẹp
            print(f"{element: >4}", end='')
        print()

def XuatListMotChieu(R):
    """Hàm hỗ trợ: Xuất một danh sách (hàng hoặc cột) ra màn hình."""
    for element in R:
        print(f"{element: >4}", end='')
    print()

def LayHang(D, r):
    """3. Lấy ra HÀNG thứ r của Ma Trận D."""
    # Lấy trực tiếp list tại chỉ mục r
    return D[r] 

def LayCot(D, c):
    """4. Lấy ra CỘT thứ c của Ma Trận D."""
    C = []
    for row in D:
        # Lấy phần tử tại chỉ mục cột c của mỗi hàng
        C.append(row[c]) 
    return C

def MAX(D):
    """5. Tìm số lớn nhất (MAX) trong Ma Trận D."""
    # Khởi tạo max bằng phần tử đầu tiên
    max_val = D[0][0]
    
    # Lặp qua tất cả các phần tử
    for row in D:
        for element in row:
            if element > max_val:
                max_val = element
                
    return max_val

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ LIST ĐA CHIỀU ---")
    
    try:
        # 1. Nhập M, N
        m = int(input("Nhập số hàng M: "))
        n = int(input("Nhập số cột N: "))
        
        # Tạo ma trận
        D = TaoMaTran(m, n)
        XuatMaTran(D)
        
        # 2. Lấy và xuất hàng (r)
        r = int(input("\nNhập chỉ mục hàng muốn xuất (bắt đầu từ 0): "))
        if 0 <= r < m:
            hang_ket_qua = LayHang(D, r)
            print(f"--- HÀNG {r} ---")
            XuatListMotChieu(hang_ket_qua)
        else:
            print("Lỗi: Chỉ mục hàng không hợp lệ.")

        # 3. Lấy và xuất cột (c)
        c = int(input("\nNhập chỉ mục cột muốn xuất (bắt đầu từ 0): "))
        if 0 <= c < n:
            cot_ket_qua = LayCot(D, c)
            print(f"--- CỘT {c} ---")
            XuatListMotChieu(cot_ket_qua)
        else:
            print("Lỗi: Chỉ mục cột không hợp lệ.")

        # 4. Tìm và xuất MAX
        max_val = MAX(D)
        print("\n--- KẾT QUẢ CUỐI CÙNG ---")
        print(f"Số lớn nhất (MAX) trong ma trận là: {max_val}")
        
    except ValueError:
        print("\nLỗi: Vui lòng chỉ nhập số nguyên.")
    except IndexError:
        print("\nLỗi: Ma trận rỗng hoặc chỉ mục không hợp lệ.")

if __name__ == "__main__":
    main()