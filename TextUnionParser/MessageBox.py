import tkinter as tk
from tkinter import messagebox


class MessageBox:
    @staticmethod
    def show_warning(message):
        """Показать предупреждение."""
        root = tk.Tk()
        root.withdraw()  # Скрыть главное окно
        messagebox.showwarning("Предупреждение", message)
        root.destroy()  # Закрыть окно после отображения сообщения

    @staticmethod
    def show_info(message):
        """Показать информационное сообщение."""
        root = tk.Tk()
        root.withdraw()  # Скрыть главное окно
        messagebox.showinfo("Информация", message)
        root.destroy()  # Закрыть окно после отображения сообщения

    @staticmethod
    def log(message):
        """Вывод сообщения в консоль."""
        print(message)
