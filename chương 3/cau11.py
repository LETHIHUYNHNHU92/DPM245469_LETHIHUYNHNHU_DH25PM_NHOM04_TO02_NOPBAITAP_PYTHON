import math
import time

def kiem_tra_so_nguyen_to(n):
    """
    Hàm kiểm tra số n có phải là số nguyên tố hay không.
    Trả về True nếu là số nguyên tố, False nếu không phải.
    """
    
    # 1. Các số nhỏ hơn 2 không phải là số nguyên tố
    if n < 2:
        return False
        
    # 2. Lặp từ 2 đến căn bậc hai của n
    # (Chỉ cần kiểm tra đến căn bậc hai là đủ)
    for i in range(2, int(math.sqrt(n)) + 1):
        # Nếu n chia hết cho bất kỳ số nào trong khoảng này
        if n % i == 0:
            return False  # n có ước số khác 1 và chính nó
            
    # 3. Nếu vòng lặp kết thúc mà không tìm thấy ước số
    return True  # n là số nguyên tố

def main():
    """Hàm chính chạy chương trình"""
    
    # Đây là vòng lặp chính của phần mềm, nó sẽ chạy mãi mãi
    while True:
        
        # --- Phần 1: Nhập và kiểm tra số ---
        try:
            so_nhap = input("\nNhập một số nguyên để kiểm tra: ")
            so = int(so_nhap)  # Thử chuyển đổi sang số nguyên
            
            # Gọi hàm kiểm tra
            if kiem_tra_so_nguyen_to(so):
                print(f"==> {so} LÀ số nguyên tố.")
            else:
                print(f"==> {so} KHÔNG phải là số nguyên tố.")

        except ValueError:
            # Bắt lỗi nếu người dùng nhập chữ (ví dụ: "abc")
            print(f"Lỗi: '{so_nhap}' không phải là một số nguyên hợp lệ.")
            # Dùng 'continue' để bỏ qua phần hỏi thoát và quay lại đầu vòng lặp
            continue 

        # --- Phần 2: Hỏi tiếp tục hay thoát ---
        
        # Vòng lặp con này dùng để đảm bảo người dùng nhập đúng 'c' hoặc 'k'
        while True:
            lua_chon = input("Bạn có muốn tiếp tục sử dụng? (c = tiếp tục, k = thoát): ").lower().strip()
            
            if lua_chon == 'c':
                # Nếu chọn 'c', thoát vòng lặp con và quay lại đầu vòng lặp chính
                break 
            elif lua_chon == 'k':
                # Nếu chọn 'k', cũng thoát vòng lặp con
                break
            else:
                # Nếu nhập sai, yêu cầu nhập lại
                print("Lựa chọn không hợp lệ. Vui lòng chỉ nhập 'c' hoặc 'k'.")
        
        # Sau khi thoát vòng lặp con, kiểm tra lựa chọn
        if lua_chon == 'k':
            print("\nĐang thoát phần mềm...")
            time.sleep(1)
            print("Cảm ơn bạn đã sử dụng. Tạm biệt!")
            break  

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()