import tkinter as tk
from tkinter import ttk

# Цвета для приложения
APP_BACKGROUND_COLOR = "#f0f0f0"

DEFAULT_BUTTON_COLOR = "#ff8200"
TEXT_BUTTON_COLOR = "white"

INACTIVE_BUTTON_COLOR = "#D3D3D3"  # Серый для неактивных кнопок
HOVER_BUTTON_COLOR = "#d99d5d"  # Цвет кнопки при наведении

TABLE_BACKGROUND_COLOR = "#ffffff"
COLUMN_HEADER_BACKGROUND_COLOR = "#ff0000"  # Цвет фона заголовков
COLUMN_HEADER_TEXT_COLOR = "#ff8200"  # Цвет текста заголовков
TABLE_TEXT_COLOR = "#000000"  # Цвет текста в таблице
TABLE_ROW_ALTERNATE_COLOR = "#f5f5f5"  # Цвет для чередующихся строк

# Словарь для отслеживания состояния сортировки каждого столбца
sort_order = {}

def sort_treeview(tree, column):
    """
    Функция для сортировки таблицы по указанному столбцу.
    :param tree: Treeview - сам виджет таблицы
    :param column: индекс столбца для сортировки
    """
    # Получаем текущее состояние сортировки для данного столбца
    reverse = sort_order.get(column, False)

    # Получаем все элементы и сортируем их
    items = [(tree.set(item, column), item) for item in tree.get_children("")]
    items.sort(key=lambda x: x[0], reverse=reverse)

    # Вставляем отсортированные элементы в таблицу
    for index, item in enumerate(items):
        tree.move(item[1], '', index)

    # Меняем порядок сортировки для следующего клика
    sort_order[column] = not reverse

    # Обновляем стрелки в заголовках
    for col in tree["columns"]:
        if col == column:
            # Если столбец выбран, показываем стрелку для сортировки
            if reverse:
                tree.heading(col, text=col + " ↓")  # Стрелка вниз для убывания
            else:
                tree.heading(col, text=col + " ↑")  # Стрелка вверх для возрастания
        else:
            tree.heading(col, text=col)  # Убираем стрелки с других заголовков

    # Перерисовываем строки с чередующимися цветами
    update_row_colors(tree, items)


def update_row_colors(tree, items):
    """
    Перерисовывает строки с чередующимися цветами.
    :param tree: сам виджет таблицы
    :param items: отсортированные элементы
    """
    for index, (value, item) in enumerate(items):
        row_tag = 'evenrow' if index % 2 == 0 else 'oddrow'  # чередование цветов строк
        tree.item(item, tags=(row_tag,))


def create_sorted_table(frame, columns, data):
    """
    Создание и отображение таблицы с возможностью сортировки.
    
    :param frame: родительский виджет, в котором будет отображаться таблица
    :param columns: список названий столбцов
    :param data: список данных, которые нужно отобразить в таблице
    :return: возвращает созданный Treeview
    """
    # Создаем контейнер для таблицы и полосы прокрутки
    tree_frame = tk.Frame(frame)
    tree_frame.pack(fill="both", expand=True)

    # Создаем таблицу
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    tree.pack(side="left", fill="both", expand=True)

    # Создание стилей для таблицы и заголовков
    style = ttk.Style()

    # Применение стиля для заголовков
    style.configure("Treeview.Heading",
                    background=COLUMN_HEADER_BACKGROUND_COLOR, 
                    foreground=COLUMN_HEADER_TEXT_COLOR,
                    font=("Arial", 12, "bold"))

    # Применение стиля для самой таблицы
    style.configure("Treeview",
                    background=TABLE_BACKGROUND_COLOR,
                    foreground=TABLE_TEXT_COLOR,
                    rowheight=30)

    # Применение стиля для чередующихся строк
    style.configure("Treeview.Item",
                    background=TABLE_BACKGROUND_COLOR,  # основной фон таблицы
                    foreground=TABLE_TEXT_COLOR)  # основной цвет текста

    tree.tag_configure('evenrow', background=TABLE_ROW_ALTERNATE_COLOR)  # Цвет для четных строк
    tree.tag_configure('oddrow', background=TABLE_BACKGROUND_COLOR)  # Цвет для нечетных строк

    # Настроим заголовки и привяжем их к функции сортировки
    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: sort_treeview(tree, c))
        tree.column(col, width=150, anchor="center")

    # Создаем полосу прокрутки
    scrollbar = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")

    # Привязываем полосу прокрутки к таблице
    tree.config(yscrollcommand=scrollbar.set)

    # Добавляем данные в таблицу
    for index, row in enumerate(data):
        row_tag = 'evenrow' if index % 2 == 0 else 'oddrow'  # чередование цветов строк
        tree.insert("", "end", values=row, tags=(row_tag,))

    return tree
