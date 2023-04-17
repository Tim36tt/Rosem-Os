import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import platform
from time import strftime

def open_google():
    webbrowser.open_new("https://www.google.com")

def open_app2():
    messagebox.showinfo("Открыть приложение 2", "hello world")

def open_settings():
    messagebox.showinfo("Открыть настройки", "#rosemPhone2.0#")

def open_control_panel():
    messagebox.showinfo("Открыть панель управления", "система не  доступ к кастомизации")

def open_youtube():
    webbrowser.open_new("https://www.youtube.com")

def change_bg_color():
    root.configure(bg="#F0F0F299")

def run_in_thread(func):
    """
    Функция для выполнения функции в отдельном потоке
    """
    thread = threading.Thread(target=func)
    thread.start()

root = tk.Tk()
root.title("Меню Пуск")
root.geometry("200x300")

# Создание фрейма для кнопок
frame_btns = tk.Frame(root, bg="#F0F0F0")
frame_btns.pack(pady=20)

# Создание кнопок
btn_google = tk.Button(frame_btns, text="Поиск Google", command=lambda: run_in_thread(open_google), relief="flat", width=20, height=1)
btn_google.pack(pady=5)

btn_app2 = tk.Button(frame_btns, text="Приложение 2", command=lambda: run_in_thread(open_app2), relief="flat", width=20, height=1)
btn_app2.pack(pady=5)

btn_settings = tk.Button(frame_btns, text="Настройки", command=lambda: run_in_thread(open_settings), relief="flat", width=20, height=1)
btn_settings.pack(pady=5)

btn_control_panel = tk.Button(frame_btns, text="Панель управления", command=lambda: run_in_thread(open_control_panel), relief="flat", width=20, height=1)
btn_control_panel.pack(pady=5)

btn_youtube = tk.Button(frame_btns, text="YouTube", command=lambda: run_in_thread(open_youtube), relief="flat", width=20, height=1)
btn_youtube.pack(pady=5)

# Отображение текущего времени
lbl_time = tk.Label(root, text="", font=("Helvetica", 20), fg="#666666", bg="#F0F0F0")
lbl_time.pack(pady=10)

# Функция для обновления времени
def update_time():
    current_time = strftime("%H:%M:%S %p")
    lbl_time.configure(text=current_time)
    lbl_time.after(1000, update_time)

update_time()

root.mainloop()
