import math

def tinh_tong_uoc_so(n):
    if n <= 1: return 0
    tong = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            tong += i
            j = n // i
            if i != j: tong += j
    return tong

def kiem_tra_hoan_thien(n):
    if n <= 0: return False
    return tinh_tong_uoc_so(n) == n

def kiem_tra_thinh_vuong(n):
    if n <= 0: return False
    return tinh_tong_uoc_so(n) > n

def main():
    print("KIỂM TRA SỐ HOÀN THIỆN & THỊNH VƯỢNG ")
    
    try:
        n = int(input("Nhập số nguyên dương n: "))
        
        if n <= 0:
            print("Lỗi: Vui lòng nhập số nguyên dương.")
            return

        tong_uoc = tinh_tong_uoc_so(n)
        
        print(f"\n--- Phân tích số {n} ---")
        print(f"Tổng các ước số (không kể {n}) là: {tong_uoc}")

        if kiem_tra_hoan_thien(n):
            print(f"a) {n} LÀ số hoàn thiện. (Vì {tong_uoc} == {n})")
        else:
            print(f"a) {n} KHÔNG phải là số hoàn thiện.")

        if kiem_tra_thinh_vuong(n):
            print(f"b) {n} LÀ số thịnh vượng. (Vì {tong_uoc} > {n})")  #f la dinh dang f-string b la nd co dinh in ra man hinh
        else:
            
            print(f"b) {n} KHÔNG phải là số thịnh vượng.")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")

if __name__ == "__main__":
    main()