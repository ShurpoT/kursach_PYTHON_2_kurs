from PIL import Image, ImageTk
from db import fetch_most_popular_group_repertoire  # Импорт метода запроса
import tkinter as tk

def show_most_popular_group_repertoire(frame, connection):
    """
    Отображение самой популярной группы с рейтингом в виде звездочек.
    """
    # Получаем данные о самой популярной группе
    group_info = fetch_most_popular_group_repertoire(connection)

    if not group_info:
        message = tk.Label(frame, text="Нет данных о самой популярной группе.", font=("Arial", 14), fg="red")
        message.pack(pady=20)
        return

    group_name, rating = group_info

    # Создаем контейнер для карточки
    card_frame = tk.Frame(frame, bg="#f0f0f0", bd=5, relief="groove")
    card_frame.pack(pady=20, padx=20, fill="x")

    # Название группы
    group_name_label = tk.Label(card_frame, text=group_name, font=("Arial", 18, "bold"), fg="#333")
    group_name_label.pack(pady=10)

    # Рейтинг (звездочки)
    rating_label = tk.Label(card_frame, text="Рейтинг: ", font=("Arial", 14), fg="#333")
    rating_label.pack(anchor="w", padx=10)

    # Отображаем звездочки на основе рейтинга
    stars_frame = tk.Frame(card_frame, bg="#f0f0f0")
    stars_frame.pack(pady=10)

    # Загрузка изображения звезды
    star_image = Image.open("music_manager_project/star.png")
    star_image = star_image.resize((100, 100))  # Фиксированный размер 30x30 пикселей
    star_image_tk = ImageTk.PhotoImage(star_image)

    # Отображение звездочек
    for i in range(5):  # Максимум 5 звезд
        if i < rating:  # Заполненные звезды
            star_label = tk.Label(stars_frame, image=star_image_tk)
            star_label.image = star_image_tk  # Сохраняем ссылку на изображение
            star_label.pack(side="left", padx=2)
        else:  # Пустые звезды
            star_label = tk.Label(stars_frame, image=star_image_tk)
            star_label.image = star_image_tk  # Ссылка на пустую звезду
            star_label.pack(side="left", padx=2)

    # Текст для подсказки
    rating_text_label = tk.Label(card_frame, text=f"Рейтинг группы: {rating}/5", font=("Arial", 14), fg="#555")
    rating_text_label.pack(pady=10)
