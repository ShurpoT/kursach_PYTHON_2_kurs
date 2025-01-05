
import tkinter as tk
from tkinter import  messagebox

from utils import create_sorted_table  # Импортируйте вашу функцию из файла, где она находится
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR


def display_groups_tab(frame, connection):
    for widget in frame.winfo_children():
        widget.destroy()

    cursor = connection.cursor()
    cursor.execute("SELECT name, creation_year, country, rating FROM Group_")
    groups = cursor.fetchall()

    columns = ["Название", "Год основания", "Страна", "Рейтинг"]

    # Создаем таблицу с помощью вашей функции
    tree = create_sorted_table(frame, columns, groups)

    # Кнопка добавления группы
    def add_group():
        add_window = tk.Toplevel()
        add_window.title("Добавление группы")
        add_window.geometry("300x400+800+200")  # Размеры и положение окна

        label_name = tk.Label(add_window, text="Название группы:")
        label_name.pack(pady=5)

        entry_name = tk.Entry(add_window)
        entry_name.pack(pady=5)

        label_creation_year = tk.Label(add_window, text="Год основания:")
        label_creation_year.pack(pady=5)

        entry_creation_year = tk.Entry(add_window)
        entry_creation_year.pack(pady=5)

        label_country = tk.Label(add_window, text="Страна:")
        label_country.pack(pady=5)

        entry_country = tk.Entry(add_window)
        entry_country.pack(pady=5)

        label_rating = tk.Label(add_window, text="Рейтинг:")
        label_rating.pack(pady=5)

        entry_rating = tk.Entry(add_window)
        entry_rating.pack(pady=5)

        def save_group():
            name = entry_name.get()
            creation_year = entry_creation_year.get()
            country = entry_country.get()
            rating = entry_rating.get()

            if name and creation_year and country and rating:
                cursor.execute(
                    "INSERT INTO Group_ (name, creation_year, country, rating) VALUES (%s, %s, %s, %s)",
                    (name, creation_year, country, rating)
                )
                connection.commit()
                messagebox.showinfo("Успех", "Группа добавлена!")
                add_window.destroy()
                display_groups_tab(frame, connection)
            else:
                messagebox.showwarning("Ошибка", "Заполните все поля!")

        button_save = tk.Button(add_window, text="Сохранить", command=save_group)
        button_save.pack(pady=10)

    button_add_group = tk.Button(frame, text="Добавить группу", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=add_group)
    button_add_group.pack(pady=10)

    # Кнопка удаления группы
    def delete_group():
        selected_item = tree.selection()
        if selected_item:
            selected_values = tree.item(selected_item, "values")
            group_name = selected_values[0]  # Учитываем, что ID больше нет, опираемся на уникальные значения
            cursor.execute("DELETE FROM Group_ WHERE name = %s", (group_name,))
            connection.commit()
            messagebox.showinfo("Успех", "Группа удалена!")
            display_groups_tab(frame, connection)
        else:
            messagebox.showwarning("Ошибка", "Выберите группу для удаления!")

    button_delete_group = tk.Button(frame, text="Удалить группу", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=delete_group)
    button_delete_group.pack(pady=10)
