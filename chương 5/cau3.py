import math
import sys

def CheckPrime(x):
    # 1. Số âm và số < 2 không phải là số nguyên tố
    if x < 2:
        return False
        
    # 2. Lặp từ 2 đến căn bậc hai của x
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            
    return True

def main():
    s = "5;7;8:-2;8;11;13;9;10" 
    
    # Thay thế tất cả dấu ':' bằng ';' để tách dễ dàng hơn
    s_clean = s.replace(':', ';')
    # Tách chuỗi thành một mảng các chuỗi số
    arr_str = s_clean.split(';')
    
    # Khởi tạo các biến đếm và tổng
    so_chan = 0
    so_am = 0
    so_nguyen_to = 0
    tong_sum = 0
    dem_so = 0 # Đếm tổng số lượng số hợp lệ để tính trung bình

    # Xuất các chữ số trên các dòng riêng biệt
    print("--- CÁC SỐ ĐƯỢC XỬ LÝ TRÊN TỪNG DÒNG ---")
    
    for x_str in arr_str:
        try:
            # Chuyển chuỗi thành số nguyên
            number = int(x_str.strip()) 
            
            # Xuất số ra màn hình (Yêu cầu 1)
            print(number) 
            
            # Chỉ tính toán với các số hợp lệ
            dem_so += 1 

            # a) Kiểm tra số chẵn
            if number % 2 == 0:
                so_chan += 1
            
            # b) Kiểm tra số âm
            if number < 0:
                so_am += 1
            
            # c) Kiểm tra số nguyên tố
            if CheckPrime(number):
                so_nguyen_to += 1
            
            # d) Tính tổng
            tong_sum += number
            
        except ValueError:
            continue 

    # --- BƯỚC 3: Tính trung bình và Xuất kết quả cuối cùng ---
    trung_binh = tong_sum / dem_so if dem_so > 0 else 0
    
    print("\n--- KẾT QUẢ PHÂN TÍCH ---")
    print(f"Xuất có bao nhiêu số chẵn: {so_chan}")
    print(f"Xuất có bao nhiêu số âm: {so_am}")
    print(f"Xuất có bao nhiêu số nguyên tố: {so_nguyen_to}")
    print(f"Trung bình cộng: {trung_binh:.2f}")

if __name__ == "__main__":
    main()