import time

def ve_hinh_1(n):
    """
    Vẽ hình 1 (Chữ U / Hộp rỗng).
    Hình này có chiều rộng cố định (3 sao / 5 ký tự)
    và chiều cao n.
    """
    print(f"\n--- Hình 1 (n={n}) ---")
    
    # Kiểm tra n. Cần ít nhất 2 hàng để_vẽ_đáy và nóc.
    if n < 2:
        print("Hình 1 yêu cầu n >= 2")
        return

    # 1. In hàng trên cùng
    print("* * *")
    
    # 2. In các hàng ở giữa (n-2 hàng)
    for i in range(n - 2):
        print("* *")
        
    # 3. In hàng dưới cùng
    print("* * *")

def ve_hinh_2(n):
    """
    Vẽ hình 2 (Tam giác vuông căn lề phải).
    """
    print(f"\n--- Hình 2 (n={n}) ---")
    
    # Lặp qua từng hàng (i từ 0 đến n-1)
    for i in range(n):
        
        # Số sao ở hàng hiện tại (i=0 có 1 sao, i=1 có 2 sao,...)
        so_sao = i + 1
        
        # Số khoảng trắng (dùng 2 dấu cách cho đẹp) để_căn lề
        so_khoang_trang = n - so_sao
        
        # In các khoảng trắng
        print("  " * so_khoang_trang, end="")
        
        # In các dấu sao
        print("* " * so_sao)

def ve_hinh_3(n):
    """
    Vẽ hình 3 (Mũi tên '>').
    Hình này yêu cầu n phải là số lẻ để_có_tính_đối_xứng.
    """
    print(f"\n--- Hình 3 (n={n}) ---")
    
    # 1. Kiểm tra n
    if n % 2 == 0:
        print("Hình 3 yêu cầu n phải là số lẻ (ví dụ: 5, 7, 9).")
        print(f"Đang sử dụng n={n+1} để_thay_thế...")
        n = n + 1
        
    # 2. Tìm hàng ở giữa
    hang_giua = n // 2
    
    # 3. Lặp qua từng hàng (i từ 0 đến n-1)
    for i in range(n):
        
        # Trường hợp 1: Nếu là hàng ở giữa
        if i == hang_giua:
            # In một hàng đầy sao
            print("* " * n)
        
        # Trường hợp 2: Các hàng còn lại
        else:
            # Tính số khoảng trắng cần thiết
            # abs(hang_giua - i) -> khoảng cách đến hàng giữa
            # (ví dụ n=7, mid=3: i=0 -> 3; i=1 -> 2; i=2 -> 1)
            so_khoang_trang = (abs(hang_giua - i) - 1) * 2
            
            # Đảm bảo không_bị_âm (cho hàng 2 và 4)
            if so_khoang_trang < 0:
                so_khoang_trang = 0
                
            # In khoảng trắng và 1 dấu *
            print(" " * so_khoang_trang + "*")

def main():
    """Hàm chính để chạy chương trình"""
    try:
        n = int(input("Nhập chiều cao n: "))
        
        if n <= 0:
            print("Lỗi: n phải là số nguyên dương.")
            return

        ve_hinh_1(n)
        time.sleep(1) # Tạm dừng 1 giây
        ve_hinh_2(n)
        time.sleep(1) # Tạm dừng 1 giây
        ve_hinh_3(n)

    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên.")

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()