import tkinter as tk
from tkinter import font
# PhotoImage được tích hợp sẵn trong tkinter
# from tkinter import PhotoImage 

# --- Bảng màu "Xanh dương trang nhã quý phái" ---
COLOR_SIDEBAR = "#5D8AA8"      # Xanh da trời (Air Force Blue)
COLOR_CONTENT_BG = "#F4F6F7"   # Xám/Trắng rất nhạt (Nền)
COLOR_BUTTON = "#4B6F8A"      # Xanh đậm hơn (Nút)
COLOR_BUTTON_HOVER = "#3A5A74" # Xanh đậm nhất (Hover)
COLOR_BUTTON_TEXT = "#FFFFFF"  # Chữ trắng
COLOR_CONTENT_TEXT = "#212F3D" # Xanh đen (Chữ trên nền chính)

class LibraryApp:
    def __init__(self, root):
        root.title("Phần mềm Quản lý Thư viện - ĐH An Giang")
        root.geometry("1100x600")
        root.configure(bg=COLOR_CONTENT_BG)

        # Giữ tham chiếu đến ảnh nền để không bị Python xóa mất
        self.bg_image = None 

        # --- 1. Tạo Khung Sidebar (Menu bên trái) ---
        self.sidebar_frame = tk.Frame(root, bg=COLOR_SIDEBAR, width=220)
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.pack_propagate(False)

        # --- 2. Tạo Khung Nội dung chính (Bên phải) ---
        self.content_frame = tk.Frame(root, bg=COLOR_CONTENT_BG)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # --- Thêm các nút chức năng vào Sidebar ---
        
        # Tiêu đề
        title_label = tk.Label(self.sidebar_frame, 
                               text="Thư viện AGU", 
                               bg=COLOR_SIDEBAR, 
                               fg=COLOR_BUTTON_TEXT,
                               font=font.Font(size=15, weight="bold"))
        title_label.pack(pady=20, padx=10)

        # Danh sách các nút
        buttons_info = [
            ("Tổng quan", self.show_dashboard_screen),
            ("Nghiệp vụ Mượn/Trả", self.show_borrow_return_screen),
            ("Quản lý Sách", self.show_book_management_screen),
            ("Quản lý Bạn đọc", self.show_user_management_screen),
            ("Thống kê & Báo cáo", self.show_stats_screen),
            ("Quản lý Quy định", self.show_settings_screen)
        ]

        self.buttons = {}
        for (text, command) in buttons_info:
            button = tk.Button(self.sidebar_frame, 
                               text=text, 
                               command=command,
                               bg=COLOR_BUTTON, 
                               fg=COLOR_BUTTON_TEXT, 
                               font=font.Font(size=11),
                               relief="flat",
                               anchor="w",
                               padx=20, pady=10)
            
            button.pack(fill="x", pady=4, padx=15)
            button.bind("<Enter>", self.on_button_hover)
            button.bind("<Leave>", self.on_button_leave)
            
            self.buttons[text] = button

        # --- 3. Hiển thị màn hình chính (Tổng quan) lúc khởi động ---
        self.show_dashboard_screen()

    # --- Các hàm "chuyển trang" ---
    
    def clear_content_frame(self):
        """Xóa tất cả widget trong khung nội dung"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
    def reset_button_colors(self):
        """Đặt lại màu cho tất cả các nút"""
        for btn in self.buttons.values():
            btn.config(bg=COLOR_BUTTON)

    def show_dashboard_screen(self):
        """
        Hiển thị màn hình Tổng quan (Dashboard) VỚI ẢNH NỀN
        """
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Tổng quan"].config(bg=COLOR_BUTTON_HOVER) 
        
        try:
            # 1. Tải ảnh nền
            # Đảm bảo bạn có file "library_bg.png" cùng thư mục file code
            self.bg_image = tk.PhotoImage(file="library_bg.png")
            
            # 2. Tạo Label chứa ảnh nền
            # Dùng .place() để nó lấp đầy khung content_frame
            bg_label = tk.Label(self.content_frame, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            # 3. Đặt chữ chào mừng LÊN TRÊN ảnh nền
            # Tạo một khung nhỏ có nền màu để chữ dễ đọc hơn
            overlay_frame = tk.Frame(self.content_frame, 
                                     bg=COLOR_CONTENT_BG, 
                                     highlightthickness=1, 
                                     highlightbackground=COLOR_SIDEBAR)
            # Đặt khung này vào giữa
            overlay_frame.place(relx=0.5, rely=0.4, anchor="center")

            label = tk.Label(overlay_frame, 
                             text="Chào mừng bạn đến với\nHệ thống Quản lý Thư viện!",
                             bg=COLOR_CONTENT_BG, # Nền của khung overlay
                             fg=COLOR_CONTENT_TEXT, 
                             font=font.Font(size=18, weight="bold"),
                             padx=30, pady=20)
            label.pack()

        except tk.TclError:
            # Xử lý nếu không tìm thấy file ảnh "library_bg.png"
            label = tk.Label(self.content_frame, 
                             text="Chào mừng bạn đến với Hệ thống Quản lý Thư viện!\n\n(Lỗi: Không tìm thấy file library_bg.png)",
                             bg=COLOR_CONTENT_BG,
                             fg="red", # Báo lỗi màu đỏ
                             font=font.Font(size=18))
            label.pack(pady=50, padx=50)

    # --- CÁC HÀM KHÁC SẼ HIỂN THỊ NỀN TRƠN ---
    # (Điều này là tốt để tập trung vào chức năng)

    def show_borrow_return_screen(self):
        """Hiển thị màn hình Nghiệp vụ Mượn/Trả"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Nghiệp vụ Mượn/Trả"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Mượn và Trả Sách",
                         bg=COLOR_CONTENT_BG,
                         fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)

    def show_book_management_screen(self):
        """Hiển thị màn hình Quản lý Sách"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Sách"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Quản lý Sách (Thêm, Sửa, Xóa, Tìm kiếm)",
                         bg=COLOR_CONTENT_BG,
                         fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)

    def show_user_management_screen(self):
        """Hiển thị màn hình Quản lý Bạn đọc"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Bạn đọc"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Quản lý Bạn đọc (Sinh viên)",
                         bg=COLOR_CONTENT_BG,
                         fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)

    def show_stats_screen(self):
        """Hiển thị màn hình Thống kê"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Thống kê & Báo cáo"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Thống kê và Báo cáo",
                         bg=COLOR_CONTENT_BG,
                         fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        
    def show_settings_screen(self):
        """Hiển thị màn hình Quản lý Quy định"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Quy định"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Cài đặt Quy định",
                         bg=COLOR_CONTENT_BG,
                         fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)

    # --- Hàm hiệu ứng cho nút ---
    def on_button_hover(self, event):
        button = event.widget
        if button.cget("bg") == COLOR_BUTTON:
            button.config(bg=COLOR_BUTTON_HOVER)

    def on_button_leave(self, event):
        button = event.widget
        if button.cget("bg") == COLOR_BUTTON_HOVER:
            button.config(bg=COLOR_BUTTON)


# --- Khởi chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()