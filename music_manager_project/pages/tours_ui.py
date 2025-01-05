
import tkinter as tk
from tkinter import ttk, messagebox
from utils import create_sorted_table  # Импортируем функцию для создания сортируемой таблицы
from utils import DEFAULT_BUTTON_COLOR  
from utils import TEXT_BUTTON_COLOR

# Функция для отображения вкладки Гастроли
def display_tours_tab(frame, connection):
    for widget in frame.winfo_children():
        widget.destroy()

    cursor = connection.cursor()
    cursor.execute("SELECT Tour.id, Tour.city, Tour.start_date, Tour.end_date, Group_.name FROM Tour JOIN Group_ ON Tour.group_id = Group_.id")
    tours = cursor.fetchall()

    # Создаем таблицу с помощью функции create_sorted_table
    tree = create_sorted_table(
        frame,
        columns=("Город", "Дата начала", "Дата окончания", "Группа"),
        data=tours,
    )

    # Кнопка добавления гастролей
    def add_tour():
        add_window = tk.Toplevel()
        add_window.title("Добавление гастролей")
        add_window.geometry("300x400+800+200")  # Размеры и положение окна

        label_city = tk.Label(add_window, text="Город:")
        label_city.pack(pady=5)

        entry_city = tk.Entry(add_window)
        entry_city.pack(pady=5)

        label_start_date = tk.Label(add_window, text="Дата начала:")
        label_start_date.pack(pady=5)

        entry_start_date = tk.Entry(add_window)
        entry_start_date.pack(pady=5)

        label_end_date = tk.Label(add_window, text="Дата окончания:")
        label_end_date.pack(pady=5)

        entry_end_date = tk.Entry(add_window)
        entry_end_date.pack(pady=5)

        label_group = tk.Label(add_window, text="Выберите группу:")
        label_group.pack(pady=5)

        group_menu = ttk.Combobox(add_window, width=30)
        group_menu.pack(pady=5)

        cursor.execute("SELECT id, name FROM Group_")
        groups = cursor.fetchall()
        group_menu['values'] = [group[1] for group in groups]
        group_menu.set(groups[0][1])

        def save_tour():
            city = entry_city.get()
            start_date = entry_start_date.get()
            end_date = entry_end_date.get()
            group_name = group_menu.get()

            group_id = next(group[0] for group in groups if group[1] == group_name)

            if city and start_date and end_date and group_id:
                cursor.execute(
                    "INSERT INTO Tour (city, start_date, end_date, group_id) VALUES (%s, %s, %s, %s)",
                    (city, start_date, end_date, group_id)
                )
                connection.commit()
                messagebox.showinfo("Успех", "Гастроли добавлены!")
                add_window.destroy()
                display_tours_tab(frame, connection)
            else:
                messagebox.showwarning("Ошибка", "Заполните все поля!")

        button_save = tk.Button(add_window, text="Сохранить", command=save_tour)
        button_save.pack(pady=10)

    button_add_tour = tk.Button(frame, text="Добавить гастроли", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=add_tour)
    button_add_tour.pack(pady=10)

    # Кнопка удаления гастролей
    def delete_tour():
        selected_item = tree.selection()
        if selected_item:
            tour_id = tree.item(selected_item, "values")[0]
            cursor.execute("DELETE FROM Tour WHERE id = %s", (tour_id,))
            connection.commit()
            messagebox.showinfo("Успех", "Гастроли удалены!")
            display_tours_tab(frame, connection)
        else:
            messagebox.showwarning("Ошибка", "Выберите гастроли для удаления!")

    button_delete_tour = tk.Button(frame, text="Удалить гастроли", bg=DEFAULT_BUTTON_COLOR, fg=TEXT_BUTTON_COLOR, font=("Arial", 14), command=delete_tour)
    button_delete_tour.pack(pady=10)
