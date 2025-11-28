import xml.dom.minidom
import os
import time

FILE_PATH = "employees.xml"

def tao_file_xml_mau(path):
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<employees>
  <employee>
    <id>1</id>
    <name>Trần Duy Thanh</name>
  </employee>
  <employee>
    <id>2</id>
    <name>Lê Hoành Sư</name>
  </employee>
  <employee>
    <id>3</id>
    <name>Hồ Trung Thành</name>
  </employee>
</employees>"""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        print(f"✅ Đã tạo file mẫu: {path}")
    except IOError as e:
        print(f"Lỗi khi tạo file: {e}")

def doc_du_lieu_xml(path):
    """
    Đọc dữ liệu từ file XML bằng phương thức DOM (minidom).
    """
    if not os.path.exists(path):
        print(f"Lỗi: Không tìm thấy file {path}.")
        return

    print("\n--- KẾT QUẢ ĐỌC DỮ LIỆU XML ---")
    print("ID\t\tTên Nhân Viên")
    print("---------------------------------")
    
    try:
        # Mở file xml bằng minidom parser
        # Dùng xml.dom.minidom.parse() để tạo cây DOM
        DOMTree = xml.dom.minidom.parse(path)
        
        # Lấy phần tử gốc (root element)
        employees_collection = DOMTree.documentElement
        
        # Lấy tất cả các tag <employee>
        employees = employees_collection.getElementsByTagName("employee")
        
        # Duyệt vòng lặp để lấy bộ dữ liệu ra 
        for employee in employees:
            
            # Lấy tag <id> (luôn là phần tử đầu tiên [0])
            tag_id_node = employee.getElementsByTagName('id')[0]
            # Lấy giá trị data bên trong tag <id>
            employee_id = tag_id_node.childNodes[0].data
            
            # Lấy tag <name>
            tag_name_node = employee.getElementsByTagName('name')[0]
            # Lấy giá trị data bên trong tag <name>
            employee_name = tag_name_node.childNodes[0].data
            
            # In ra màn hình
            print(f"{employee_id:<8}\t{employee_name}")
            
    except Exception as e:
        print(f"Lỗi khi parsing XML: {e}")
        
def main():
   
    tao_file_xml_mau(FILE_PATH)
    
    doc_du_lieu_xml(FILE_PATH)
    
    # Dọn dẹp file mẫu sau khi chạy xong 
    os.remove(FILE_PATH) 

if __name__ == "__main__":
    main()