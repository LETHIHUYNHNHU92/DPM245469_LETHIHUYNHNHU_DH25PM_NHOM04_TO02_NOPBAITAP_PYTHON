import xlsxwriter
import os # Cần thiết để kiểm tra lỗi file

def tao_file_excel_san_pham(filename="demo.xlsx"):
    
    print(f"Bắt đầu tạo file '{filename}'...")
    try:
        # 1. Tạo workbook và worksheet
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
    except Exception as e:
        print(f"Lỗi khi tạo file Workbook: {e}")
        return

    
    # 2. Định dạng in đậm (bold format)
    bold = workbook.add_format({'bold': True})
    
    # 3. Thiết lập chiều rộng cột (set_column)
    worksheet.set_column('A:A', 5)   
    worksheet.set_column('B:B', 15)  
    worksheet.set_column('C:C', 20)  
    worksheet.set_column('D:D', 15)  
    worksheet.set_column('E:E', 15) 

    # 4. Ghi tiêu đề (Hàng 1)
    worksheet.write('A1', 'STT', bold)
    worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
    worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
    worksheet.write('D1', 'SỐ LƯỢNG', bold)
    worksheet.write('E1', 'ĐƠN GIÁ', bold)

    # 5. Ghi dữ liệu mẫu (Hàng 2 và Hàng 3)
    worksheet.write('A2', 1)
    worksheet.write('B2', 'SP1')
    worksheet.write('C2', 'CocaCola')
    worksheet.write('D2', 15)
    worksheet.write('E2', 15000)
    
    worksheet.write('A3', 2)
    worksheet.write('B3', 'SP2')
    worksheet.write('C3', 'Pepsi')
    worksheet.write('D3', 20)
    worksheet.write('E3', 18000)
    
    # 6. Chèn Logo vào ô B5 (Chỉ chạy nếu có file 'logo.png')
    try:
        # Kiểm tra sự tồn tại của file trước khi chèn
        if os.path.exists('logo.png'):
             worksheet.insert_image('B5', 'logo.png')
             print("Đã chèn logo vào B5.")
        else:
             print("Cảnh báo: Không tìm thấy file ảnh 'logo.png'.")
    except Exception as e:
        # Bắt lỗi nếu file ảnh tồn tại nhưng bị lỗi định dạng
        print(f"Lỗi chèn ảnh: {e}")
        
    # 7. Đóng workbook (BẮT BUỘC)
    workbook.close()
    print(f"\n✅ Đã tạo file Excel thành công: {filename}")

if __name__ == "__main__":
    tao_file_excel_san_pham()