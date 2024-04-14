
"""
    
    作られた Aditya Dwi Nugroho

"""

import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.text_area = tk.Text(self.root, undo=True)
        self.file_path = None
        self.set_up_widgets()

    def set_up_widgets(self):
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="新規作成", command=self.new_file)
        self.file_menu.add_command(label="開く...", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_command(
            label="名前を付けて保存...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="終了", command=self.exit_app)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("無題 - Python Notepad")

    def open_file(self):
        path = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt"),
                                                     ("Python Scripts", "*.py"),
                                                     ("C++ Source Files", "*.cpp"),
                                                     ("HTML Documents", "*.html"),
                                                     ("JavaScript Files", "*.js")])
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Python Notepad")
            with open(path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("保存エラー", e)
        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt"),
                                                       ("Python Scripts", "*.py"),
                                                       ("C++ Source Files", "*.cpp"),
                                                       ("HTML Documents", "*.html"),
                                                       ("JavaScript Files", "*.js")])
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Python Notepad")
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("保存エラー", e)

    def exit_app(self):
        self.root.quit()


def main():
    root = tk.Tk()
    Notepad(root)
    root.mainloop()


if __name__ == "__main__":
    main()

"""
    
    作られた Aditya Dwi Nugroho

"""

import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.text_area = tk.Text(self.root, undo=True)
        self.file_path = None
        self.set_up_widgets()

    def set_up_widgets(self):
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="新規作成", command=self.new_file)
        self.file_menu.add_command(label="開く...", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_command(label="名前を付けて保存...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="終了", command=self.exit_app)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("無題 - Python Notepad")

    def open_file(self):
        path = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt"),
                                                     ("Python Scripts", "*.py"),
                                                     ("C++ Source Files", "*.cpp"),
                                                     ("HTML Documents", "*.html"),
                                                     ("JavaScript Files", "*.js")])
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Python Notepad")
            with open(path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("保存エラー", e)
        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt"),
                                                       ("Python Scripts", "*.py"),
                                                       ("C++ Source Files", "*.cpp"),
                                                       ("HTML Documents", "*.html"),
                                                       ("JavaScript Files", "*.js")])
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Python Notepad")
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("保存エラー", e)

    def exit_app(self):
        self.root.quit()

def main():
    root = tk.Tk()
    Notepad(root)
    root.mainloop()

if __name__ == "__main__":
    main()

