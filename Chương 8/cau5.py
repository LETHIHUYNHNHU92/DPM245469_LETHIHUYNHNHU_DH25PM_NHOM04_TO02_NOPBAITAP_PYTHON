import tkinter as tk
from tkinter import ttk, messagebox

def check_password():
    """
    Hàm xử lý khi nút OK được bấm.
    Kiểm tra xem mật khẩu mới có khớp nhau không.
    """
    old_pass = entry_old.get()
    new_pass = entry_new.get()
    confirm_pass = entry_confirm.get()
    
    # Kiểm tra mật khẩu mới có khớp nhau không
    if new_pass != confirm_pass:
        messagebox.showerror("Lỗi", "Mật khẩu mới không khớp! Vui lòng nhập lại.")
    else:
        messagebox.showinfo("Thành công", "Mật khẩu đã được cập nhật thành công!")
        print(f"Old Password: {old_pass}, New Password: {new_pass}")

def cancel_operation():
    """Đóng ứng dụng."""
    root.quit()


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Enter New Password")

# Cấu hình layout cột
root.columnconfigure(0, weight=1) # Cột cho Label
root.columnconfigure(1, weight=3) # Cột cho Entry

# Tiêu đề
label_title = ttk.Label(root, text="Enter New Password", 
                        font=("Arial", 12, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='w')


# 1. Old Password
ttk.Label(root, text="Old Password:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry_old = ttk.Entry(root, show='*', width=30) # show='*' để ẩn ký tự
entry_old.grid(row=1, column=1, sticky='we', padx=10, pady=5)

# 2. New Password
ttk.Label(root, text="New Password:").grid(row=2, column=0, sticky='w', padx=10, pady=5)
entry_new = ttk.Entry(root, show='*', width=30)
entry_new.grid(row=2, column=1, sticky='we', padx=10, pady=5)

# 3. Enter New Password Again
ttk.Label(root, text="Enter New Password Again:").grid(row=3, column=0, sticky='w', padx=10, pady=5)
entry_confirm = ttk.Entry(root, show='*', width=30)
entry_confirm.grid(row=3, column=1, sticky='we', padx=10, pady=5)

# --- Khung chứa các nút bấm (Căn giữa) ---
frame_buttons = ttk.Frame(root)
frame_buttons.grid(row=4, column=0, columnspan=2, pady=(15, 10))

# Nút OK
ttk.Button(frame_buttons, text="OK", command=check_password, width=10).pack(side='left', padx=10, ipadx=10)

# Nút Cancel
ttk.Button(frame_buttons, text="Cancel", command=cancel_operation, width=10).pack(side='left', padx=10, ipadx=10)

root.mainloop()