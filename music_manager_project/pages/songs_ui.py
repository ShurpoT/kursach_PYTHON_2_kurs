

import tkinter as tk
from tkinter import ttk, messagebox

from utils import create_sorted_table  # Импортируем функцию создания таблицы
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR

def display_songs_tab(frame, connection):
    for widget in frame.winfo_children():
        widget.destroy()

    cursor = connection.cursor()
    cursor.execute(
        "SELECT Song.title, Song.composer, Song.lyricist, Song.creation_year, Group_.name "
        "FROM Song JOIN Group_ ON Song.group_id = Group_.id"
    )
    songs = cursor.fetchall()

    # Создаем таблицу с помощью функции create_sorted_table
    tree = create_sorted_table(
        frame,
        columns=("Название", "Композитор", "Автор текста", "Год создания", "Группа"),
        # headings=("Название", "Композитор", "Автор текста", "Год создания", "Группа"),
        data=songs,
    )

    # Кнопка добавления песни
    def add_song():
        add_window = tk.Toplevel()
        add_window.title("Добавление песни")
        add_window.geometry("300x400+800+200")  # Размеры и положение окна

        label_title = tk.Label(add_window, text="Название песни:")
        label_title.pack(pady=5)

        entry_title = tk.Entry(add_window)
        entry_title.pack(pady=5)

        label_composer = tk.Label(add_window, text="Композитор:")
        label_composer.pack(pady=5)

        entry_composer = tk.Entry(add_window)
        entry_composer.pack(pady=5)

        label_lyricist = tk.Label(add_window, text="Автор текста:")
        label_lyricist.pack(pady=5)

        entry_lyricist = tk.Entry(add_window)
        entry_lyricist.pack(pady=5)

        label_creation_year = tk.Label(add_window, text="Год создания:")
        label_creation_year.pack(pady=5)

        entry_creation_year = tk.Entry(add_window)
        entry_creation_year.pack(pady=5)

        label_group = tk.Label(add_window, text="Выберите группу:")
        label_group.pack(pady=5)

        group_menu = ttk.Combobox(add_window, width=30)
        group_menu.pack(pady=5)

        cursor.execute("SELECT id, name FROM Group_")
        groups = cursor.fetchall()
        group_menu['values'] = [group[1] for group in groups]
        group_menu.set(groups[0][1])  # Установить первую группу как выбранную

        def save_song():
            title = entry_title.get()
            composer = entry_composer.get()
            lyricist = entry_lyricist.get()
            creation_year = entry_creation_year.get()
            group_name = group_menu.get()

            group_id = next(group[0] for group in groups if group[1] == group_name)

            if title and composer and lyricist and creation_year and group_id:
                cursor.execute(
                    "INSERT INTO Song (title, composer, lyricist, creation_year, group_id) VALUES (%s, %s, %s, %s, %s)",
                    (title, composer, lyricist, creation_year, group_id)
                )
                connection.commit()
                messagebox.showinfo("Успех", "Песня добавлена!")
                add_window.destroy()
                display_songs_tab(frame, connection)
            else:
                messagebox.showwarning("Ошибка", "Заполните все поля!")

        button_save = tk.Button(add_window, text="Сохранить", command=save_song)
        button_save.pack(pady=10)

    button_add_song = tk.Button(
        frame, text="Добавить песню", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=add_song
    )
    button_add_song.pack(pady=10)

    # Кнопка удаления песни
    def delete_song():
        selected_item = tree.selection()
        if selected_item:
            selected_values = tree.item(selected_item, "values")
            title = selected_values[0]  # Получаем название песни
            cursor.execute("DELETE FROM Song WHERE title = %s", (title,))
            connection.commit()
            messagebox.showinfo("Успех", "Песня удалена!")
            display_songs_tab(frame, connection)
        else:
            messagebox.showwarning("Ошибка", "Выберите песню для удаления!")

    button_delete_song = tk.Button(
        frame, text="Удалить песню", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=delete_song
    )
    button_delete_song.pack(pady=10)
