import tkinter as tk
from db import fetch_song_details_by_title  # Добавляем импорт метода для запроса
from utils import create_sorted_table  # Убедитесь, что эта функция работает корректно для таблиц
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR  

def show_song_details_by_title(frame, connection):
    """
    Отображение деталей песни по названию.
    """
    # Создаем контейнер для поля ввода и кнопки
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=10, padx=20)  # Пакуем в верхнюю часть окна

    # Ввод названия песни
    label = tk.Label(search_frame, text="Введите название песни:", font=("Arial", 14))
    label.pack(side="left", padx=(0, 10))  # Метка слева от поля ввода

    song_title_entry = tk.Entry(search_frame, font=("Arial", 12))
    song_title_entry.pack(side="left", fill="x", expand=True)  # Поле ввода

    # Кнопка поиска
    search_button = tk.Button(search_frame, text="Поиск", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 12), command=lambda: on_search(song_title_entry))
    search_button.pack(side="left", padx=(10, 0))  # Кнопка поиска справа

    # Создаем контейнер для результатов поиска
    result_frame = tk.Frame(frame)
    result_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def on_search(song_title_entry):
        # Удаляем старые результаты поиска и таблицу
        for widget in result_frame.winfo_children():
            widget.destroy()

        song_title = song_title_entry.get()
        if song_title:
            # Получаем данные о песне по названию
            data = fetch_song_details_by_title(connection, song_title)
            
            if not data:
                message = tk.Label(result_frame, text="Нет данных для выбранной песни.", font=("Arial", 14), fg="red")
                message.pack(pady=20)
                return

            # Создаем таблицу с результатами
            columns = ("Автор текста", "Композитор", "Год создания", "Группа")
            create_sorted_table(result_frame, columns, data)
        else:
            message = tk.Label(result_frame, text="Пожалуйста, введите название песни.", font=("Arial", 14), fg="red")
            message.pack(pady=20)
