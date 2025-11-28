import json
import os
import operator
from datetime import datetime

# --- CẤU TRÚC DỮ LIỆU VÀ I/O (JSON) ---
FILE_PATH = "quanly_sinhvien.json"

def DocFileJSON():
    """Đọc dữ liệu từ file JSON và chuyển thành Dictionary Python."""
    if not os.path.exists(FILE_PATH):
        return {} 
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = f.read()
            if not data: return {}
            return json.loads(data)
    except Exception:
        # Xử lý trường hợp file bị hỏng
        return {}

def LuuFileJSON(data):
    """Lưu Dictionary Python vào file dưới dạng JSON."""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            # indent=4 giúp file dễ đọc, ensure_ascii=False giúp giữ tiếng Việt
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Lỗi: Không thể lưu dữ liệu vào file. {e}")
        return False

# --- CÁC HÀM XỬ LÝ CƠ BẢN (CRUD) ---

def ThemSinhVien(ds_lop):
    """1. Lưu mới sinh viên."""
    print("\n--- THÊM SINH VIÊN MỚI ---")
    
    # 1. Nhập thông tin Sinh viên
    ma_lop = input("Nhập Mã Lớp (Ví dụ: L01): ").upper().strip()
    ma_sv = input("Nhập Mã Sinh Viên: ").upper().strip()
    ten_sv = input("Nhập Tên Sinh Viên: ").strip()
    
    while True:
        try:
            nam_sinh = int(input("Nhập Năm Sinh (Ví dụ: 2004): "))
            if 1950 < nam_sinh <= datetime.now().year:
                break
            print("Năm sinh không hợp lệ.")
        except ValueError:
            print("Năm sinh phải là số nguyên.")
            
    # 2. Xử lý Danh mục Lớp
    if ma_lop not in ds_lop:
        ten_lop = input(f"Lớp '{ma_lop}' chưa tồn tại. Nhập tên lớp mới: ").strip()
        ds_lop[ma_lop] = {'Ten_Lop': ten_lop, 'Students': []}
    
    # 3. Kiểm tra trùng mã SV (trong toàn bộ hệ thống)
    if any(sv['Mã'] == ma_sv for dm in ds_lop.values() for sv in dm['Students']):
        print(f"Lỗi: Mã sinh viên '{ma_sv}' đã tồn tại trong hệ thống.")
        return

    # 4. Thêm sinh viên vào lớp
    ds_lop[ma_lop]['Students'].append({
        'Mã': ma_sv,
        'Tên': ten_sv,
        'Năm Sinh': nam_sinh
    })
    
    LuuFileJSON(ds_lop)
    print(f"Đã thêm sinh viên {ma_sv} vào lớp {ma_lop}.")

def TimKiemSinhVien(ds_lop):
    """3. Tìm kiếm sinh viên theo tên hoặc mã."""
    tu_khoa = input("Nhập tên hoặc mã SV/Lớp cần tìm: ").lower().strip()
    
    ket_qua_tim = []
    
    for ma_lop, lop_data in ds_lop.items():
        # Kiểm tra trùng với Tên Lớp hoặc Mã Lớp
        if tu_khoa in lop_data['Ten_Lop'].lower() or tu_khoa == ma_lop.lower():
             # Thêm tất cả sinh viên trong lớp đó vào kết quả tìm kiếm
             for sv in lop_data['Students']:
                 ket_qua_tim.append(sv)
             continue 

        # Kiểm tra trùng với Tên SV hoặc Mã SV
        for sv in lop_data['Students']:
            if tu_khoa in sv['Tên'].lower() or tu_khoa == sv['Mã'].lower():
                ket_qua_tim.append(sv)
                
    if ket_qua_tim:
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        for sv in ket_qua_tim:
            print(f"[{sv['Mã']} | {sv['Năm Sinh']}] Tên: {sv['Tên']}, Lớp: {ma_lop}")
    else:
        print(f"Không tìm thấy kết quả nào với từ khóa '{tu_khoa}'.")

def XoaSinhVien(ds_lop):
    """4. Xóa sinh viên khỏi hệ thống."""
    ma_sv_xoa = input("Nhập Mã Sinh Viên cần xóa: ").upper().strip()
    
    for ma_lop, lop_data in ds_lop.items():
        # Tìm index của sinh viên cần xóa trong list Products
        # Dùng enumerate để lấy cả index và object
        for i, sv in enumerate(lop_data['Students']):
            if sv['Mã'] == ma_sv_xoa:
                # Xóa sinh viên khỏi list
                lop_data['Students'].pop(i)
                LuuFileJSON(ds_lop)
                print(f"Đã xóa thành công sinh viên {ma_sv_xoa} khỏi lớp {ma_lop}.")
                return
                
    print(f"Không tìm thấy sinh viên có mã '{ma_sv_xoa}'.")

def XuatDanhSach(ds_lop, sap_xep=False):
    """2. Xuất toàn bộ dữ liệu ra màn hình."""
    if not ds_lop:
        print("Danh sách rỗng.")
        return

    # Tạo một list phẳng (flattened list) để dễ dàng xuất và sắp xếp
    all_students = []
    for ma_lop, lop_data in ds_lop.items():
        for sv in lop_data['Students']:
            all_students.append({
                'Mã Lớp': ma_lop,
                'Tên Lớp': lop_data['Ten_Lop'],
                'Mã SV': sv['Mã'],
                'Tên SV': sv['Tên'],
                'Năm Sinh': sv['Năm Sinh']
            })

    # Nếu có sắp xếp, sắp xếp theo Tên (Name)
    if sap_xep:
        all_students.sort(key=operator.itemgetter('Tên SV')) # Mặc định tăng dần A-Z
        print("\n--- DANH SÁCH ĐÃ SẮP XẾP THEO TÊN (A-Z) ---")
    else:
        print("\n--- DANH SÁCH SINH VIÊN (NGUYÊN GỐC) ---")

    print("="*60)
    print(f"| {'Mã Lớp':<6} | {'Mã SV':<5} | {'Tên Sinh Viên':<25} | {'Năm Sinh':<10} |")
    print("="*60)
    
    for p in all_students:
        print(f"| {p['Mã Lớp']:<6} | {p['Mã SV']:<5} | {p['Tên SV']:<25} | {p['Năm Sinh']:<10} |")
    print("="*60)

# --- HÀM MAIN MENU ---

def main_menu():
    # Đảm bảo file tồn tại và khởi tạo với dictionary rỗng nếu không có
    if not os.path.exists(FILE_PATH):
        LuuFileJSON({}) 

    ds_sinh_vien = DocFileJSON()
    
    while True:
        print("\n" + "*"*50)
        print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (JSON FILE)")
        print("1. Lưu mới sinh viên")
        print("2. Xuất toàn bộ danh sách (Sắp xếp theo Tên)")
        print("3. Tìm kiếm sinh viên/lớp")
        print("4. Xóa sinh viên theo Mã")
        print("5. Xuất toàn bộ danh sách (Thứ tự gốc)")
        print("0. Thoát & Lưu")
        print("*"*50)
        
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        
        if lua_chon == '1':
            ThemSinhVien(ds_sinh_vien)
        elif lua_chon == '2':
            XuatDanhSach(ds_sinh_vien, sap_xep=True)
        elif lua_chon == '3':
            TimKiemSinhVien(ds_sinh_vien)
        elif lua_chon == '4':
            XoaSinhVien(ds_sinh_vien)
        elif lua_chon == '5':
            XuatDanhSach(ds_sinh_vien, sap_xep=False)
        elif lua_chon == '0':
            print("Đang thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main_menu()