print("-- XÁC ĐỊNH QUÝ TRONG NĂM ---")

try:
    # 1. Nhập tháng
    thang = int(input("Nhập vào tháng (1-12): "))
    
    # 2. Kiểm tra logic quý
    # (Python cho phép viết 1 <= thang <= 3, rất dễ đọc)
    
    if 1 <= thang <= 3:
        quy = 1
    elif 4 <= thang <= 6:
        quy = 2
    elif 7 <= thang <= 9:
        quy = 3
    elif 10 <= thang <= 12:
        quy = 4
    else:
        # Xử lý trường hợp nhập số không hợp lệ (ví dụ: 0 hoặc 13)
        quy = None
        print(f"Lỗi: Tháng {thang} không hợp lệ. Vui lòng nhập số từ 1 đến 12.")

    # 3. In kết quả nếu đầu vào hợp lệ
    if quy is not None:
        print(f"==> Tháng {thang} thuộc Quý {quy} trong năm.")

except ValueError:
    # Bắt lỗi nếu người dùng nhập "abc" thay vì số
    print("Lỗi: Vui lòng chỉ nhập SỐ.")
except Exception as e:
    # Bắt các lỗi chung khác
    print(f"Đã xảy ra lỗi không mong muốn: {e}")