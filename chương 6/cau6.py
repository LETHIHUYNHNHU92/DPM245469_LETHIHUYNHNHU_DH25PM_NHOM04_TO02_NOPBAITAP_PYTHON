import random

def tao_list_doc_nhat(N, gioi_han_tren=1000):
    """
        N (int): Số lượng phần tử cần tạo.
        gioi_han_tren (int): Phạm vi số ngẫu nhiên (ví dụ: từ 1 đến 1000).
    """
    
    if N <= 0:
        return []
        
    if N > gioi_han_tren:
        print(f"Cảnh báo: Phạm vi số (1-{gioi_han_tren}) không đủ để tạo {N} số độc nhất.")
        N = gioi_han_tren
    
    pool_so = range(1, gioi_han_tren + 1)
    
    # random.sample() đảm bảo tính độc nhất
    list_doc_nhat = random.sample(pool_so, N)
    
    return list_doc_nhat

def main():
    print("TẠO LIST N SỐ NGẪU NHIÊN KHÔNG TRÙNG NHAU ")
    
    try:
        n_input = input("Nhập số lượng phần tử N cần tạo: ")
        N = int(n_input)
        
        if N < 0:
            print("Lỗi: N phải là số nguyên không âm.")
            return

        final_list = tao_list_doc_nhat(N)
        
        print("-" * 50)
        if final_list:
            print(f"✅ Đã tạo List {len(final_list)} phần tử độc nhất (trong phạm vi 1-1000).")
            print(f"List kết quả: {final_list}")
        else:
             print("List rỗng được tạo.")
             
    except ValueError:
        print(f"Lỗi: '{n_input}' không phải là số nguyên hợp lệ.")
        
if __name__ == "__main__":
    main()