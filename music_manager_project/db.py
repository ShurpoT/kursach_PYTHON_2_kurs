import mysql.connector


def get_connection():
    return mysql.connector.connect( 
        host="localhost",  # Адрес вашего MySQL сервера
        user="root",       # Пользователь базы данных
        password="root",   # Пароль базы данных
        database="music_manager"  # Имя базы данных
    )


# запросы
def fetch_groups_info(connection):
    """
    Получение информации о группах.
    """
    query = "SELECT name, creation_year, country, rating FROM `Group_`"  # Убираем `id` из запроса
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def fetch_songs_info(connection):
    """
    Запрос к базе данных для получения информации о песнях.
    Возвращает список песен с данными: название, группа, жанр, длительность, год.
    """
    query = """
    SELECT s.title, g.name AS group_name, s.composer, s.lyricist, s.creation_year
    FROM Song s
    JOIN Group_ g ON s.group_id = g.id
    """
    cursor = connection.cursor()
    cursor.execute(query)
    songs = cursor.fetchall()  # Получаем все результаты запроса
    cursor.close()
    
    return songs  # Возвращаем список песен



def fetch_tours_info(connection):
    """
    Получение информации о гастролях.
    """
    query = """
        SELECT t.city, t.start_date, t.end_date, g.name AS group_name
        FROM Tour t
        JOIN Group_ g ON t.group_id = g.id
        ORDER BY t.start_date
    """
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result



def fetch_songs_on_tours(connection, group_name):
    """
    Получение песен, которые исполнялись группой на гастролях.
    :param connection: подключение к базе данных
    :param group_name: название группы для фильтрации
    :return: список песен
    """
    query = """
        SELECT s.title, t.city, t.start_date, t.end_date
        FROM Song s
        JOIN Group_ g ON s.group_id = g.id
        JOIN Tour t ON g.id = t.group_id
        WHERE g.name = %s
        ORDER BY t.start_date
    """
    cursor = connection.cursor()
    cursor.execute(query, (group_name,))
    result = cursor.fetchall()
    cursor.close()
    return result



def fetch_groups_by_composer(connection, composer_name):
    """
    Получение информации о группах, связанных с композитором.
    :param connection: соединение с базой данных
    :param composer_name: имя композитора
    :return: результат запроса
    """
    query = """
        SELECT g.name, g.creation_year, g.country, g.rating
        FROM `Group_` g
        JOIN Song s ON g.id = s.group_id
        WHERE s.composer LIKE %s
    """
    cursor = connection.cursor()
    cursor.execute(query, ('%' + composer_name + '%',))  # Используем LIKE для поиска по части имени
    result = cursor.fetchall()
    cursor.close()
    return result


def fetch_song_details_by_title(connection, song_title):
    """
    Получение информации о песне по названию.
    :param connection: соединение с базой данных
    :param song_title: название песни
    :return: результат запроса
    """
    query = """
        SELECT s.lyricist, s.composer, s.creation_year, g.name AS group_name
        FROM Song s
        JOIN `Group_` g ON s.group_id = g.id
        WHERE s.title LIKE %s
    """
    cursor = connection.cursor()
    cursor.execute(query, ('%' + song_title + '%',))  # Используем LIKE для поиска по части названия
    result = cursor.fetchall()
    cursor.close()
    return result




def fetch_most_popular_group_repertoire(connection):
    """
    Получение самой популярной группы с ее рейтингом.
    :param connection: соединение с базой данных
    :return: название группы и ее рейтинг
    """
    query = """
        SELECT name, rating
        FROM `Group_`
        ORDER BY rating DESC
        LIMIT 1
    """
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result



def fetch_tour_details_by_group_name(connection, group_name):
    """
    Получение информации о турах для заданной группы.
    """
    query = """
        SELECT t.id, t.city, t.start_date, t.end_date
        FROM Tour t
        JOIN Group_ g ON t.group_id = g.id
        WHERE g.name = %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (group_name,))
    result = cursor.fetchall()
    cursor.close()
    return result



def fetch_songs_by_lyricist(connection, lyricist_name):
    """
    Получение песен по лирическому писателю.
    """
    query = """
        SELECT s.id, s.title, s.composer, s.creation_year, g.name AS group_name
        FROM Song s
        JOIN Group_ g ON s.group_id = g.id
        WHERE s.lyricist LIKE %s
    """
    cursor = connection.cursor()
    cursor.execute(query, ('%' + lyricist_name + '%',))  # Используем LIKE для поиска по частичному совпадению
    result = cursor.fetchall()
    cursor.close()
    return result
