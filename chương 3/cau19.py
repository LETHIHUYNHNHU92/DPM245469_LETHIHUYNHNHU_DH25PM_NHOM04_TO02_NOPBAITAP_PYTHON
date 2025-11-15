import math  # Import thư viện math để dùng hàm tính giai thừa (factorial)

print("---  TÍNH GIÁ TRỊ BIỂU THỨC S ---")
print("S(x, n) = x + x^3/3! + ... + x^(2n+1)/(2n+1)!")

try:
    # 1. Nhập dữ liệu
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập số nguyên n (n >= 0): "))
    
    # 2. Kiểm tra điều kiện n
    if n < 0:
        print("Lỗi: n phải là số nguyên không âm (n >= 0).")
    else:
        # 3. Khởi tạo tổng S
        tong_s = 0.0
        
        # 4. Vòng lặp i chạy từ 0 đến n
        # (range(n + 1) sẽ_tạo_ra_dãy 0, 1, 2, ..., n)
        for i in range(n + 1):
            
            # Tính số mũ và_số_giai_thừa (k = 2*i + 1)
            k = 2 * i + 1
            
            # Tính tử số: x^k
            tu_so = x ** k
            
            # Tính mẫu số: k!
            mau_so = math.factorial(k)
            
            # Cộng số hạng (tử/mẫu) vào tổng
            tong_s += (tu_so / mau_so)
            
            # (Optional) In ra từng bước để_theo_dõi:
            # print(f"i={i}, k={k}, so_hang = {tu_so / mau_so:.4f}")

        # 5. In kết quả_cuối_cùng
        print(f"\n--- KẾT QUẢ ---")
        # :.6f dùng để làm tròn kết quả_đến 6 chữ số thập phân
        print(f"S({x}, {n}) = {tong_s:.6f}")

except ValueError:
    print("\nLỗi: Vui lòng nhập đúng định dạng (x là số, n là số nguyên).")
except Exception as e:
    # Bắt các lỗi hiếm gặp (ví dụ: giai thừa quá lớn)
    print(f"\nĐã xảy ra lỗi: {e}")