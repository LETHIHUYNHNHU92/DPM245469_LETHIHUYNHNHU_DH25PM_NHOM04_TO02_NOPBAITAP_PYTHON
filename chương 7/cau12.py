import csv
import random
import os

FILE_PATH = "du_lieu_nhan_vien.csv"

def LuuTapTin(path):
    """Tạo file CSV chứa 10 dòng, mỗi dòng 10 số ngẫu nhiên."""
    print(f"✅ Đang tạo file {path}...")
    
    # Sử dụng 'w' để ghi đè (tạo file mới)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        # csv.writer để xử lý delimiter=';' một cách chính xác
        writer = csv.writer(f, delimiter=';')
        
        # Tạo 10 dòng dữ liệu
        for _ in range(10):
            # Tạo 10 số ngẫu nhiên từ 1 đến 99 (như trong hình minh họa)
            row_data = [random.randrange(1, 100) for _ in range(10)]
            
            # Ghi dòng dữ liệu vào file
            writer.writerow(row_data) 
            
    print(f"Hoàn thành tạo file với 10x10 số ngẫu nhiên.")