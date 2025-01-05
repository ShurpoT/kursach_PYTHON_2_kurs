import tkinter as tk
from db import fetch_songs_by_lyricist  # Импорт метода запроса
from utils import create_sorted_table  # Убедитесь, что эта функция работает корректно для таблиц
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR  

def show_songs_by_lyricist(frame, connection):
    """
    Отображение песен по автору текста.
    """
    # Создаем контейнер для поля ввода и кнопки
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=10, padx=20)  # Пакуем в верхнюю часть окна

    # Ввод имени лирического писателя
    label = tk.Label(search_frame, text="Введите имя лирического писателя:", font=("Arial", 14))
    label.pack(side="left", padx=(0, 10))  # Метка слева от поля ввода

    lyricist_name_entry = tk.Entry(search_frame, font=("Arial", 12))
    lyricist_name_entry.pack(side="left", fill="x", expand=True)  # Поле ввода

    # Кнопка поиска
    search_button = tk.Button(search_frame, text="Поиск", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 12), command=lambda: on_search(lyricist_name_entry))
    search_button.pack(side="left", padx=(10, 0))  # Кнопка поиска справа

    # Создаем контейнер для результатов поиска
    result_frame = tk.Frame(frame)
    result_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def on_search(lyricist_name_entry):
        # Удаляем старые результаты поиска и таблицу
        for widget in result_frame.winfo_children():
            widget.destroy()

        lyricist_name = lyricist_name_entry.get().strip()
        if lyricist_name:
            # Получаем данные о песнях по имени лирического писателя
            songs_info = fetch_songs_by_lyricist(connection, lyricist_name)
            
            if not songs_info:
                message = tk.Label(result_frame, text="Нет данных для выбранного лирического писателя.", font=("Arial", 14), fg="red")
                message.pack(pady=20)
                return

            # Создаем таблицу с результатами
            columns = ("ID", "Название песни", "Композитор", "Год создания", "Группа")
            create_sorted_table(result_frame, columns, songs_info)
        else:
            message = tk.Label(result_frame, text="Пожалуйста, введите имя лирического писателя.", font=("Arial", 14), fg="red")
            message.pack(pady=20)
