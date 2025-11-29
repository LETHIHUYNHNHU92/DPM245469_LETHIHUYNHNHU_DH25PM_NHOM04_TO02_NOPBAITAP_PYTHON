import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate_bmi():
    """Đọc chiều cao/cân nặng, tính BMI và phân loại."""
    try:
        # Lấy giá trị từ ô nhập liệu
        # Chú ý: Chiều cao phải là mét (m), Cân nặng là kg
        chieu_cao_m = float(entry_chieu_cao.get())
        can_nang_kg = float(entry_can_nang.get())

        if chieu_cao_m <= 0 or can_nang_kg <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và cân nặng phải lớn hơn 0.")
            return

        # Công thức BMI: Cân nặng (kg) / [Chiều cao (m)]^2
        bmi = can_nang_kg / (chieu_cao_m ** 2)
        
        # 2. Phân loại và đánh giá nguy cơ dựa trên tiêu chuẩn quốc tế
        tinh_trang = ""
        nguy_co = ""

        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif 18.5 <= bmi <= 24.9:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif 25 <= bmi <= 29.9:
            tinh_trang = "Mập"
            nguy_co = "Cao"
        else: # BMI >= 30
            tinh_trang = "Béo phì"
            nguy_co = "Rất cao"
            
        # 3. Cập nhật kết quả hiển thị
        bmi_var.set(f"{bmi:.2f}")
        tinh_trang_var.set(tinh_trang)
        nguy_co_var.set(nguy_co)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập chiều cao và cân nặng bằng số hợp lệ.")
        bmi_var.set("x")
        tinh_trang_var.set("...")
        nguy_co_var.set("...")

def exit_app():
    """Thoát ứng dụng."""
    root.quit()


# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Cấu hình Style để tạo nền màu vàng (giống ảnh mẫu)
style = ttk.Style()
style.configure('Yellow.TFrame', background='yellow')
style.configure('Yellow.TLabel', background='yellow', font=('Arial', 11))

# --- String Variables for Output ---
bmi_var = tk.StringVar(root, value="x")
tinh_trang_var = tk.StringVar(root, value="...") 
nguy_co_var = tk.StringVar(root, value="...") 

# Khung chính (Main Frame) với nền vàng
main_frame = ttk.Frame(root, style='Yellow.TFrame')
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# Cấu hình 2 cột
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=2)

# --- Input Fields (Rows 0-1) ---

# Nhập chiều cao (m)
ttk.Label(main_frame, text="Nhập chiều cao:", style='Yellow.TLabel').grid(row=0, column=0, sticky='w', padx=5, pady=5)
entry_chieu_cao = ttk.Entry(main_frame, width=10, justify='center', font=('Arial', 11))
entry_chieu_cao.grid(row=0, column=1, sticky='we', padx=5, pady=5)
entry_chieu_cao.insert(0, "1.8") # Giá trị mẫu

# Nhập cân nặng (kg)
ttk.Label(main_frame, text="Nhập cân nặng:", style='Yellow.TLabel').grid(row=1, column=0, sticky='w', padx=5, pady=5)
entry_can_nang = ttk.Entry(main_frame, width=10, justify='center', font=('Arial', 11))
entry_can_nang.grid(row=1, column=1, sticky='we', padx=5, pady=5)
entry_can_nang.insert(0, "72") # Đặt 72kg (chứ không phải 172) để có kết quả bình thường

# --- Tính BMI Button (Row 2) ---
ttk.Button(main_frame, text="Tính BMI", command=calculate_bmi).grid(row=2, column=1, sticky='we', padx=5, pady=5)


# BMI của bạn
ttk.Label(main_frame, text="BMI của bạn:", style='Yellow.TLabel').grid(row=3, column=0, sticky='w', padx=5, pady=5)
ttk.Entry(main_frame, textvariable=bmi_var, state='readonly', justify='center', font=('Arial', 11)).grid(row=3, column=1, sticky='we', padx=5, pady=5)

# Tình trạng của bạn
ttk.Label(main_frame, text="Tình trạng của bạn:", style='Yellow.TLabel').grid(row=4, column=0, sticky='w', padx=5, pady=5)
ttk.Entry(main_frame, textvariable=tinh_trang_var, state='readonly', justify='center', font=('Arial', 11)).grid(row=4, column=1, sticky='we', padx=5, pady=5)

# Nguy cơ phát triển bệnh
ttk.Label(main_frame, text="Nguy cơ phát triển bệnh:", style='Yellow.TLabel').grid(row=5, column=0, sticky='w', padx=5, pady=5)
ttk.Entry(main_frame, textvariable=nguy_co_var, state='readonly', justify='center', font=('Arial', 11)).grid(row=5, column=1, sticky='we', padx=5, pady=5)

# Thoát Button (Row 6)
ttk.Button(main_frame, text="Thoát", command=exit_app).grid(row=6, column=1, sticky='we', padx=5, pady=10)

root.mainloop()