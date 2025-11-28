import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def solve_ptb1():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        # Xử lý lỗi nếu người dùng nhập chữ
        ket_qua_var.set("Lỗi: Hệ số a, b phải là số.")
        return

    if a == 0:
        if b == 0:
            ket_qua_var.set("Kết quả: Vô số nghiệm")
        else:
            ket_qua_var.set("Kết quả: Vô nghiệm")
    else:
        x = -b / a
        ket_qua_var.set(f"Kết quả: x = {x:.2f}")

def clear_fields():
    """Xóa trắng các ô nhập liệu và kết quả."""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    ket_qua_var.set("Kết quả:")

def exit_app():
    """Thoát ứng dụng."""
    root.quit()

# --- THIẾT KẾ GIAO DIỆN TKINTER ---

# Tạo cửa sổ chính
root = tk.Tk()
root.title("PTB1")

# Biến để lưu kết quả xuất ra màn hình
ket_qua_var = tk.StringVar(root, value="Kết quả:")

# Cấu hình layout cột
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

label_title = ttk.Label(root, text="Phương Trình Bậc 1", 
                        font=("Arial", 16, "bold"), 
                        foreground="red")
label_title.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=10)

ttk.Label(root, text="Hệ số a:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry_a = ttk.Entry(root)
entry_a.grid(row=1, column=1, sticky='we', padx=10, pady=5)
entry_a.insert(0, "5") # Giá trị mẫu 5

# Hàng 2: Hệ số b
ttk.Label(root, text="Hệ số b:").grid(row=2, column=0, sticky='w', padx=10, pady=5)
entry_b = ttk.Entry(root)
entry_b.grid(row=2, column=1, sticky='we', padx=10, pady=5)
entry_b.insert(0, "9") # Giá trị mẫu 9

# Hàng 3: Khung nút bấm
frame_buttons = ttk.Frame(root)
frame_buttons.grid(row=3, column=0, columnspan=2, pady=10)

# Nút Giải
ttk.Button(frame_buttons, text="Giải", command=solve_ptb1).pack(side='left', padx=10, ipadx=10)
# Nút Tiếp (Clear)
ttk.Button(frame_buttons, text="Tiếp", command=clear_fields).pack(side='left', padx=10, ipadx=10)
# Nút Thoát
ttk.Button(frame_buttons, text="Thoát", command=exit_app).pack(side='left', padx=10, ipadx=10)

# Hàng 4: Kết quả (Sử dụng Entry để mô phỏng ô xuất kết quả)
entry_ket_qua = ttk.Entry(root, textvariable=ket_qua_var, state='readonly', 
                          font=("Arial", 10))
entry_ket_qua.grid(row=4, column=0, columnspan=2, sticky='we', padx=10, pady=(5, 20))

root.mainloop()