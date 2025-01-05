import tkinter as tk
from tkinter import ttk
from db import fetch_tour_details_by_group_name  # Импорт метода запроса
from utils import create_sorted_table  # Убедитесь, что эта функция работает корректно для таблиц
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR  

def show_tour_details_by_group_name(frame, connection):
    """
    Отображение информации о турах для выбранной группы.
    """
    # Создаем контейнер для поля ввода и кнопки
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=10, padx=20)  # Пакуем в верхнюю часть окна

    # Ввод названия группы
    label = tk.Label(search_frame, text="Введите название группы:", font=("Arial", 14))
    label.pack(side="left", padx=(0, 10))  # Метка слева от поля ввода

    group_name_entry = tk.Entry(search_frame, font=("Arial", 12))
    group_name_entry.pack(side="left", fill="x", expand=True)  # Поле ввода

    # Кнопка поиска
    search_button = tk.Button(search_frame, text="Поиск", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 12), command=lambda: on_search(group_name_entry))
    search_button.pack(side="left", padx=(10, 0))  # Кнопка поиска справа

    # Создаем контейнер для результатов поиска
    result_frame = tk.Frame(frame)
    result_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def on_search(group_name_entry):
        # Удаляем старые результаты поиска и таблицу
        for widget in result_frame.winfo_children():
            widget.destroy()

        group_name = group_name_entry.get().strip()
        if group_name:
            # Получаем данные о турах для этой группы
            tours_info = fetch_tour_details_by_group_name(connection, group_name)
            
            if not tours_info:
                message = tk.Label(result_frame, text="Нет данных о турах для данной группы.", font=("Arial", 14), fg="red")
                message.pack(pady=20)
                return

            # Создаем таблицу с результатами
            columns = ("ID", "Город", "Дата начала", "Дата окончания")
            create_sorted_table(result_frame, columns, tours_info)
        else:
            message = tk.Label(result_frame, text="Пожалуйста, введите название группы.", font=("Arial", 14), fg="red")
            message.pack(pady=20)
