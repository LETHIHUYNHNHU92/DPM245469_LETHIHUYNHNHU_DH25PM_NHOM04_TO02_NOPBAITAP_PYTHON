import datetime  # Import thư viện xử lý ngày tháng

def main():
    
    try:
        # 1. Nhập dữ liệu
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        # 2. Tạo đối tượng ngày
        # Dùng try...except để bắt lỗi nếu ngày không hợp lệ
        # (Ví dụ: 30/2, 31/4, hoặc 29/2/2025)
        try:
            ngay_hien_tai = datetime.date(nam, thang, ngay)
        except ValueError:
            print(f"\nLỗi: Ngày {ngay}/{thang}/{nam} không tồn tại.")
            return

        # 3. Tạo một khoảng thời gian 1 ngày
        mot_ngay = datetime.timedelta(days=1)
        
        # 4. Tính toán ngày kế tiếp
        # Đây là phép toán chính: (ngày hôm nay + 1 ngày)
        ngay_ke_tiep = ngay_hien_tai + mot_ngay
        
        # 5. In kết quả
        print(f"\nNgày vừa nhập: {ngay_hien_tai.strftime('%d/%m/%Y')}")
        print(f"Ngày kế sau là: {ngay_ke_tiep.strftime('%d/%m/%Y')}")

    except ValueError:
        # Bắt lỗi nếu người dùng nhập chữ thay vì số
        print("\nLỗi: Vui lòng chỉ nhập SỐ.")
    except Exception as e:
        # Bắt các lỗi chung khác
        print(f"\nĐã xảy ra lỗi: {e}")

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()