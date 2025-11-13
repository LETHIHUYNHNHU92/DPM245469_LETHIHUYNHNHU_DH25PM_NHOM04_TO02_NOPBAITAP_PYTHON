import time

print("--- CÂU 8: MÁY TÍNH ĐƠN GIẢN ---")

try:
    # 1. Nhập 2 giá trị a và b
    a = float(input("Nhập giá trị a: "))
    b = float(input("Nhập giá trị b: "))

    # 2. Nhập phép toán
    # .strip() dùng để xóa khoảng trắng thừa nếu lỡ tay nhập (ví dụ: " + ")
    phep_toan = input("Nhập phép toán (+, -, *, /): ").strip()

    print("\nĐang tính toán...")
    time.sleep(1) # Dừng 1 giây cho "kịch tính"
    
    # 3. Sử dụng if...elif...else để kiểm tra phép toán
    
    if phep_toan == '+':
        ket_qua = a + b
        print(f"Kết quả: {a} + {b} = {ket_qua}")
        
    elif phep_toan == '-':
        ket_qua = a - b
        print(f"Kết quả: {a} - {b} = {ket_qua}")
        
    elif phep_toan == '*':
        ket_qua = a * b
        print(f"Kết quả: {a} * {b} = {ket_qua}")
        
    elif phep_toan == '/':
        # Xử lý trường hợp đặc biệt: Chia cho 0
        if b == 0:
            print(f"Kết quả: {a} / {b}")
            print("Lỗi: Không thể chia cho 0.")
        else:
            ket_qua = a / b
            print(f"Kết quả: {a} / {b} = {ket_qua}")
            
    else:
        # Xử lý trường hợp nhập sai phép toán
        print(f"Lỗi: Phép toán '{phep_toan}' không được hỗ trợ.")

except ValueError:
    # Bắt lỗi nếu người dùng nhập "abc" thay vì số
    print("\nLỗi: Vui lòng chỉ nhập SỐ cho a và b.")
except Exception as e:
    # Bắt các lỗi chung khác
    print(f"\nĐã xảy ra lỗi không mong muốn: {e}")