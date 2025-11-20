import random
import math # Import cho tính toán tổng quát

def CheckDoiXung(lst):
    
    n = len(lst) #do dai cua list
    # Chỉ cần lặp đến nửa list (n // 2)
    for i in range(n // 2):
        # So sánh phần tử đầu (i) với phần tử cuối đối xứng (n - 1 - i)
        if lst[i] != lst[n - 1 - i]:
            return False
    return True

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ LIST (NGẪU NHIÊN) ---")
    
    # 1. Khởi tạo list ngẫu nhiên n phần tử
    try:
        n_input = input("Nhập số phần tử N: ")
        n = int(n_input)
    except ValueError:
        print(f"Lỗi: '{n_input}' không phải là số nguyên.")
        return

    lst = []
    # Khởi tạo list với N phần tử ngẫu nhiên (từ 0 đến 100)
    for i in range(n):
        lst.append(random.randrange(0, 101)) 

    print(f"\nList ngẫu nhiên ban đầu: {lst}")
    
    # 2. Thêm phần tử mới (x)
    try:
        x_input = input("\nMời bạn chèn thêm số mới (x): ")
        x = int(x_input)
        lst.append(x)
        print(f"List sau khi chèn {x}: {lst}")
    except ValueError:
        print("Cảnh báo: Giá trị x không hợp lệ và đã bị bỏ qua.")

    # 3. Loại bỏ tất cả các phần tử có giá trị k
    try:
        k_input = input("\nNhập số muốn xóa (k): ")
        k = int(k_input)
        
        # Vòng lặp chuẩn: Xóa K cho đến khi không còn K trong list
        so_lan_xoa = 0
        while lst.count(k) > 0:
            lst.remove(k)
            so_lan_xoa += 1
            
        print(f"List sau khi xóa {k} ({so_lan_xoa} lần): {lst}")
    except ValueError:
        print("Cảnh báo: Giá trị k không hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xóa: {e}")
        
    # 4. Kiểm tra đối xứng
    kt = CheckDoiXung(lst)
    
    print("\n--- KIỂM TRA ĐỐI XỨNG ---")
    if kt:
        print("List ĐỐI XỨNG (Palindrome).")
    else:
        print("List KHÔNG đối xứng.")

if __name__ == "__main__":
    main()