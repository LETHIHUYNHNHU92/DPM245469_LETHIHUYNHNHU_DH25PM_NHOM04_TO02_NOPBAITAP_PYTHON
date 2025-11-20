import math

def is_prime(n):
   
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: # Loại trừ tất cả số chẵn > 2
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True

def phan_tich_list(M):
   
    le = []; chan = []; nt = []; khong_nt = []

    for n in M:
        if n % 2 != 0:
            le.append(n)
        else:
            chan.append(n)
            
        if is_prime(n):
            nt.append(n)
        else:
            khong_nt.append(n)
            
    return {
        'le': le, 'chan': chan, 'nt': nt, 'khong_nt': khong_nt
    }

def main():
    M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]
    
    ket_qua = phan_tich_list(M)
    
    print("KẾT QUẢ XỬ LÝ MẢNG")
    print(f"Mảng đầu vào M: {M}")
    print("-" * 40)
    
    le = ket_qua['le']
    print(f"Dòng 1: {le} -> {len(le)} số lẻ.")
    
    chan = ket_qua['chan']
    print(f"Dòng 2: {chan} -> {len(chan)} số chẵn.")
    
    nt = ket_qua['nt']
    print(f"Dòng 3: {nt} -> {len(nt)} số nguyên tố.")
    
    khong_nt = ket_qua['khong_nt']
    print(f"Dòng 4: {khong_nt} -> {len(khong_nt)} số không phải là số nguyên tố.")

if __name__ == "__main__":
    main()