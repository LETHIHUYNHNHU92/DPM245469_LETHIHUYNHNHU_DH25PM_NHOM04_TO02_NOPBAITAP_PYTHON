import os # Cần import os để lấy đường dẫn ví dụ 

#  LẤY TÊN FILE (muabui.mp3) 
# d:\\music\muabui.mp3 
def lay_ten_file(duong_dan):
    """
    Sử dụng rsplit để tách chuỗi từ bên phải (sau ký tự '\\')
    và chỉ lấy phần tử cuối cùng (
    """
    # Ta dùng '\\' vì ký tự '\' cần được escape trong chuỗi Python
    # rsplit(separator, maxsplit=1) đảm bảo chỉ tách tại dấu '\' cuối cùng
    return duong_dan.rsplit('\\', 1)[-1]


#  LẤY TÊN BÀI HÁT (muabui) ---
def lay_ten_bai_hat(duong_dan):
   
    ten_file = lay_ten_file(duong_dan)
    
    # Split tại dấu '.' và lấy phần tử đầu tiên ([0])
    return ten_file.split('.')[0]


def main():
    duong_dan_test = "d:\\music\\muabui.mp3"
    
    print(f"Đường dẫn gốc: {duong_dan_test}")
    print("-" * 30)

    # A. Lấy tên file
    ten_file_ket_qua = lay_ten_file(duong_dan_test)
    print(f"1. Tên file đầy đủ: {ten_file_ket_qua}")
    
    # B. Lấy tên bài hát (không extension)
    ten_bai_hat_ket_qua = lay_ten_bai_hat(duong_dan_test)
    print(f"2. Tên bài hát:    {ten_bai_hat_ket_qua}")
    
    # Thử một đường dẫn khác
    duong_dan_khac = "C:\\Users\\Desktop\\05_buh_da_nang.wav"
    print("-" * 30)
    print(f"Đường dẫn khác: {duong_dan_khac}")
    print(f"1. Tên file đầy đủ: {lay_ten_file(duong_dan_khac)}")
    print(f"2. Tên bài hát:    {lay_ten_bai_hat(duong_dan_khac)}")


if __name__ == "__main__":
    main()