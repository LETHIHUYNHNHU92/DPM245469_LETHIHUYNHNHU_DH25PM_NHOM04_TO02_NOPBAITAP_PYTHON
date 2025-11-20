import sys

def nhap_ma_tran_elements(ten_ma_tran, m, n):
    D = []
    print(f"\n--- NHẬP MA TRẬN {ten_ma_tran} ({m}x{n}) ---")
    for i in range(m):
        row = []
        for j in range(n):
            while True:
                try:
                    val = float(input(f"Nhập phần tử {ten_ma_tran}[{i}][{j}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Lỗi: Vui lòng nhập số hợp lệ.")
        D.append(row)
    return D

def xuat_ma_tran(D, ten="Ma trận"):

    print(f"\n{ten} (Kích thước {len(D)}x{len(D[0])}):")
    for row in D:
        # Dùng .4f để hiển thị số thực gọn gàng hơn
        print([f"{val:.4f}" for val in row]) 

def cong_ma_tran(A, B):

    m_a = len(A)
    n_a = len(A[0])
    m_b = len(B)
    n_b = len(B[0])
    

    if m_a != m_b or n_a != n_b:
        return "Lỗi: Hai ma trận phải có cùng kích thước để cộng."
        
    C = []
    for i in range(m_a):
        row = []
        for j in range(n_a):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def tinh_ma_tran_hoan_vi(A):
   
    m = len(A)    # Số hàng cũ (M)
    n = len(A[0]) # Số cột cũ (N)
    
    # Khởi tạo ma trận mới A_T với kích thước ngược lại (n x m)
    A_T = [[0] * m for _ in range(n)] 
    
    for i in range(m):
        for j in range(n):
            # Đảo vị trí: A_T[j][i] = A[i][j]
            A_T[j][i] = A[i][j] 
            
    return A_T

def main():
    print(" XỬ LÝ MA TRẬN ")
    
    try:
        m = int(input("Nhập số hàng (M): "))
        n = int(input("Nhập số cột (N): "))
        
        if m <= 0 or n <= 0:
            print("Lỗi: Kích thước phải lớn hơn 0.")
            return

        A = nhap_ma_tran_elements('A', m, n)
        B = nhap_ma_tran_elements('B', m, n)

        xuat_ma_tran(A, 'Ma trận A')
        xuat_ma_tran(B, 'Ma trận B')

        C = cong_ma_tran(A, B)
        if isinstance(C, str) and C.startswith("Lỗi"):
            print(f"\n{C}")
        else:
            xuat_ma_tran(C, 'Tổng Ma trận C = A + B')

        print("\n" + "=" * 30)
        A_T = tinh_ma_tran_hoan_vi(A)
        xuat_ma_tran(A_T, 'Ma trận hoán vị A^T')
        
        B_T = tinh_ma_tran_hoan_vi(B)
        xuat_ma_tran(B_T, 'Ma trận hoán vị B^T')
        
    except ValueError:
        print("\nLỗi: Vui lòng chỉ nhập số nguyên cho kích thước hoặc số hợp lệ cho phần tử.")
    except Exception as e:
        print(f"\nĐã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()