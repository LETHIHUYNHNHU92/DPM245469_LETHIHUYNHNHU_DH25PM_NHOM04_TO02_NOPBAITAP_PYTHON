
def oscillate(start, stop):
    """
    Một generator function lặp từ 'start' đến 'stop' (không bao gồm stop).
    Với mỗi số, nó 'yield' (trả về) số đó VÀ số đối của nó.
    """
    
    # Vòng lặp for chạy từ -3, -2, -1, 0, 1, 2, 3, 4
    for i in range(start, stop):
        
        # 1. Trả về số hiện tại
        yield i
        
        # 2. Trả về số đối của nó (i * -1)
        yield i * -1

print("Kết quả chạy:")

# Vòng lặp này sẽ gọi hàm oscillate
for n in oscillate(-3, 5):
    print(n, end=' ')

# In một dòng mới cho đẹp
print()