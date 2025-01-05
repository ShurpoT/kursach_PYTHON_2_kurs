
-- Создание базы данных
CREATE DATABASE music_manager;

-- Выбор базы данных
USE music_manager;

-- Создание таблицы Group
CREATE TABLE Group_ (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    creation_year YEAR NOT NULL,
    country VARCHAR(255) NOT NULL,
    rating INT DEFAULT 0
);

-- Создание таблицы Song
CREATE TABLE Song (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    composer VARCHAR(255),
    lyricist VARCHAR(255),
    creation_year YEAR NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Group_(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Создание таблицы Tour
CREATE TABLE Tour (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Group_(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Добавление индексов для улучшения производительности
CREATE INDEX idx_song_group_id ON Song(group_id);
CREATE INDEX idx_tour_group_id ON Tour(group_id);

-- Добавление данных для тестирования
INSERT INTO Group_ (name, creation_year, country, rating)
VALUES 
    ('The Beatles', 1960, 'UK', 5),
    ('Pink Floyd', 1965, 'UK', 5),
    ('ABBA', 1972, 'Sweden', 4),
    ('The Rolling Stones', 1962, 'UK', 5),
    ('Led Zeppelin', 1968, 'UK', 5),
    ('Queen', 1970, 'UK', 5);

INSERT INTO Song (title, composer, lyricist, creation_year, group_id)
VALUES
    ('Hey Jude', 'Paul McCartney', 'John Lennon', 1968, 1),
    ('Let It Be', 'Paul McCartney', 'John Lennon', 1970, 1),
    ('Another Brick in the Wall', 'Roger Waters', 'Roger Waters', 1979, 2),
    ('Comfortably Numb', 'Roger Waters', 'Roger Waters', 1979, 2),
    ('Dancing Queen', 'Benny Andersson', 'Björn Ulvaeus', 1976, 3),
    ('Mamma Mia', 'Benny Andersson', 'Björn Ulvaeus', 1975, 3),
    ('Satisfaction', 'Mick Jagger', 'Mick Jagger', 1965, 4),
    ('Paint It Black', 'Mick Jagger', 'Mick Jagger', 1966, 4),
    ('Stairway to Heaven', 'Jimmy Page', 'Robert Plant', 1971, 5),
    ('Whole Lotta Love', 'Jimmy Page', 'Robert Plant', 1969, 5),
    ('Bohemian Rhapsody', 'Freddie Mercury', 'Freddie Mercury', 1975, 6),
    ('We Are the Champions', 'Freddie Mercury', 'Freddie Mercury', 1977, 6),
    ('My Generation', 'Pete Townshend', 'Pete Townshend', 1965, 1),
    ('Pinball Wizard', 'Pete Townshend', 'Pete Townshend', 1969, 1),
    ('Back In Black', 'Angus Young', 'Brian Johnson', 1980, 2),
    ('Highway to Hell', 'Angus Young', 'Bon Scott', 1979, 2),
    ('Light My Fire', 'Jim Morrison', 'Jim Morrison', 1967, 3),
    ('Riders on the Storm', 'Jim Morrison', 'Jim Morrison', 1971, 3),
    ('Enter Sandman', 'James Hetfield', 'James Hetfield', 1991, 4),
    ('The Unforgiven', 'James Hetfield', 'James Hetfield', 1991, 4),
    ('Smells Like Teen Spirit', 'Kurt Cobain', 'Kurt Cobain', 1991, 5),
    ('Come as You Are', 'Kurt Cobain', 'Kurt Cobain', 1991, 5),
    ('Under the Bridge', 'Flea', 'Anthony Kiedis', 1992, 6),
    ('Give It Away', 'Flea', 'Anthony Kiedis', 1991, 6),
    ('Fix You', 'Chris Martin', 'Chris Martin', 2005, 1),
    ('Viva La Vida', 'Chris Martin', 'Chris Martin', 2008, 1),
    ('With or Without You', 'Bono', 'Bono', 1987, 2),
    ('I Still Haven’t Found What I’m Looking For', 'Bono', 'Bono', 1987, 2),
    ('Just Like Heaven', 'Robert Smith', 'Robert Smith', 1987, 2),
    ('Lullaby', 'Robert Smith', 'Robert Smith', 1992, 2),
    ('Creep', 'Thom Yorke', 'Thom Yorke', 1992, 2),
    ('Karma Police', 'Thom Yorke', 'Thom Yorke', 1997, 3),
    ('Wonderwall', 'Noel Gallagher', 'Noel Gallagher', 1995, 3),
    ('Don’t Look Back in Anger', 'Noel Gallagher', 'Noel Gallagher', 1996, 3),
    ('Learn to Fly', 'Dave Grohl', 'Dave Grohl', 1999, 1),
    ('The Pretender', 'Dave Grohl', 'Dave Grohl', 2007, 1),
    ('Boulevard of Broken Dreams', 'Billie Joe Armstrong', 'Billie Joe Armstrong', 2004, 1),
    ('American Idiot', 'Billie Joe Armstrong', 'Billie Joe Armstrong', 2004, 5),
    ('Holiday', 'Billie Joe Armstrong', 'Billie Joe Armstrong', 2005, 5),
    ('American Idiot', 'Billie Joe Armstrong', 'Billie Joe Armstrong', 2004, 4);
INSERT INTO Tour (city, start_date, end_date, group_id)
VALUES
    ('London', '1965-05-10', '1965-05-20', 1),
    ('New York', '1979-07-01', '1979-07-15', 2),
    ('Stockholm', '1980-03-01', '1980-03-05', 3),
    ('San Francisco', '1992-10-01', '1992-10-10', 1),
    ('Seattle', '1991-04-01', '1991-04-15', 1),
    ('Barcelona', '2001-03-01', '2001-03-10', 3),
    ('Milan', '2003-09-01', '2003-09-10', 2),
    ('Los Angeles', '2008-06-01', '2008-06-10', 2),
    ('Manchester', '2000-11-01', '2000-11-10', 5),
    ('London', '2010-06-01', '2010-06-10', 5),
    ('New York', '2006-09-01', '2006-09-10', 5);
