import tkinter as tk
from tkinter import ttk

def setup_gui():
    root = tk.Tk()
    root.title("frame 2") 
    
    # Định nghĩa các giá trị borderwidth và kiểu relief
    borderwidth_values = [0, 1, 2, 3, 4]
    relief_styles = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

    # Thiết lập các cột để co giãn đều (cho các nút)
    for i in range(len(relief_styles) + 1): 
        root.columnconfigure(i, weight=1) 
    
    
    row_num = 0 
    
    # Vòng lặp ngoài: Lặp qua giá trị borderwidth (Tạo các HÀNG)
    for border_width in borderwidth_values:
        
        # 1. Tạo label cho hàng (Ví dụ: "borderwidth = 0")
        label_text = f"borderwidth = {border_width}"
        label = ttk.Label(root, text=label_text, anchor='w')
        
        # Đặt label ở cột đầu tiên (Cột 0)
        label.grid(row=row_num, column=0, sticky='w', padx=5, pady=5)
        
        # Vòng lặp trong: Lặp qua kiểu relief (Tạo các CỘT)
        col_num = 1
        for style in relief_styles:
            # 2. Tạo nút bấm (sử dụng tk.Button vì nó hỗ trợ thuộc tính relief)
            btn = tk.Button(root, 
                            text=style,
                            relief=style,           # Đặt kiểu relief
                            borderwidth=border_width, # Đặt độ dày viền
                            fg='black',             
                            padx=10, 
                            pady=5)
            
            # 3. Đặt nút bấm vào lưới
            btn.grid(row=row_num, column=col_num, sticky='nsew', padx=5, pady=5)
            
            col_num += 1
            
        row_num += 1 # Chuyển xuống hàng tiếp theo
        
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
