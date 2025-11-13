import math

# --- 1. HÀM TÍNH TỔNG ƯỚC SỐ (DÙNG CHUNG) ---
def tinh_tong_uoc_so(n):
    """
    Tính tổng các ước số của n, KHÔNG bao gồm chính n.
    Hàm này được tối ưu bằng cách chỉ lặp đến sqrt(n).
    """
    if n <= 1:
        return 0
    
    tong = 1  # Bắt đầu với 1 (vì 1 luôn là ước số)
    sqrt_n = int(math.sqrt(n))
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            tong += i
            j = n // i
            if i != j:
                tong += j
                
    return tong

# --- 2. HÀM KIỂM TRA (CÂU A & B) ---
def kiem_tra_hoan_thien(n):
    """
    a) Kiểm tra n có phải là số hoàn thiện hay không.
    (Tổng ước số = n)
    """
    if n <= 0:
        return False
    return tinh_tong_uoc_so(n) == n

def kiem_tra_thinh_vuong(n):
    """
    b) Kiểm tra n có phải là số thịnh vượng hay không.
    (Tổng ước số > n)
    """
    if n <= 0:
        return False
    return tinh_tong_uoc_so(n) > n

# --- 3. HÀM MAIN ĐỂ CHẠY THỬ ---
def main():
    try:
        n = int(input("Nhập số nguyên dương n để kiểm tra: "))
        
        if n <= 0:
            print("Vui lòng nhập số nguyên dương.")
            return

        # Tính tổng ước số một lần duy nhất
        tong_uoc = tinh_tong_uoc_so(n)
        
        print(f"\n--- Kết quả cho n = {n} ---")
        print(f"Tổng các ước số (không kể {n}) là: {tong_uoc}")

        # Kiểm tra câu a
        if kiem_tra_hoan_thien(n):
            print(f"a) {n} LÀ số hoàn thiện (Vì {tong_uoc} == {n})")
        else:
            print(f"a) {n} KHÔNG phải là số hoàn thiện.")

        # Kiểm tra câu b
        if kiem_tra_thinh_vuong(n):
            print(f"b) {n} LÀ số thịnh vượng (Vì {tong_uoc} > {n})")
        else:
            print(f"b) {n} KHÔNG phải là số thịnh vượng.")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()