import math  # Dùng để_lấy_hàm_căn_bậc_hai (sqrt)

print("--- CÂU 7: TÍNH ĐỘ DÀI ĐOẠN AB ---")

try:
    # --- Nhập tọa độ điểm A ---
    print("--- Nhập tọa độ điểm A ---")
    x_a = float(input("Nhập hoành độ (xA): "))
    y_a = float(input("Nhập tung độ (yA): "))
    
    # --- Nhập tọa độ điểm B ---
    print("\n--- Nhập tọa độ điểm B ---")
    x_b = float(input("Nhập hoành độ (xB): "))
    y_b = float(input("Nhập tung độ (yB): "))
    
    # --- Tính toán độ dài ---
    # Áp dụng công thức: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    
    # (xB - xA) ** 2
    do_dai_x = (x_b - x_a) ** 2
    
    # (yB - yA) ** 2
    do_dai_y = (y_b - y_a) ** 2
    
    # Lấy căn bậc hai của tổng
    do_dai_ab = math.sqrt(do_dai_x + do_dai_y)
    
    # --- Xuất kết quả ---
    print("\n--- KẾT QUẢ ---")
    print(f"Tọa độ A = ({x_a}, {y_a})")
    print(f"Tọa độ B = ({x_b}, {y_b})")
    # :.4f dùng để làm tròn
    print(f"==> Độ dài đoạn AB là: {do_dai_ab:.4f}")

except ValueError:
    print("\nLỗi: Vui lòng chỉ nhập số. Hãy chạy lại chương trình.")
except Exception as e:
    print(f"\nĐã xảy ra lỗi: {e}")