import xml.dom.minidom
import os
import sys

FILE_PATH = "nhomthietbi.xml"

# --- 1. HÀM HỖ TRỢ: TẠO FILE XML MẪU ---
def tao_file_xml_mau(path):
    """Tạo file XML mẫu chứa danh sách nhóm thiết bị theo cấu trúc đề bài."""
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<nhoms>
  <nhom>
    <ma>n1</ma>
    <ten>Nhóm 1</ten>
  </nhom>
  <nhom>
    <ma>n2</ma>
    <ten>Nhóm 2</ten>
  </nhom>
  <nhom>
    <ma>n3</ma>
    <ten>Nhóm 3</ten>
  </nhom>
</nhoms>"""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        print(f"✅ Đã tạo file mẫu: {path}")
    except IOError as e:
        print(f"Lỗi khi tạo file: {e}")

# --- 2. HÀM ĐỌC DỮ LIỆU VÀ TRÍCH XUẤT ---
def DocNhomThietBi(path):
    """
    Đọc dữ liệu từ XML, trích xuất Mã và Tên của từng nhóm.
    """
    ds_nhom = []
    if not os.path.exists(path):
        return ds_nhom

    try:
        # 1. Parse và lấy phần tử gốc
        DOMTree = xml.dom.minidom.parse(path)
        root = DOMTree.documentElement
        
        # 2. Lấy tất cả các tag <nhom>
        nhom_nodes = root.getElementsByTagName("nhom")
        
        # 3. Duyệt qua từng node <nhom>
        for nhom in nhom_nodes:
            # Lấy giá trị data của tag <ma>
            ma = nhom.getElementsByTagName('ma')[0].childNodes[0].data
            
            # Lấy giá trị data của tag <ten>
            ten = nhom.getElementsByTagName('ten')[0].childNodes[0].data
            
            ds_nhom.append({'Mã': ma, 'Tên': ten})
            
    except Exception as e:
        print(f"Lỗi khi parsing XML: {e}")
        
    return ds_nhom

def main():
    print("--- QUẢN LÝ THIẾT BỊ (XỬ LÝ XML) ---")
    # Đảm bảo file mẫu được tạo trước khi đọc
    tao_file_xml_mau(FILE_PATH)
    
    # Đọc dữ liệu
    ds_nhom = DocNhomThietBi(FILE_PATH)
    
    # Xuất kết quả
    print("\n--- KẾT QUẢ DANH SÁCH NHÓM THIẾT BỊ ---")
    if ds_nhom:
        for nhom in ds_nhom:
            print(f"| Mã: {nhom['Mã']:<4} | Tên Nhóm: {nhom['Tên']}")
    else:
        print("Không có dữ liệu nhóm nào được đọc.")

if __name__ == "__main__":
    main()