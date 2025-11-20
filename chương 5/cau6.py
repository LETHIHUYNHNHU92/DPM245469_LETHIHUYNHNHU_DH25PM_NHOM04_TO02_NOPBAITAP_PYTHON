import re  # Import thư viện Regular Expression (Biểu thức chính quy)

def NegativeNumberInStrings(s):
    
    # Mẫu: '-' (Dấu trừ) theo sau bởi '\d+' (một hoặc nhiều chữ số)
    regex_pattern = r'-\d+'
    
    # 2. Sử dụng re.findall để tìm tất cả các chuỗi con khớp với mẫu
    # Kết quả là một list các chuỗi (ví dụ: ['-5', '-12'])
    chuoi_so_am = re.findall(regex_pattern, s)
    
    # 3. Chuyển đổi chuỗi thành số nguyên và xuất ra
    so_am_ket_qua = []
    
    print("\n--- KẾT QUẢ TRÍCH LỌC ---")
    print("Các số nguyên âm được tìm thấy:")
    
    for chuoi in chuoi_so_am:
        try:
            so = int(chuoi)
            so_am_ket_qua.append(so)
            print(so) # Xuất từng số ra màn hình
        except ValueError:
            # Trường hợp không xảy ra với mẫu regex này, nhưng là biện pháp phòng ngừa
            pass
            
    return so_am_ket_qua

def main():

    chuoi_test_1 = "abc-5xyz-12k9l--p"
    print(f"Chuỗi đầu vào 1: '{chuoi_test_1}'")
    NegativeNumberInStrings(chuoi_test_1)
    
    chuoi_test_2 = "Gia_tri: -99.9; Chi phi: -1000, 200"
    print(f"\nChuỗi đầu vào 2: '{chuoi_test_2}'")
    NegativeNumberInStrings(chuoi_test_2)
    
if __name__ == "__main__":
    main()