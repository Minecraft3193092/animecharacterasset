import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Python 視窗")
root.geometry("300x200")

def on_click():
    messagebox.showinfo("提示", "哈囉！")

# 使用 pack 佈局，自動置中並堆疊
button = tk.Button(root, text="點我", command=on_click)
button.pack(pady=60)

root.mainloop()