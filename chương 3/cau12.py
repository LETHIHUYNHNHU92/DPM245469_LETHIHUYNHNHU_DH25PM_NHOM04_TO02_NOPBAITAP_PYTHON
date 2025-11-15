print("--- CÂU 12: XUẤT BẢNG CỬU CHƯƠNG 2->9 ---")

# Vòng lặp bên ngoài: chạy từ 1 đến 10 (số nhân i)
# (Đây là các hàng)
for i in range(1, 11):
    
    # Vòng lặp bên trong: chạy từ 2 đến 9 (số cửu chương j)
    # (Đây là các cột)
    for j in range(2, 10):
        
        # 1. Tính kết quả
        ket_qua = j * i
        
        # 2. Tạo chuỗi định dạng (f-string)
        # {j} là số cửu chương (ví dụ: 2)
        # {i: >2} là số nhân (ví dụ: 1 hoặc 10). 
        #   : >2 nghĩa là "căn lề phải trong 2 ký tự"
        # {ket_qua: >2} là kết quả. 
        #   : >2 cũng là "căn lề phải trong 2 ký tự"
        
        line = f"{j} * {i: >2} = {ket_qua: >2}"
        
        # 3. In chuỗi và kết thúc bằng một phím Tab (\t)
        # 'end=\t' ngăn không cho xuống dòng, mà thay bằng 1 Tab
        print(line, end='\t')
        
    # 4. Xuống dòng
    # Sau khi vòng lặp 'j' (cột) chạy xong (từ 2 đến 9),
    # chúng ta cần xuống dòng để bắt đầu hàng 'i' tiếp theo.
    print()