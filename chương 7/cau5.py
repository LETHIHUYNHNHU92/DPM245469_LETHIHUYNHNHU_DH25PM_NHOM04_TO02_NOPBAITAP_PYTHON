import json

def chuyen_doi_python_to_json():
    """
    Chuyển đổi đối tượng Python (Dictionary) sang chuỗi JSON (String).
    """
    pythonObject = {
        "ten": "Trần Duy Thanh",
        "tuoi": 50,
        "ma": "nv1"
    }
    
    print("--- DỮ LIỆU GỐC (PYTHON DICTIONARY) ---")
    print(pythonObject)

    # 2. Thực hiện chuyển đổi JSON
    # json.dumps() (dump string) là phương thức dùng để chuyển đổi Python Object sang JSON String.
    # indent=4 giúp chuỗi JSON dễ đọc hơn.
    # ensure_ascii=False giúp hiển thị tiếng Việt chính xác.
    jsonString = json.dumps(pythonObject, indent=4, ensure_ascii=False)
    
    print("\n--- KẾT QUẢ SAU KHI CHUYỂN ĐỔI (JSON STRING) ---")
    print(jsonString)
    print(f"\nLoại dữ liệu: {type(jsonString)}")

if __name__ == "__main__":
    chuyen_doi_python_to_json()