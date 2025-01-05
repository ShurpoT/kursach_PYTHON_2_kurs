import tkinter as tk
from utils import create_sorted_table
from db import fetch_groups_info  # Подключаем метод для получения данных

def show_groups_info(frame, connection):
    """
    Отображение информации о группах.
    """
    # Удаляем все старые виджеты
    for widget in frame.winfo_children():
        widget.destroy()

    # Получаем данные о группах
    data = fetch_groups_info(connection)

    # Если данных нет, показываем сообщение
    if not data:
        message = tk.Label(frame, text="Данные о группах не найдены.", font=("Arial", 14), fg="red")
        message.pack(pady=20)
        return  # Останавливаем выполнение, если данных нет

    # Задаем столбцы
    columns = ("Группа", "Год создания", "Страна", "Рейтинг")

    # Создаем и отображаем таблицу с сортировкой
    create_sorted_table(frame, columns, data)
