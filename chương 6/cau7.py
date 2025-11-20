def nhap_day_so_tang_dan():
    day_so = []
    print("CHƯƠNG TRÌNH NHẬP DÃY SỐ TĂNG DẦN")
    print("Yêu cầu: Số sau phải lớn hơn số trước đó. Nhấn [Enter] để kết thúc.")

    while True:
        
        if day_so:
            thong_bao = f"Nhập số tiếp theo (phải > {day_so[-1]}): "
        else:
            thong_bao = "Nhập số đầu tiên: "
            
        nhap_str = input(thong_bao)
        
        # 1. Điều kiện thoát (Nhấn Enter mà không nhập gì)
        if not nhap_str:
            break
        
        # 2. Kiểm tra tính hợp lệ của số 
        try:
            so_moi = int(nhap_str)
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập SỐ nguyên hợp lệ. Nhập lại.")
            continue # Quay lại đầu vòng lặp

        # 3. KIỂM TRA QUY CÁCH TĂNG DẦN
        if day_so: # Chỉ kiểm tra nếu list đã có phần tử
            if so_moi <= day_so[-1]:
                print(f"❌ Lỗi: Số {so_moi} không lớn hơn số trước đó ({day_so[-1]}). Vui lòng nhập lại.")
                continue # Quay lại đầu vòng lặp
        
       
       # Thêm số mới vào list
        day_so.append(so_moi)
        
    print("\n--- DÃY SỐ ĐÃ NHẬP XONG ---")
    print(day_so)

if __name__ == "__main__":
    nhap_day_so_tang_dan()