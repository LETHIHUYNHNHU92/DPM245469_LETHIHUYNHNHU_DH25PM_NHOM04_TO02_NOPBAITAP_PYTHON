import json
import os
import operator

# --- CẤU TRÚC DỮ LIỆU VÀ I/O (JSON) ---
FILE_PATH = "quanly_sanpham.json"

def DocDuLieu():
    """Đọc dữ liệu từ file JSON và chuyển thành Dictionary Python."""
    if not os.path.exists(FILE_PATH):
        # Nếu file không tồn tại, trả về cấu trúc rỗng ban đầu
        return {} 
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = f.read()
            if not data: return {}
            return json.loads(data)
    except Exception:
        return {}

def LuuDuLieu(data):
    """Lưu Dictionary Python vào file dưới dạng JSON."""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            # indent=4 và ensure_ascii=False giúp file JSON dễ đọc và giữ tiếng Việt
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Lưu dữ liệu thành công.")
    except Exception as e:
        print(f"Lỗi: Không thể lưu dữ liệu vào file. {e}")

# --- CÁC HÀM XỬ LÝ CƠ BẢN ---

def XuatDuLieu(ds_danh_muc, sap_xep=False):
    """Xuất toàn bộ dữ liệu ra màn hình."""
    if not ds_danh_muc:
        print("Danh sách rỗng.")
        return

    print("\n" + "="*50)
    print(f"| {'Mã DM':<5} | {'Tên Danh Mục':<20} | {'Mã SP':<5} | {'Tên Sản Phẩm':<20} | {'Đơn Giá':<10} |")
    print("="*50)
    
    # Tạo một list phẳng (flattened list) để sắp xếp
    all_products = []
    for ma_dm, dm_data in ds_danh_muc.items():
        for sp in dm_data['Products']:
            all_products.append({
                'Mã DM': ma_dm,
                'Tên SP': sp['Tên'],
                'Mã SP': sp['Mã'],
                'Giá': sp['Giá']
            })

    # Nếu có sắp xếp, sắp xếp theo giá
    if sap_xep:
        all_products.sort(key=operator.itemgetter('Giá'), reverse=True)
        print("--- ĐÃ SẮP XẾP THEO ĐƠN GIÁ GIẢM DẦN ---")

    for p in all_products:
        print(f"| {p['Mã DM']:<5} | {ds_danh_muc[p['Mã DM']]['Ten_DM']:<20} | {p['Mã SP']:<5} | {p['Tên SP']:<20} | {p['Giá']:<10,.2f} |")
    
    print("="*50)

def ThemSanPham(ds_danh_muc):
    """Lưu mới sản phẩm."""
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    
    # 1. Nhập thông tin sản phẩm
    ma_dm = input("Nhập Mã Danh Mục (Ví dụ: DM01): ").upper().strip()
    ten_sp = input("Nhập Tên Sản Phẩm: ").strip()
    ma_sp = input("Nhập Mã Sản Phẩm: ").upper().strip()
    
    while True:
        try:
            don_gia = float(input("Nhập Đơn Giá: "))
            break
        except ValueError:
            print("Đơn giá phải là số hợp lệ.")
            
    # 2. Xử lý Danh mục
    if ma_dm not in ds_danh_muc:
        ten_dm = input(f"Danh mục '{ma_dm}' chưa tồn tại. Nhập tên danh mục mới: ").strip()
        ds_danh_muc[ma_dm] = {'Ten_DM': ten_dm, 'Products': []}
        
    # 3. Kiểm tra trùng mã SP trong danh mục (Logic đơn giản)
    for sp in ds_danh_muc[ma_dm]['Products']:
        if sp['Mã'] == ma_sp:
            print(f"Lỗi: Mã sản phẩm '{ma_sp}' đã tồn tại trong danh mục '{ma_dm}'.")
            return
            
    # 4. Thêm sản phẩm vào danh mục
    ds_danh_muc[ma_dm]['Products'].append({
        'Mã': ma_sp,
        'Tên': ten_sp,
        'Giá': don_gia
    })
    
    LuuDuLieu(ds_danh_muc)
    print(f"Đã thêm sản phẩm {ma_sp} vào danh mục {ma_dm}.")

def TimKiemSanPham(ds_danh_muc):
    """Tìm kiếm sản phẩm theo tên hoặc mã."""
    tu_khoa = input("Nhập tên hoặc mã sản phẩm cần tìm: ").lower().strip()
    
    ket_qua_tim = []
    
    for ma_dm, dm_data in ds_danh_muc.items():
        for sp in dm_data['Products']:
            if tu_khoa in sp['Tên'].lower() or tu_khoa == sp['Mã'].lower():
                ket_qua_tim.append({
                    'Mã DM': ma_dm,
                    'Tên SP': sp['Tên'],
                    'Mã SP': sp['Mã'],
                    'Giá': sp['Giá']
                })
                
    if ket_qua_tim:
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        for p in ket_qua_tim:
            print(f"[{p['Mã DM']} - {p['Mã SP']}] Tên: {p['Tên SP']}, Giá: {p['Giá']:,} VND")
    else:
        print(f"Không tìm thấy sản phẩm nào với từ khóa '{tu_khoa}'.")

# --- HÀM MAIN MENU ---

def main_menu():
    ds_san_pham = DocDuLieu()
    
    while True:
        print("\n" + "*"*40)
        print("CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM (TEXT FILE - JSON)")
        print("1. Lưu mới sản phẩm")
        print("2. Sắp xếp và xuất toàn bộ danh sách (theo giá giảm dần)")
        print("3. Tìm kiếm sản phẩm")
        print("4. Xuất toàn bộ danh sách (theo thứ tự file)")
        print("0. Thoát & Lưu")
        print("*"*40)
        
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        
        if lua_chon == '1':
            ThemSanPham(ds_san_pham)
        elif lua_chon == '2':
            XuatDuLieu(ds_san_pham, sap_xep=True)
        elif lua_chon == '3':
            TimKiemSanPham(ds_san_pham)
        elif lua_chon == '4':
            XuatDuLieu(ds_san_pham, sap_xep=False)
        elif lua_chon == '0':
            print("Đang thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    # Đảm bảo file tồn tại để không bị lỗi lúc khởi tạo
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write('{}') # Khởi tạo file với dictionary rỗng
            
    main_menu()