import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date 

# --- 1. MẢNG THIÊN CAN & ĐỊA CHI ĐÚNG ---

# Thiên Can (Mod 10): 0: Canh, 1: Tân, 2: Nhâm, 3: Quý, 4: Giáp, 5: Ất, 6: Bính, 7: Đinh, 8: Mậu, 9: Kỷ
# Công thức: (Năm + 6) % 10 (Áp dụng cho mảng này)
CAN_LIST = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"] 

# Địa Chi (Mod 12): 0: Tý, 1: Sửu, 2: Dần, ..., 10: Tuất, 11: Hợi
# Công thức: (Năm + 8) % 12 (Áp dụng cho mảng này)
CHI_LIST = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]


def convert_lunar():
    """Giải quyết logic chuyển năm dương lịch sang năm âm lịch Can Chi."""
    try:
        duong_lich_nam = int(entry_duong_lich.get())
        if duong_lich_nam < 1900 or duong_lich_nam > date.today().year + 5:
             messagebox.showerror("Lỗi", "Năm không hợp lệ. Vui lòng nhập năm gần đây.")
             return

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm bằng số nguyên.")
        return

    # --- Logic Tính Toán đã sửa ---
    
    # 1. Tính Thiên Can: (Năm + 6) % 10. (2006 -> 2 -> Bính)
    can_index = (duong_lich_nam + 6) % 10
    can = CAN_LIST[can_index]
    
    # 2. Tính Địa Chi: (Năm + 8) % 12. (2006 -> 10 -> Tuất)
    chi_index = (duong_lich_nam + 8) % 12
    chi = CHI_LIST[chi_index]
    
    am_lich = f"{can} {chi}"
    
    # Cập nhật kết quả hiển thị
    nam_am_var.set(am_lich)


root = tk.Tk()
root.title("Chuyển đổi Lịch Âm Dương")

style = ttk.Style()
style.configure('Yellow.TFrame', background='yellow')
style.configure('Yellow.TLabel', background='yellow', font=('Arial', 11))

nam_am_var = tk.StringVar(root, value="") 

main_frame = ttk.Frame(root, style='Yellow.TFrame')
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

ttk.Label(main_frame, text="Nhập năm dương:", style='Yellow.TLabel').grid(row=0, column=0, sticky='w', padx=5, pady=5)
entry_duong_lich = ttk.Entry(main_frame, width=8, justify='center', font=('Arial', 12, 'bold'), foreground='red')
entry_duong_lich.grid(row=0, column=1, sticky='we', padx=5, pady=5)
entry_duong_lich.insert(0, "2006") # Đặt giá trị mẫu 2006 để kiểm tra

ttk.Button(main_frame, text="Chuyển", command=convert_lunar).grid(row=1, column=1, sticky='we', padx=5, pady=5)

ttk.Label(main_frame, text="Năm âm:", style='Yellow.TLabel').grid(row=2, column=0, sticky='w', padx=5, pady=5)
output_am_lich = ttk.Entry(main_frame, textvariable=nam_am_var, state='readonly', 
                           justify='center', font=('Arial', 12, 'bold'), width=15)
output_am_lich.grid(row=2, column=1, sticky='we', padx=5, pady=5)

root.mainloop()