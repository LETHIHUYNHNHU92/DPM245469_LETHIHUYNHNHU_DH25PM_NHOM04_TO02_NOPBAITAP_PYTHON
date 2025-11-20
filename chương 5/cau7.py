def ToiUuChuoiDanhTu(s):
   
   # Tối ưu chuỗi:Xóa khoảng trắng thừa và Viết Hoa chữ cái đầu mỗi từ.
    
    chuoi_thuong = s.lower() # chuyen thanh chu thuong thi ham .capitalize hoat dong chinh xac
    
    danh_sach_tu = chuoi_thuong.split() # tach chuoi thanh tu (xoa khoang trang dau cuoi,xoa khoang trang o giua)
    
    danh_sach_moi = []
    
    for tu in danh_sach_tu:
        tu_toi_uu = tu.capitalize() #(chu dau cua tu viet hoa,con lai viet thuong)
        danh_sach_moi.append(tu_toi_uu) #them tu vao cuoi danh sach
        
    # 4. Nối các từ lại với nhau bằng ĐÚNG một khoảng trắng
    chuoi_toi_uu = " ".join(danh_sach_moi)
    
    return chuoi_toi_uu

def main():
    chuoi_goc_1 = " TRẦN duY   thAnH "
    
    print(f"Chuỗi đầu vào:   '{chuoi_goc_1}'")
    
    chuoi_ket_qua_1 = ToiUuChuoiDanhTu(chuoi_goc_1)
    
    print(f"Chuỗi sau tối ưu: '{chuoi_ket_qua_1}'")
    
    chuoi_test_2 = "   nguyỄN vĂn    a   "
    print(f"\nChuỗi đầu vào:   '{chuoi_test_2}'")
    print(f"Chuỗi sau tối ưu: '{ToiUuChuoiDanhTu(chuoi_test_2)}'")

if __name__ == "__main__":
    main()