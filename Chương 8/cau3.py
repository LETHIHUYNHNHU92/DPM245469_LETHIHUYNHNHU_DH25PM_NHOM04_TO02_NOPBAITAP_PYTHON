import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate(operation):
    """Thực hiện phép toán dựa trên nút bấm."""
    try:
        # Lấy giá trị từ ô nhập liệu và chuyển sang số thực (float)
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        # Xử lý lỗi nếu người dùng nhập chữ
        ket_qua_var.set("Lỗi: Dữ liệu nhập không hợp lệ.")
        return

    result = None
    
    # Thực hiện phép toán
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            # Xử lý lỗi chia cho 0
            ket_qua_var.set("Lỗi: Không thể chia cho 0.")
            return
        result = a / b
    
    # Cập nhật kết quả (dùng .1f để làm tròn 1 chữ số thập phân, giống ví dụ)
    if result is not None:
        ket_qua_var.set(f"{result:.1f}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("tk") 

# Tạo StringVar cho kết quả
ket_qua_var = tk.StringVar(root, value="-1.0") # Giá trị khởi tạo -1.0

# Tiêu đề (Phù hợp với thiết kế ảnh)
label_title = ttk.Label(root, text="Cộng trừ nhân chia", 
                        font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

frame_buttons = ttk.Frame(root)
frame_buttons.grid(row=1, column=0, rowspan=3, sticky='nsw', padx=10, pady=5) 

ttk.Button(frame_buttons, text="Cộng", command=lambda: calculate('+')).pack(fill='x', pady=2, ipadx=10)
ttk.Button(frame_buttons, text="Trừ", command=lambda: calculate('-')).pack(fill='x', pady=2)
ttk.Button(frame_buttons, text="Nhân", command=lambda: calculate('*')).pack(fill='x', pady=2)
ttk.Button(frame_buttons, text="Chia", command=lambda: calculate('/')).pack(fill='x', pady=2)

ttk.Label(root, text="số a:").grid(row=1, column=1, sticky='w', padx=5, pady=5)
entry_a = ttk.Entry(root, width=15)
entry_a.grid(row=1, column=1, sticky='e', padx=10, pady=5)
entry_a.insert(0, "6") # Giá trị mẫu 6

ttk.Label(root, text="số b:").grid(row=2, column=1, sticky='w', padx=5, pady=5)
entry_b = ttk.Entry(root, width=15)
entry_b.grid(row=2, column=1, sticky='e', padx=10, pady=5)
entry_b.insert(0, "7") # Giá trị mẫu 7

ttk.Label(root, text="kết quả:").grid(row=3, column=1, sticky='w', padx=5, pady=5)
entry_result = ttk.Entry(root, width=15, textvariable=ket_qua_var, state='readonly')
entry_result.grid(row=3, column=1, sticky='e', padx=10, pady=5)

# Thoát Button (Bottom right)
ttk.Button(root, text="Thoát", command=root.quit).grid(row=4, column=1, sticky='se', padx=10, pady=(5, 10), ipadx=10)

root.mainloop()