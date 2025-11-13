def doc_so_hai_chu_so(n):
    
    
    # 1. Tạo danh sách các từ cơ bản
    don_vi = [
        "không", "một", "hai", "ba", "bốn", 
        "năm", "sáu", "bảy", "tám", "chín"
    ]
    
    # 2. Xử lý các trường hợp đơn giản (0 -> 9)
    if 0 <= n <= 9:
        return don_vi[n]

    # 3. Xử lý các trường hợp "mười" (10 -> 19)
    if 10 <= n <= 19:
        # Trường hợp đặc biệt: n=10 (mười)
        if n == 10:
            return "mười"
            
        # Trường hợp đặc biệt: n=15 (mười lăm)
        if n == 15:
            return "mười lăm"
            
        # Các trường hợp 11-19 (trừ 15)
        # Lấy chữ số hàng đơn vị (ví dụ: 11 -> 1)
        so_dv = n % 10
        return "mười " + don_vi[so_dv]

    # 4. Xử lý các trường hợp "mươi" (20 -> 99)
    if 20 <= n <= 99:
        # Lấy chữ số hàng chục và hàng đơn vị
        so_chuc = n // 10
        so_dv = n % 10
        
        # Tạo phần "mươi" (ví dụ: "ba mươi")
        phan_chuc = don_vi[so_chuc] + " mươi"
        
        # --- Xử lý các ngoại lệ của hàng đơn vị ---
        
        # Trường hợp 1: Hàng đơn vị là 0 (ví dụ: 30)
        if so_dv == 0:
            return phan_chuc
            
        # Trường hợp 2: Hàng đơn vị là 1 (ví dụ: 31 -> ... mốt)
        elif so_dv == 1:
            return phan_chuc + " mốt"
            
        # Trường hợp 3: Hàng đơn vị là 5 (ví dụ: 35 -> ... lăm)
        elif so_dv == 5:
            return phan_chuc + " lăm"
            
        # Trường hợp 4: Đơn vị là 2, 3, 4, 6, 7, 8, 9 (ví dụ: 32)
        else:
            return phan_chuc + " " + don_vi[so_dv]
            
    # Trường hợp nếu số nằm ngoài 0-99
    return "Số không hợp lệ (chỉ xử lý 0-99)"

def main():
  
    try:
        n_str = input("Nhập một số nguyên n (tối đa 2 chữ số): ")
        n = int(n_str)
        
        if 0 <= n <= 99:
            # Gọi hàm để đọc số
            cach_doc = doc_so_hai_chu_so(n)
            print(f"n = {n} => {cach_doc}")
        else:
            print(f"Lỗi: Số {n} không phải là số có tối đa 2 chữ số (0-99).")
            
    except ValueError:
        print(f"Lỗi: '{n_str}' không phải là một số nguyên hợp lệ.")

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()