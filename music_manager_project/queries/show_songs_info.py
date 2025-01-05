import tkinter as tk
from utils import create_sorted_table  # Функция для создания и отображения таблицы
from db import fetch_songs_info  # Метод запроса данных о песнях из базы данных

def show_songs_info(frame, connection):
    """
    Отображение информации о песнях.
    Эта функция будет запрашивать данные о песнях из базы данных и отображать их в виде таблицы.
    """
    # Убираем все предыдущие виджеты (чтобы не было старых данных)
    for widget in frame.winfo_children():
        widget.destroy()

    # Запрос данных о песнях из базы данных
    data = fetch_songs_info(connection)

    # Проверяем, есть ли данные
    if not data:
        # Если нет данных, показываем сообщение
        message = tk.Label(frame, text="Данные о песнях не найдены.", font=("Arial", 14), fg="red")
        message.pack(pady=20)
        return

    # Указываем столбцы для таблицы
    columns = ("Название", "Группа", "Жанр", "Длительность", "Год")
    
    # Создаем таблицу с данными
    create_sorted_table(frame, columns, data)
