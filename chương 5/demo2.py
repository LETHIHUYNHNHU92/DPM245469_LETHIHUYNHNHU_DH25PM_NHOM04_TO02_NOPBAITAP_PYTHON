import tkinter as tk
from tkinter import ttk, font, messagebox

# --- Màu sắc ---
COLOR_SIDEBAR = "#5D8AA8"
COLOR_CONTENT_BG = "#F4F6F7"
COLOR_BUTTON = "#4B6F8A"
COLOR_BUTTON_HOVER = "#3A5A74"
COLOR_BUTTON_TEXT = "#FFFFFF"
COLOR_CONTENT_TEXT = "#212F3D"

class LibraryApp:
    def __init__(self, root):
        root.title("Phần mềm Quản lý Thư viện - ĐH An Giang")
        root.geometry("1150x650")
        root.configure(bg=COLOR_CONTENT_BG)

        # Sidebar
        self.sidebar_frame = tk.Frame(root, bg=COLOR_SIDEBAR, width=220)
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.pack_propagate(False)

        self.content_frame = tk.Frame(root, bg=COLOR_CONTENT_BG)
        self.content_frame.pack(side="right", fill="both", expand=True)

        title_label = tk.Label(self.sidebar_frame, text="Thư viện AGU", 
                               bg=COLOR_SIDEBAR, fg="white",
                               font=font.Font(size=15, weight="bold"))
        title_label.pack(pady=20)

        buttons_info = [
            ("Tổng quan", self.show_dashboard_screen),
            ("Quản lý Sách", self.show_book_management_screen),
        ]
        self.buttons = {}
        for text, command in buttons_info:
            btn = tk.Button(self.sidebar_frame, text=text, command=command,
                            bg=COLOR_BUTTON, fg="white",
                            font=font.Font(size=11),
                            relief="flat", anchor="w", padx=20, pady=10)
            btn.pack(fill="x", pady=4, padx=15)
            btn.bind("<Enter>", self.on_button_hover)
            btn.bind("<Leave>", self.on_button_leave)
            self.buttons[text] = btn

        self.show_dashboard_screen()

    # --- Các màn hình ---
    def clear_content_frame(self):
        for w in self.content_frame.winfo_children():
            w.destroy()

    def reset_button_colors(self):
        for b in self.buttons.values():
            b.config(bg=COLOR_BUTTON)

    def show_dashboard_screen(self):
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Tổng quan"].config(bg=COLOR_BUTTON_HOVER)
        label = tk.Label(self.content_frame, 
                         text="Chào mừng bạn đến với Hệ thống Quản lý Thư viện!",
                         bg=COLOR_CONTENT_BG, fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18))
        label.pack(pady=50)

    # --- Giao diện Quản lý Sách ---
    def show_book_management_screen(self):
        self.clear_content_frame()
        self.reset_button_colors()
        self.buttons["Quản lý Sách"].config(bg=COLOR_BUTTON_HOVER)

        title = tk.Label(self.content_frame, text="QUẢN LÝ SÁCH", 
                         bg=COLOR_CONTENT_BG, fg=COLOR_CONTENT_TEXT,
                         font=font.Font(size=18, weight="bold"))
        title.pack(pady=10)

        # --- Form nhập sách ---
        form_frame = tk.Frame(self.content_frame, bg=COLOR_CONTENT_BG)
        form_frame.pack(pady=10)

        labels = ["Mã sách", "Tên sách", "Tác giả", "Thể loại", "Năm XB", "Số lượng"]
        self.entries = {}

        for i, lbl in enumerate(labels):
            tk.Label(form_frame, text=lbl, bg=COLOR_CONTENT_BG, fg=COLOR_CONTENT_TEXT, font=font.Font(size=10)).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=35)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entries[lbl] = entry

        add_btn = tk.Button(form_frame, text="➕ Thêm sách", bg=COLOR_BUTTON, fg="white",
                            font=font.Font(size=10, weight="bold"),
                            relief="flat", command=self.add_book)
        add_btn.grid(row=len(labels), column=1, pady=10, sticky="e")

        # --- Bảng Treeview ---
        columns = ("Mã sách", "Tên sách", "Tác giả", "Thể loại", "Năm XB", "Số lượng")
        self.tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor="center")
        self.tree.pack(padx=15, pady=10, fill="x")

        # --- Thanh cuộn ---
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def add_book(self):
        values = [entry.get().strip() for entry in self.entries.values()]
        if any(v == "" for v in values):
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đầy đủ thông tin sách!")
            return
        self.tree.insert("", "end", values=values)
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    # --- Hover hiệu ứng ---
    def on_button_hover(self, e):
        if e.widget.cget("bg") == COLOR_BUTTON:
            e.widget.config(bg=COLOR_BUTTON_HOVER)

    def on_button_leave(self, e):
        if e.widget.cget("bg") == COLOR_BUTTON_HOVER:
            e.widget.config(bg=COLOR_BUTTON)

# --- Chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
