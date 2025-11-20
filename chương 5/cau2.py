def ToiUuChuoi(s):
    """
    Hàm tối ưu chuỗi: Loại bỏ khoảng trắng thừa ở đầu, cuối và giữa các từ.
    """
    s2 = s
    s2 = s2.strip() #strip de bo khoang trong thua
    
    # 2. Chia chuỗi thành một mảng (list) các từ, 
    #    việc này tạo ra các chuỗi rỗng trong mảng nếu có nhiều khoảng trắng.
    arr = s2.split(' ')
    
    s2 = ""  # Khởi tạo chuỗi mới để chứa kết quả tối ưu
    
    # 3. Lặp qua mảng và chỉ giữ lại các từ không rỗng
    for x in arr:
        word = x
        
        # Kiểm tra nếu độ dài của từ > 0 ( không phải là chuỗi rỗng)
        if len(word.strip()) != 0:
            # Thêm từ vào chuỗi mới, theo sau là MỘT khoảng trắng
            s2 = s2 + word + " "
            
    # 4. Trả về kết quả, dùng .strip() một lần nữa để loại bỏ khoảng trắng 
    #    dư thừa cuối cùng mà chúng ta đã thêm vào sau từ cuối cùng.
    return s2.strip()

s = "   Trần Duy    Thanh    "
print(f"Chuỗi gốc: '{s}'")
print(f"Độ dài chuỗi gốc: {len(s)}")

# Tối ưu chuỗi
s_toi_uu = ToiUuChuoi(s)

# In kết quả sau khi tối ưu
print(f"\nChuỗi sau tối ưu: '{s_toi_uu}'")
print(f"Độ dài chuỗi tối ưu: {len(s_toi_uu)}")