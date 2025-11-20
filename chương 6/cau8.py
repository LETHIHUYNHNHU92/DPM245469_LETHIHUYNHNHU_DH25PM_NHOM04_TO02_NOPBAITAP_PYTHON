def sap_xep_giam_dan():
    print("SẮP XẾP DÃY SỐ GIẢM DẦN ")
    
    try:
        n_input = input("Nhập số lượng phần tử N: ")
        N = int(n_input)
    except ValueError:
        print("❌ Lỗi: N phải là số nguyên hợp lệ.")
        return

    if N <= 0:
        print("Cảnh báo: Số lượng phần tử phải lớn hơn 0.")
        return

    M = []
    print(f"\nNhập {N} số thực:")
    
    for i in range(N):
        while True: 
            try:
                so_thuc = float(input(f"Nhập phần tử thứ {i + 1}: "))
                M.append(so_thuc)
                break  
            except ValueError:
                print("❌ Lỗi: Vui lòng nhập SỐ THỰC (ví dụ: 10.5, -3). Nhập lại.")
                
    M.sort(reverse=True) #sap xep giam dan
    
    print("\n--- KẾT QUẢ ---")
    print(f"Dãy số sau khi sắp xếp giảm dần là: {M}")

if __name__ == "__main__":
    sap_xep_giam_dan()