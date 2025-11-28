import os
import time

def LuuFile(path, data):
    # Dữ liệu phải là chuỗi
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(data + "\n")
    except IOError:
        print(f"Lỗi: Không thể ghi vào file {path}.")

def DocFile(path):
    """
    Đọc dữ liệu từ file, tách tất cả các số bằng nhiều loại delimiter 
    và trả về 1 list chứa tất cả các số thực.
    """
    arrSo = []
    if not os.path.exists(path):
        return arrSo 

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip()
                if not data: continue 
                
                # 1. CHUẨN HÓA DELIMITERS: Thay tất cả các dấu phân cách bằng khoảng trắng
                # Điều này giúp hàm split() xử lý hiệu quả.
                data = data.replace(',', ' ').replace(';', ' ').replace('\t', ' ')
                
                # 2. Split() không đối số tự động xử lý nhiều khoảng trắng dư thừa
                parts = data.split()
                
                # 3. Chuyển đổi sang số thực (float)
                for part in parts:
                    try:
                        arrSo.append(float(part))
                    except ValueError:
                        # Bỏ qua các chuỗi không phải số (ví dụ: tên cột)
                        continue
        return arrSo
    except IOError:
        print(f"Lỗi: Không thể đọc file {path}.")
        return []

def main():
    FILE_PATH = "csdl_so.txt"
    
    print("--- BƯỚC 1: TẠO FILE MẪU VÀ GHI DỮ LIỆU ---")
    # Xóa file cũ nếu tồn tại để chuẩn bị file mới
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    
    # Ghi dữ liệu mẫu 
    LuuFile(FILE_PATH, "5, 4.7, 9.3, 20")
    LuuFile(FILE_PATH, "5.7, -3, 9.15, -21")
    LuuFile(FILE_PATH, "5, 64, 27, -9.3, 7")
    LuuFile(FILE_PATH, "-50, 26")
    
    time.sleep(1)
    
    # --- BƯỚC 2: XỬ LÝ VÀ XUẤT KẾT QUẢ ---
    arrSo = DocFile(FILE_PATH)
    
    # a) Xuất toàn bộ list 
    print("\n--- A) TOÀN BỘ LIST SỐ TỪ FILE ---")
    print(arrSo)
    print(f"Tổng số phần tử được đọc: {len(arrSo)}")
    
    so_am = [n for n in arrSo if n < 0]
    print("\n--- B) CÁC SỐ ÂM ĐƯỢC TÌM THẤY ---")
    
    if so_am:
        print(so_am)
        print(f"Có {len(so_am)} số âm.")
    else:
        print("Không tìm thấy số âm nào.")

if __name__ == "__main__":
    main()