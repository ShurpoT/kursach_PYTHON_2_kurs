import tkinter as tk
from db import get_connection
from pages.groups_ui import display_groups_tab
from pages.songs_ui import display_songs_tab
from pages.tours_ui import display_tours_tab
from pages.queries_ui import display_queries_tab
from utils import APP_BACKGROUND_COLOR  
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR  
from utils import INACTIVE_BUTTON_COLOR  
from utils import HOVER_BUTTON_COLOR  

# Главная функция для запуска программы
def main():
    connection = get_connection()

    # Создаем главное окно приложения
    root = tk.Tk()
    root.title("Менеджер музыки")
    root.geometry("1200x600+350+200")  # Размеры и положение окна
    

    # Устанавливаем фоновый цвет для всего приложения
    root.configure(bg=APP_BACKGROUND_COLOR)

    frame = tk.Frame(root, bg=APP_BACKGROUND_COLOR)  # Устанавливаем цвет фона для фрейма
    frame.pack(fill=tk.BOTH, expand=True)

    # Меню навигации
    header_frame = tk.Frame(root, bg=APP_BACKGROUND_COLOR)  # Устанавливаем цвет фона для хедера
    header_frame.pack(fill=tk.X)

    # Функция для изменения цвета кнопки при наведении
    def on_enter(button):
        if button["bg"] != DEFAULT_BUTTON_COLOR:  # Не изменять активную кнопку
            button.config(bg=HOVER_BUTTON_COLOR)

    def on_leave(button):
        if button["bg"] != DEFAULT_BUTTON_COLOR:  # Не изменять активную кнопку
            button.config(bg=INACTIVE_BUTTON_COLOR)

    # Кнопки для перехода по вкладкам
    buttons = [
        ("Группы", lambda: display_groups_tab(frame, connection)),
        ("Песни", lambda: display_songs_tab(frame, connection)),
        ("Гастроли", lambda: display_tours_tab(frame, connection)),
        ("Запросы", lambda: display_queries_tab(frame, connection))
    ]

    # Создаем кнопки с нужным стилем
    button_objects = []
    for text, command in buttons:
        button = tk.Button(header_frame, text=text, bg=INACTIVE_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("JetBrains Mono", 16),
                           command=lambda text=text: change_tab(text))  # Используем lambda для вызова change_tab
        # При наведении на кнопку
        button.bind("<Enter>", lambda event, btn=button: on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: on_leave(btn))
        
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button_objects.append(button)

    # Функция для активации выбранной кнопки
    def activate_button(selected_button):
        for button in button_objects:
            if button == selected_button:
                button.config(bg=DEFAULT_BUTTON_COLOR)
            else:
                button.config(bg=INACTIVE_BUTTON_COLOR)

    # Функция для переключения вкладок
    def change_tab(tab_name):
        for i, (text, command) in enumerate(buttons):
            if text == tab_name:
                activate_button(button_objects[i])  # Активация кнопки
                command()  # Запуск соответствующей функции вкладки

    # Изначально активируем первую кнопку (например, "Группы")
    activate_button(button_objects[0])

    # Запуск первой вкладки (например, "Группы") при запуске
    display_groups_tab(frame, connection)

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == "__main__":
    main()
