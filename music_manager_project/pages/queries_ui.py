import tkinter as tk
from tkinter import ttk

from queries.show_groups_info import show_groups_info
from queries.show_songs_info import show_songs_info
from queries.show_tours_info import show_tours_info
from queries.show_songs_on_tours import show_songs_on_tours
from queries.show_groups_by_composer import show_groups_by_composer
from queries.show_song_details_by_title import show_song_details_by_title
from queries.show_most_popular_group_repertoire import show_most_popular_group_repertoire
from queries.show_tour_details_by_group_name import show_tour_details_by_group_name
from queries.show_songs_by_lyricist import show_songs_by_lyricist

def display_queries_tab(frame, connection):
    for widget in frame.winfo_children():
        widget.destroy()

    query_options = [
        "Сведения о группах",
        "Сведения о песнях",
        "Сведения о гастролях",
        "Какие песни исполнялись на гастролях заданной группы",
        "Какие группы исполняют песни заданного композитора",
        "Автор текста, композитор и дата создания песни с данным названием",
        "Репертуар наиболее популярной группы",
        "Место и продолжительность гастролей группы с заданным названием",
        "Какие песни исполняет заданный певец"
    ]

    query_methods = {
        query_options[0]: lambda: show_groups_info(content_frame, connection),
        query_options[1]: lambda: show_songs_info(content_frame, connection),
        query_options[2]: lambda: show_tours_info(content_frame, connection),
        query_options[3]: lambda: show_songs_on_tours(content_frame, connection),
        query_options[4]: lambda: show_groups_by_composer(content_frame, connection),
        query_options[5]: lambda: show_song_details_by_title(content_frame, connection),
        query_options[6]: lambda: show_most_popular_group_repertoire(content_frame, connection),
        query_options[7]: lambda: show_tour_details_by_group_name(content_frame, connection),
        query_options[8]: lambda: show_songs_by_lyricist(content_frame, connection)
    }

    label_query_type = tk.Label(frame, text="Выберите тип запроса:", font=("Arial", 14))
    label_query_type.pack(pady=10)

    # Стиль для Combobox
    query_menu = ttk.Combobox(frame, values=query_options, width=40, font=("Arial", 12))
    query_menu.pack(pady=10)

    # Устанавливаем начальный элемент (первый)
    query_menu.set(query_options[0])

    # Настроим стиль для комбобокса без selectbackground
    style = ttk.Style()
    style.configure("TCombobox",
                    foreground="black",  # Цвет текста
                    background="white",  # Цвет фона
                    fieldbackground="white",  # Фон поля
                    selectcolor="black",  # Цвет текста при выборе
                    padding=5)

    content_frame = tk.Frame(frame, relief=tk.GROOVE, borderwidth=2)
    content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

    def on_query_change(event):
        selected_query = query_menu.get()
        for widget in content_frame.winfo_children():
            widget.destroy()
        if selected_query in query_methods:
            query_methods[selected_query]()
    
    # Привязка обработчика к изменению значения комбобокса
    query_menu.bind("<<ComboboxSelected>>", on_query_change)

    # Вызов обработки для первого выбранного элемента
    on_query_change(None)
