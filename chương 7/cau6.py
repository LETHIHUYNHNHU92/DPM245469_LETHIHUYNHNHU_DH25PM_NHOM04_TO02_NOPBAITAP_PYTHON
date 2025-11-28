import csv
import os

FILE_NAME = "datacsv.csv"

def tao_file_mau(path):
    """Tạo file CSV mẫu để chương trình có thể chạy."""
    content = [
        "ma;ten",
        "nv1;obama",
        "nv2;Kim Jong un",
        "nv3;Putin"
    ]
    # Ghi dữ liệu vào file
    with open(path, 'w', newline='', encoding='utf-8') as f:
        f.write('\n'.join(content) + '\n')
    print(f"✅ Đã tạo file mẫu: {path}")

def xuat_du_lieu_csv(path):
    """
    Đọc file CSV, dùng delimiter=';' và xuất Mã và Tên.
    """
    print("\n--- KẾT QUẢ TRÍCH LỌC CSV ---")
    print("Mã\t\tTên")
    print("----------------------------")
    
    try:
        # Mở file ở chế độ đọc 'r', 'newline=""' là cần thiết cho CSV trên Windows
        with open(path, 'r', newline="", encoding='utf-8') as f:
            # 1. TẠO READER: Chỉ định delimiter=';'
            reader = csv.reader(f, delimiter=';')
            
            # 2. Bỏ qua dòng tiêu đề (Header: "ma;ten")
            next(reader) 
            
            # 3. Lặp qua các dòng dữ liệu và xuất
            for row in reader:
                # row[0] là Mã, row[1] là Tên
                ma = row[0]
                ten = row[1]
                
                # Xuất ra màn hình
                print(f"{ma:<8}\t{ten}")
                
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {path}. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

def main():
    # 1. Tạo file mẫu nếu chưa tồn tại
    if not os.path.exists(FILE_NAME):
        tao_file_mau(FILE_NAME)
        
    # 2. Thực hiện đọc và xuất dữ liệu
    xuat_du_lieu_csv(FILE_NAME)

if __name__ == "__main__":
    main()