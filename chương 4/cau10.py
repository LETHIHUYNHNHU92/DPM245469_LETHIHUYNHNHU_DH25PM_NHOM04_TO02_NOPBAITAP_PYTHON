import time  # Thư viện để dùng hàm sleep() (nghỉ)
import os    # Thư viện để dùng hàm xóa màn hình (clear screen)

def xoa_man_hinh():
    """
    Hàm này kiểm tra hệ_điều hành để_gọi_lệnh_xóa màn hình cho đúng.
    'nt' là Windows (dùng lệnh 'cls')
    Các hệ_điều hành khác như macOS, Linux (dùng lệnh 'clear')
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Định nghĩa 4 hình ảnh bằng chuỗi (string) nhiều dòng ---


hinh_1 = """
    *
   * *
  * * *
* * * * *
  * * *
  * * *
    *
"""

hinh_2 = """
    *
   * *
  * * *
* * * * *
  * * *
    * *
      *
"""

hinh_3 = """
* * * *
* *
* *
  * *
  * *
  * *
* * * *
"""

hinh_4 = """
* * *
 * *
  * * *
   * *
  * *
 * *
* *
"""

# Tạo một danh sách (list) chứa cả 4 hình
cac_hinh = [hinh_1, hinh_2, hinh_3, hinh_4]

# --- Vòng lặp chính để_hiển_thị ---

print("Chuẩn bị xem hoạt ảnh... (mỗi hình 5 giây)")
time.sleep(2)  # Chờ 2 giây để người dùng đọc

# Lặp qua từng hình trong danh sách
for i in range(len(cac_hinh)):
    
    xoa_man_hinh()  # Xóa màn hình trước khi vẽ hình mới
    
    print(f"Hình {i + 1} / {len(cac_hinh)}")
    print(cac_hinh[i])  # In hình hiện tại
    
    # yêu cầu : Dừng 5 giây
    time.sleep(5)

# Xóa màn hình khi kết thúc
xoa_man_hinh()
print("Đã kết thúc.")