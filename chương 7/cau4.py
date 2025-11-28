import json

def xu_ly_json_string():
   
    # Chuỗi JSON đã được sửa lỗi cú pháp (sử dụng nháy kép cho keys/values)
    jsonString = '{"ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'
    
    print("--- DỮ LIỆU GỐC (JSON STRING) ---")
    print(jsonString)

    # 1. Thực hiện chuyển đổi JSON String sang Python Object (Dictionary)
    dataObject = json.loads(jsonString)
    
    print("\n--- KẾT QUẢ SAU KHI CHUYỂN ĐỔI ---")
    print(f"Loại dữ liệu: {type(dataObject)}")
    print(f"Đối tượng Python: {dataObject}")
    
    # 2. Truy xuất dữ liệu từ Python Object (Dictionary)
    print("\n--- TRUY XUẤT DỮ LIỆU ---")
    print(f"Mã nhân viên: {dataObject['ma']}")
    print(f"Tuổi:         {dataObject['age']}")
    print(f"Tên:          {dataObject['ten']}")

if __name__ == "__main__":
    xu_ly_json_string()