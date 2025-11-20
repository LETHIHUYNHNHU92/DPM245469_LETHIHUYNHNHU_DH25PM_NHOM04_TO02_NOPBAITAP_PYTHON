import random
import math

def CheckPrime(n):
    """
    Kiểm tra số nguyên tố bằng cách đếm số ước.
    Trả về True nếu n có đúng 2 ước (1 và chính nó).
    """
    if n <= 1:
        return False
    
    d = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2 # Số nguyên tố có chính xác 2 ước

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ LIST ---")
    
    try:
        n = int(input("Nhập số phần tử khởi tạo N: "))
    except ValueError:
        print("Lỗi: N phải là số nguyên.")
        return

    # Khởi tạo list với N phần tử ngẫu nhiên (từ -100 đến 100)
    lst = []
    for _ in range(n):
        lst.append(random.randrange(-100, 101)) 

    print(f"\nList ngẫu nhiên được tạo: {lst}")
    
    # 2. Thêm phần tử mới
    try:
        value = int(input("Nhập so mới muốn thêm vào list: "))
        lst.append(value)
        print(f"List sau khi thêm: {lst}")
    except ValueError:
        print("Cảnh báo: Giá trị thêm vào không hợp lệ và đã bị bỏ qua.")

    # 3. Kiểm tra k xuất hiện bao nhiêu lần
    try:
        k = int(input("\nNhập k (số muốn đếm): "))
        dem = lst.count(k) # Hàm count() của list
        print(f"Số {k} xuất hiện {dem} lần trong list.")
    except ValueError:
        print("Cảnh báo: Giá trị k không hợp lệ.")
        
    # 4. Tính tổng các số nguyên tố
    dem_nt = 0       
    tong_nt = 0      
    
    for x in lst:
        if CheckPrime(x):
            dem_nt += 1
            tong_nt += x
    
    print(f"\nCó {dem_nt} số nguyên tố trong list. Tổng của chúng là: {tong_nt}")
    
    # 5. Sắp xếp list
    print("\n--- XỬ LÝ LIST ---")
    lst.sort() # Sắp xếp trực tiếp trên list gốc
    print(f"List sau khi Sắp xếp: {lst}")
    
    # 6. Xóa list
    try:
        del lst # Xóa biến 'lst' khỏi bộ nhớ
        print("List đã được Xóa thành công (del lst).")
        
    except NameError:
        print("List không tồn tại nữa.")

if __name__ == "__main__":
    main()