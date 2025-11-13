def tinh_roi(tong_doanh_thu, chi_phi_dau_tu):
    """
    Hàm này tính Tỷ suất hoàn vốn (ROI).
    
    Args:
        tong_doanh_thu (float): Tổng số tiền thu về.
        chi_phi_dau_tu (float): Tổng số tiền đã bỏ ra để đầu tư.
        
    Returns:
        float: Chỉ số ROI (dưới dạng phần trăm) hoặc None nếu có lỗi.
    """
    
    # --- Bước 1: Kiểm tra điều kiện ---
    # Chi phí đầu tư phải là số dương
    if chi_phi_dau_tu <= 0:
        print("Lỗi: Chi phí đầu tư phải là một số dương.")
        return None  # Trả về None nếu có lỗi

    # --- Bước 2: Tính toán theo công thức ---
    loi_nhuan_rong = tong_doanh_thu - chi_phi_dau_tu
    
    # Công thức ROI
    roi = (loi_nhuan_rong / chi_phi_dau_tu) * 100
    
    # --- Bước 3: Trả về kết quả ---
    return roi

def main():
   
    print("--- CHƯƠNG TRÌNH TÍNH ROI (TỶ SUẤT HOÀN VỐN) ---")
    
    try:
        # 1. Nhập dữ liệu từ người dùng
        # float() cho phép nhập số thập phân
        chi_phi = float(input("Nhập tổng chi phí đầu tư (VND): "))
        doanh_thu = float(input("Nhập tổng doanh thu thu về (VND): "))
        
        # 2. Gọi hàm để tính toán
        ket_qua_roi = tinh_roi(doanh_thu, chi_phi)
        
        # 3. In kết quả nếu tính toán thành công (ket_qua_roi không phải là None)
        if ket_qua_roi is not None:
            print("\n--- KẾT QUẢ ---")
            # :.2f dùng để làm tròn đến 2 chữ số thập phân
            print(f"Tỷ suất hoàn vốn (ROI) của bạn là: {ket_qua_roi:.2f}%")
            
            # Thêm một chút phân tích cho thân thiện
            if ket_qua_roi > 0:
                print(f"-> Chúc mừng! Bạn đã lãi {ket_qua_roi:.2f}%.")
            elif ket_qua_roi == 0:
                print("-> Bạn đã hòa vốn.")
            else:
                # abs() dùng để lấy giá trị tuyệt đối (bỏ dấu trừ)
                print(f"-> Cảnh báo! Bạn đã lỗ {abs(ket_qua_roi):.2f}%.")

    except ValueError:
        # Bắt lỗi nếu người dùng nhập chữ thay vì số
        print("\nLỗi: Vui lòng chỉ nhập số. Hãy thử lại.")
    except Exception as e:
        # Bắt các lỗi chung khác
        print(f"\nĐã xảy ra lỗi không mong muốn: {e}")

# --- Điểm bắt đầu chạy chương trình ---
if __name__ == "__main__":
    main()