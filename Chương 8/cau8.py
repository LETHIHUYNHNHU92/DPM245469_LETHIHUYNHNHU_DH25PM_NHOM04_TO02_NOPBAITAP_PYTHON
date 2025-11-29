import tkinter as tk
from tkinter import ttk, messagebox

def convert_temp():
    """Đọc độ F, tính toán và hiển thị độ C."""
    try:
        # Lấy giá trị độ F từ ô nhập liệu và chuyển sang số thực
        do_f = float(entry_f.get())
        
        # Công thức chuyển đổi: C = (F - 32) * 5/9
        do_c = (do_f - 32) * (5/9)
        
        # Cập nhật kết quả hiển thị (làm tròn 2 chữ số thập phân)
        ket_qua_var.set(f"{do_c:.2f}°C")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập độ F bằng số.")
        ket_qua_var.set("Lỗi")
        

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi Nhiệt độ")

# Biến để lưu kết quả xuất ra
ket_qua_var = tk.StringVar(root, value="Độ C ở đây") 

# Cấu hình Styling để tạo nền màu vàng (giống ảnh mẫu)
style = ttk.Style()
style.configure('Yellow.TFrame', background='yellow')
style.configure('Yellow.TLabel', background='yellow', font=('Arial', 11))

# Khung chính (Main Frame) với nền vàng
main_frame = ttk.Frame(root, style='Yellow.TFrame')
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# Label
ttk.Label(main_frame, text="Nhập độ F", style='Yellow.TLabel').grid(row=0, column=0, sticky='w', padx=5, pady=5)

# Input Entry (°F)
entry_f = ttk.Entry(main_frame, width=8, justify='center', font=('Arial', 12, 'bold'), foreground='red')
entry_f.grid(row=0, column=1, sticky='we', padx=5, pady=5)
entry_f.insert(0, "350") # Giá trị mẫu 350

# Nút Chuyển
ttk.Button(main_frame, text="Chuyển", command=convert_temp).grid(row=1, column=1, sticky='we', padx=5, pady=5)

# Label: Độ C
ttk.Label(main_frame, text="Độ C", style='Yellow.TLabel').grid(row=2, column=0, sticky='w', padx=5, pady=5)

output_c = ttk.Entry(main_frame, textvariable=ket_qua_var, state='readonly', 
                           justify='center', font=('Arial', 12, 'bold'), width=15)
output_c.grid(row=2, column=1, sticky='we', padx=5, pady=5)

root.mainloop()