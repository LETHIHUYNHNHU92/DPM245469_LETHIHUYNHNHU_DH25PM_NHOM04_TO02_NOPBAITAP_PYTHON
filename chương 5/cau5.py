def phan_tich_chuoi(s):
    
    nguyen_am_set = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}

    count_hoa = 0
    count_thuong = 0
    count_chu_so = 0
    count_khoang_trang = 0
    count_nguyen_am = 0
    count_phu_am = 0
    count_dac_biet = 0
    
    for char in s:
        
       
        if char.isspace(): #kiem tra khoang trang
            count_khoang_trang += 1
            continue

        # 2. Kiểm tra Chữ số
        if char.isdigit():
            count_chu_so += 1
            continue

        # 3. Kiểm tra Chữ cái (IN HOA / in thường / Nguyên Âm / Phụ Âm)
        if char.isalpha():
            # A. Đếm IN HOA và in thường
            if char.isupper():
                count_hoa += 1
            else:
                count_thuong += 1
            
            # B. Đếm Nguyên Âm và Phụ Âm
            if char in nguyen_am_set:
                count_nguyen_am += 1
            else:
                count_phu_am += 1
            
            continue # Đã xử lý xong ký tự này

        # 4. Ký tự Đặc biệt (Bằng cách loại trừ: bất cứ thứ gì còn lại)
        else:
            count_dac_biet += 1
            
    # Trả về kết quả dưới dạng dictionary
    return {
        "IN HOA": count_hoa,
        "IN THƯỜNG": count_thuong,
        "CHỮ SỐ": count_chu_so,
        "KHOẢNG TRẮNG": count_khoang_trang,
        "NGUYÊN ÂM": count_nguyen_am,
        "PHỤ ÂM": count_phu_am,
        "KÝ TỰ ĐẶC BIỆT": count_dac_biet,
    }

def main():
    
    print(" PHÂN TÍCH VÀ ĐẾM KÝ TỰ ")
    
    s = input("Nhập vào một chuỗi bất kỳ: ")
    
    ket_qua = phan_tich_chuoi(s)
    
    print("\n--- KẾT QUẢ XUẤT RA ---")
    print(f"Tổng số ký tự trong chuỗi: {len(s)}")
    print("-" * 30)
    
    # In ra kết quả chi tiết
    print(f"1. Số chữ IN HOA:             {ket_qua['IN HOA']}")
    print(f"2. Số chữ in thường:          {ket_qua['IN THƯỜNG']}")
    print(f"3. Số chữ là chữ số:          {ket_qua['CHỮ SỐ']}")
    print(f"4. Số chữ là khoảng trắng:    {ket_qua['KHOẢNG TRẮNG']}")
    print(f"5. Số ký tự đặc biệt:         {ket_qua['KÝ TỰ ĐẶC BIỆT']}")
    print(f"6. Số Nguyên Âm (chữ cái):    {ket_qua['NGUYÊN ÂM']}")
    print(f"7. Số Phụ Âm (chữ cái):       {ket_qua['PHỤ ÂM']}")

if __name__ == "__main__":
    main()