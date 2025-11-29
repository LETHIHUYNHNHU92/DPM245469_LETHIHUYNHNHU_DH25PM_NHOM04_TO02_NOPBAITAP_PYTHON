import tkinter as tk
from tkinter import ttk, messagebox

expression = ""  # Lưu trữ biểu thức tính toán (ví dụ: "12+3*4")

def button_click(item):
    """Thêm số hoặc phép toán vào biểu thức."""
    global expression
    expression += str(item)
    input_text.set(expression)

def button_clear():
    """Xóa toàn bộ biểu thức và màn hình hiển thị."""
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    """Đánh giá (evaluate) biểu thức và hiển thị kết quả."""
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        # Đặt kết quả làm nền cho phép tính tiếp theo
        expression = result 
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")
        input_text.set("")
        expression = ""
    except Exception:
        messagebox.showerror("Lỗi", "Cú pháp không hợp lệ.")
        input_text.set("")
        expression = ""


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")

# Biến để lưu trữ và hiển thị nội dung trên màn hình (Entry)
input_text = tk.StringVar()

# 1. Màn hình hiển thị (Display Screen)
input_field = ttk.Entry(root, textvariable=input_text, justify='right', font=('Arial', 18))
# Trải dài qua tất cả 4 cột
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, padx=10, sticky="nsew")

# Định nghĩa các nút theo thứ tự từ trên xuống dưới, trái sang phải
buttons_layout = [
    '1', '2', '3', 
    '4', '5', '6',
    '7', '8', '9',
    '-', '0', '.',
    '+', '*', '/', '=',
]

r = 1 # Bắt đầu từ hàng 1
c = 0 # Bắt đầu từ cột 0

# Vòng lặp để tạo các nút và gán vào grid
for button in buttons_layout:
    # Xác định hành động (dùng lambda để truyền giá trị của nút)
    action = lambda x=button: button_click(x)
    
    # Xác định hàm command cho nút '='
    if button == '=':
        btn = ttk.Button(root, text=button, command=button_equal, width=5)
    else:
        btn = ttk.Button(root, text=button, command=action, width=5)
        
    # Gán nút vào grid
    btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
        
    # Di chuyển sang cột tiếp theo
    c += 1
    # Nếu hết cột 3 (c=4), chuyển xuống hàng mới và reset cột
    if c > 3:
        c = 0
        r += 1
        
# 3. Nút Clear (Hàng 6, trải dài 4 cột)
ttk.Button(root, text="Clr", command=button_clear).grid(row=6, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

# Cấu hình các hàng và cột co giãn đều
for i in range(7): # 7 rows total (0 to 6)
    root.grid_rowconfigure(i, weight=1)
for i in range(4): # 4 columns total (0 to 3)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()