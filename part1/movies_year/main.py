# #Все года
# Вам нужно выбрать все фильмы, которые были сняты между 1943 и 1945 годами.
# Выведите их названия и год производства в виде списка.

# Пример результата:
# +--------------------------------+--------------+
# |             title              | release_year |
# +--------------------------------+--------------+
# |    Know Your Enemy - Japan     |     1945     |
# |    Nazi Concentration Camps    |     1945     |
# |           San Pietro           |     1945     |
# +--------------------------------+--------------+
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
import prettytable

with sqlite3.connect("../netflix.db") as con:
    cur = con.cursor()
    sqlite_query = """
    SELECT title, release_year
    FROM netflix
    WHERE release_year > 1942 
    AND release_year < 1946
    AND release_year IS NOT NULL
    """
    result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
