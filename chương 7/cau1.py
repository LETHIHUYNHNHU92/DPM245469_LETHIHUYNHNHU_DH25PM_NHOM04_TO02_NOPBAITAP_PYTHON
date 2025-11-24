import os
import operator
import sys

# Dùng os.path.join để đảm bảo đường dẫn hoạt động trên mọi hệ điều hành
FILE_PATH = os.path.join(os.path.dirname(__file__), "database_san_pham.txt")

def LuuFile(data):
    try:
        # Mở file ở chế độ 'a' (append) để ghi thêm vào cuối file
        with open(FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(data + "\n")
    except IOError:
        print("Lỗi: Không thể ghi vào file.")

def DocFile(path): 
    arrProduct = [] 
    
    # 1. Kiểm tra sự tồn tại của file trước khi mở
    if not os.path.exists(path):
        # Tạo file rỗng nếu chưa tồn tại
        try:
            with open(path, 'w', encoding='utf-8'):
                pass
        except IOError:
            print(f"Lỗi: Không thể tạo file tại {path}.")
        return arrProduct
        
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip() 
                if not data: continue # Bỏ qua dòng trống

                arr = data.split(';')
                
                # 2. KIỂM TRA VÀ CHUYỂN ĐỔI ĐƠN GIÁ
                if len(arr) == 3:
                    try:
                        # Chuyển đổi Đơn giá (index 2) sang float
                        arr[2] = float(arr[2]) 
                        arrProduct.append(arr)
                    except ValueError:
                        # Bắt lỗi nếu Đơn giá không phải là số
                        print(f"Cảnh báo: Đơn giá không hợp lệ trong dòng '{line.strip()}' và bị bỏ qua.")
                
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return []
        
    return arrProduct

# --- CÁC HÀM XỬ LÝ KHÁC (Đã giữ nguyên) ---

def NhapSanPham():
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM ---")
    masp = input("Mã SP: ")
    tensp = input("Tên SP: ")
    
    while True:
        try:
            dongia = float(input("Đơn giá: "))
            break
        except ValueError:
            print("Đơn giá phải là một số. Nhập lại.")
            
    line = f"{masp};{tensp};{dongia}"
    LuuFile(line)

def XuatSanPham(dssp, tieu_de="DANH SÁCH SẢN PHẨM"):
    print(f"\n--- {tieu_de} ---")
    if not dssp:
        print("Danh sách rỗng hoặc chưa có dữ liệu.")
        return
        
    print("Mã SP\tTên Sản Phẩm\t\t\tĐơn Giá")
    print("-------------------------------------------------")
    for row in dssp:
        # row[2] đã là float, nên chỉ cần format để in
        print(f"{row[0]:<7}\t{row[1]:<25}\t{row[2]:.2f}")

def SortSp(dssp):
    # Dùng operator.itemgetter(2) để lấy đơn giá (index 2)
    # reverse=True để sắp xếp giảm dần
    return sorted(dssp, key=operator.itemgetter(2), reverse=True)


def main():
    print("--- QUẢN LÝ SẢN PHẨM (XỬ LÝ TẬP TIN) ---")
    
    dssp_goc = DocFile(FILE_PATH)

    XuatSanPham(dssp_goc, "SẢN PHẨM GỐC TỪ FILE")
    
    dssp_sap_xep = SortSp(dssp_goc)
    XuatSanPham(dssp_sap_xep, "SẢN PHẨM SAU KHI SẮP XẾP THEO GIÁ GIẢM DẦN")

if __name__ == "__main__":
    main()