def kiem_tra_doi_xung(chuoi):
    
    n = len(chuoi)
    # Lặp từ đầu đến giữa (n // 2)
    for i in range(n // 2):
        # So sánh ký tự ở vị trí i (từ trái) 
        # với ký tự ở vị trí đối xứng (n - 1 - i) (từ phải)
        if chuoi[i] != chuoi[n - 1 - i]:
            return False  
            
    return True  

def main():
  
    while True:
        print("\n--- KIỂM TRA CHUỖI ĐỐI XỨNG ---")
        
        # Dùng .strip() để loại bỏ khoảng trắng thừa
        s = input("Nhập Chuỗi: ").strip()
        
        if kiem_tra_doi_xung(s):
            print("==> Chuỗi bạn nhập ĐỐI XỨNG.")
        else:
            print("==> Chuỗi bạn nhập KHÔNG đối xứng.")
            
        while True:
            lua_chon = input("Tiếp tục nhập Chuỗi mới? (c/k): ").lower().strip()
            
            if lua_chon == 'k':
                print("\nCẢM ƠN BẠN ĐÃ SỬ DỤNG PHẦN MỀM.")
                return  
            elif lua_chon == 'c':
                break  
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'c' hoặc 'k'.")

if __name__ == "__main__":
    main()