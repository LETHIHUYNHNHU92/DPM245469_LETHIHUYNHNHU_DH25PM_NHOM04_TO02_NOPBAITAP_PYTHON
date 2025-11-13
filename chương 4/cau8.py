import math  # Import thư viện math để dùng hàm log (chính là ln)

print("--- CHƯƠNG TRÌNH TÍNH LOGARIT CƠ SỐ A CỦA X ---")
print("Sử dụng công thức: log_a(x) = ln(x) / ln(a)\n")

try:
    # 1. Nhập dữ liệu
    # Dùng float() để cho phép nhập số thực
    a = float(input("Nhập cơ số a: "))
    x = float(input("Nhập giá trị x: "))

    # 2. Kiểm tra các điều kiện
    # Kiểm tra trường hợp hợp lệ (Tất cả điều kiện đều ĐÚNG)
    if x > 0 and a > 0 and a != 1:
        
        # 3. Tính toán theo công thức
        # math.log(x) trong Python chính là ln(x) (logarit tự nhiên)
        ln_x = math.log(x)
        ln_a = math.log(a)
        
        ket_qua = ln_x / ln_a
        
        # 4. Xuất kết quả
        print("\n--- KẾT QUẢ ---")
        # :.4f dùng để làm tròn kết quả đến 4 chữ số thập phân
        print(f"ln(x) = ln({x}) = {ln_x:.4f}")
        print(f"ln(a) = ln({a}) = {ln_a:.4f}")
        print(f"==> log_{a}({x}) = {ket_qua:.4f}")

    else:
        # Nếu không hợp lệ, in ra lỗi tương ứng
        print("\n--- LỖI ĐẦU VÀO ---")
        if x <= 0:
            print("Điều kiện không được đáp ứng: x phải > 0")
        if a <= 0:
            print("Điều kiện không được đáp ứng: a phải > 0")
        if a == 1:
            print("Điều kiện không được đáp ứng: a phải khác 1")

except ValueError:
    # Bắt lỗi nếu người dùng nhập chữ thay vì số
    print("\nLỗi: Vui lòng chỉ nhập SỐ.")
except Exception as e:
    # Bắt các lỗi chung khác
    print(f"\nĐã xảy ra lỗi không mong muốn: {e}")