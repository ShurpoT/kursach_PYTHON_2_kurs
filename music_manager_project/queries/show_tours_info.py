import tkinter as tk
from utils import create_sorted_table  # Функция для создания таблицы
from db import fetch_tours_info  # Метод запроса данных о турах

def show_tours_info(frame, connection):
    """
    Отображение информации о турах.
    Эта функция будет запрашивать данные о турах из базы данных и отображать их в виде таблицы.
    """
    # Убираем все предыдущие виджеты (чтобы не было старых данных)
    for widget in frame.winfo_children():
        widget.destroy()

    # Запрос данных о турах из базы данных
    data = fetch_tours_info(connection)

    # Проверяем, есть ли данные
    if not data:
        # Если нет данных, показываем сообщение
        message = tk.Label(frame, text="Данные о турах не найдены.", font=("Arial", 14), fg="red")
        message.pack(pady=20)
        return

    # Указываем столбцы для таблицы
    columns = ("Название тура", "Дата начала", "Дата окончания", "Группа")

    # Создаем таблицу с данными
    create_sorted_table(frame, columns, data)
