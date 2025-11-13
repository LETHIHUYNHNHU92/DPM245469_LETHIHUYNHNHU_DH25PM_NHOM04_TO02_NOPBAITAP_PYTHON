import math  # Import thư viện math để dùng hàm sqrt (căn bậc 2)

def tinh_can_long(x, n):
    """
    Hàm tính căn bậc 2 lồng nhau n lần của x.
    S = sqrt(x + sqrt(x + ... + sqrt(x)))
    
    Args:
        x (float): Giá trị bên trong dấu căn.
        n (int): Số lượng dấu căn lồng nhau.
        
    Returns:
        float: Kết quả của biểu thức, hoặc None nếu lỗi.
    """
    
    # Bắt đầu với kết quả = 0
    ket_qua = 0.0
    
    # Chạy vòng lặp n lần
    for i in range(n):
        
        # Giá trị bên trong căn (x + kết quả của lần lặp trước)
        gia_tri_trong_can = x + ket_qua
        
        # Kiểm tra điều kiện (không thể lấy căn số âm)
        if gia_tri_trong_can < 0:
            print(f"Lỗi: ở lần lặp {i+1}, không thể lấy căn của số âm ({gia_tri_trong_can:.2f})")
            return None
            
        # Tính kết quả mới
        ket_qua = math.sqrt(gia_tri_trong_can)
        
        
        # print(f"Lần {i+1}, S = {ket_qua:.5f}")

    return ket_qua

def main():
    """Hàm chính để chạy chương trình"""
    print("--- CHƯƠNG TRÌNH TÍNH CĂN BẬC 2 LỒNG NHAU ---")
    print("Tính S = sqrt(x + sqrt(x + ... + sqrt(x))) (n lần)")
    
    try:
        # 1. Nhập giá trị
        x = float(input("\nNhập giá trị x: "))
        n = int(input("Nhập số lần lồng nhau (n): "))

        # 2. Kiểm tra n
        if n <= 0:
            print("Lỗi: Số lần lồng (n) phải là số nguyên dương.")
        else:
            # 3. Gọi hàm và tính toán
            ket_qua = tinh_can_long(x, n)
            
            # 4. In kết quả nếu tính toán thành công
            if ket_qua is not None:
                print("\n--- KẾT QUẢ ---")
                print(f"Giá trị của biểu thức là: {ket_qua:.6f}")

    except ValueError:
        print("\nLỗi: Vui lòng nhập x (số thực) và n (số nguyên) hợp lệ.")
    except Exception as e:
        print(f"\nĐã xảy ra lỗi: {e}")

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()