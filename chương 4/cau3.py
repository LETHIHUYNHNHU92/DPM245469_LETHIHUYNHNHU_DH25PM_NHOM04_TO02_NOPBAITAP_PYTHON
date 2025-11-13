# --- Hàm 1: Tính BMI ---
def tinh_bmi(can_nang, chieu_cao_m):
    """Tính chỉ số BMI (kg/m^2)"""
    
    # Kiểm tra xem chiều cao có hợp lệ không
    if chieu_cao_m <= 0:
        print("Lỗi: Chiều cao phải là số dương.")
        return None  # Trả về None nếu có lỗi
        
    return can_nang / (chieu_cao_m ** 2)

# --- Hàm 2: Phân loại BMI ---
def phan_loai_bmi(bmi):
    """Phân loại BMI theo chuẩn WHO"""
    
    # Nếu hàm tính BMI trả về None (do lỗi), thì không phân loại
    if bmi is None:
        return "Không thể phân loại do đầu vào không hợp lệ."
        
    if bmi < 18.5:
        return "Dưới chuẩn (Gầy)"
    elif 18.5 <= bmi < 24.9:
        return "Bình thường"
    elif 25 <= bmi < 29.9:
        return "Thừa cân"
    elif 30 <= bmi < 34.9:
        return "Béo phì độ I"
    elif 35 <= bmi < 39.9:
        return "Béo phì độ II"
    else:
        return "Béo phì độ III (Nguy hiểm)"

# --- Hàm 3: Hàm chính để chạy chương trình ---
def main():
    print("--- CHƯƠNG TRÌNH TÍNH BMI (CHỈ SỐ KHỐI CƠ THỂ) ---")
    
    try:
        # Sử dụng float() để cho phép người dùng nhập số lẻ (ví dụ: 60.5)
        # input() luôn trả về một chuỗi (string)
        
        can_nang = float(input("Nhập cân nặng của bạn (kg): "))
        chieu_cao_m = float(input("Nhập chiều cao của bạn (mét, ví dụ: 1.75): "))
        
        # 1. Tính toán
        chi_so = tinh_bmi(can_nang, chieu_cao_m)
        
        # 2. Phân loại
        ket_luan = phan_loai_bmi(chi_so)
        
        # 3. In kết quả
        # Chỉ in nếu chi_so được tính thành công (không phải là None)
        if chi_so is not None:
            print("\n--- KẾT QUẢ ---")
            print(f"Cân nặng: {can_nang} kg")
            print(f"Chiều cao: {chieu_cao_m} m")
            # :.2f dùng để làm tròn BMI đến 2 chữ số thập phân
            print(f"Chỉ số BMI của bạn là: {chi_so:.2f}") 
            print(f"Phân loại: {ket_luan}")
            
    except ValueError:
        # Bắt lỗi nếu người dùng nhập chữ (ví dụ: "abc") thay vì số
        print("\nLỗi: Vui lòng chỉ nhập số.")
    except Exception as e:
        # Bắt các lỗi chung khác
        print(f"\nĐã xảy ra lỗi không mong muốn: {e}")

# --- Điểm bắt đầu chạy chương trình ---
# Dòng này đảm bảo hàm main() chỉ chạy khi file này được thực thi trực tiếp
if __name__ == "__main__":
    main()