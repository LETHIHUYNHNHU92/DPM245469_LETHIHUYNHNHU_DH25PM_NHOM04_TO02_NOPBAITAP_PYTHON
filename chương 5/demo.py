import tkinter as tk
from tkinter import font

# --- Định nghĩa màu sắc và font chữ (để trông "hiện đại" hơn) ---
COLOR_SIDEBAR = "#2c3e50"  # Màu xanh đen
COLOR_CONTENT_BG = "#ecf0f1"  # Màu xám rất nhạt
COLOR_BUTTON = "#34495e"  # Màu xanh đậm hơn
COLOR_BUTTON_HOVER = "#4a637c" # Màu khi di chuột
COLOR_BUTTON_TEXT = "#ffffff"  # Màu chữ trắng

class LibraryApp:
    def __init__(self, root):
        root.title("Phần mềm Quản lý Thư viện - ĐH An Giang")
        root.geometry("1100x600")
        root.configure(bg=COLOR_CONTENT_BG)

        # --- 1. Tạo Khung Sidebar (Menu bên trái) ---
        self.sidebar_frame = tk.Frame(root, bg=COLOR_SIDEBAR, width=220)
        self.sidebar_frame.pack(side="left", fill="y")
        
        # Ngăn không cho sidebar co lại
        self.sidebar_frame.pack_propagate(False)

        # --- 2. Tạo Khung Nội dung chính (Bên phải) ---
        self.content_frame = tk.Frame(root, bg=COLOR_CONTENT_BG)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # --- Thêm các nút chức năng vào Sidebar ---
        # Dựa trên file .docx của bạn [cite: 52, 74]
        
        # Tiêu đề
        title_label = tk.Label(self.sidebar_frame, 
                               text="Thư viện AGU", 
                               bg=COLOR_SIDEBAR, 
                               fg=COLOR_BUTTON_TEXT,
                               font=font.Font(size=15, weight="bold"))
        title_label.pack(pady=20, padx=10)

        # Danh sách các nút
        # Các chức năng này lấy từ file của bạn [cite: 52, 69, 54, 55, 56, 74]
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
                               relief="flat",  # Tắt viền 3D
                               anchor="w",     # Căn chữ về bên trái (West)
                               padx=20, pady=10)
            
            button.pack(fill="x", pady=4, padx=15)
            
            # Thêm hiệu ứng di chuột (hover)
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
        """Hiển thị màn hình Tổng quan"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Tổng quan"].config(bg=COLOR_BUTTON_HOVER) # Highlight nút được chọn
        
        label = tk.Label(self.content_frame, 
                         text="Chào mừng bạn đến với Hệ thống Quản lý Thư viện!",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        
        # Bạn có thể thêm các ô thống kê nhanh ở đây
        # (Số sách đang mượn, số bạn đọc, số sách quá hạn...)

    def show_borrow_return_screen(self):
        """Hiển thị màn hình Nghiệp vụ Mượn/Trả"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Nghiệp vụ Mượn/Trả"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Mượn và Trả Sách",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        # (Nơi đây sẽ là giao diện để nhập Mã SV và Mã Sách)

    def show_book_management_screen(self):
        """Hiển thị màn hình Quản lý Sách"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Sách"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Quản lý Sách (Thêm, Sửa, Xóa, Tìm kiếm)",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        # (Nơi đây sẽ là bảng (Treeview) hiển thị danh sách sách)

    def show_user_management_screen(self):
        """Hiển thị màn hình Quản lý Bạn đọc"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Bạn đọc"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Quản lý Bạn đọc (Sinh viên)",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        # (Nơi đây sẽ là bảng (Treeview) hiển thị danh sách sinh viên)

    def show_stats_screen(self):
        """Hiển thị màn hình Thống kê"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Thống kê & Báo cáo"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Thống kê và Báo cáo",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        # (Nơi đây sẽ là các biểu đồ hoặc bảng thống kê)
        
    def show_settings_screen(self):
        """Hiển thị màn hình Quản lý Quy định"""
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Quy định"].config(bg=COLOR_BUTTON_HOVER)
        
        label = tk.Label(self.content_frame, 
                         text="Giao diện Cài đặt Quy định",
                         bg=COLOR_CONTENT_BG,
                         font=font.Font(size=18))
        label.pack(pady=50, padx=50)
        # (Nơi đây sẽ là các ô để nhập số ngày mượn, số sách tối đa...)

    # --- Hàm hiệu ứng cho nút ---
    def on_button_hover(self, event):
        """Thay đổi màu khi di chuột vào nút (nếu nút đó không được chọn)"""
        button = event.widget
        if button.cget("bg") == COLOR_BUTTON: # Chỉ đổi màu nếu không phải nút đang active
            button.config(bg=COLOR_BUTTON_HOVER)

    def on_button_leave(self, event):
        """Thay đổi màu khi di chuột rời khỏi nút (nếu nút đó không được chọn)"""
        button = event.widget
        if button.cget("bg") == COLOR_BUTTON_HOVER: # Chỉ đổi màu nếu không phải nút đang active
            button.config(bg=COLOR_BUTTON)


# --- Khởi chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()