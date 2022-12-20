# Болливуд
#
# Индийские фильмы одно время были очень популярны.
# Давайте проверим, как это отразилось на Нетфликсе!
# Нам нужно посчитать, сколько индийских фильмов и сериалов есть на платформе.
# Также считаются фильмы и сериалы которые были сняты совместно с Индией
#
# Пример результата:
#
# фильмы: 50 шт
# сериалы: 10 шт
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

with sqlite3.connect("../netflix.db") as con:
    cur = con.cursor()
    sqlite_query = """
    SELECT COUNT(duration)
    FROM netflix
    WHERE release_year = 2010  
    AND "type" = 'Movie'
    """
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    minutes = result[0][0]
    hours = minutes//60
    result = (f'Чтобы посмотреть все фильмы, нам нужно {hours} часов.')

if __name__ == '__main__':
    print(result)
