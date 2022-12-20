# Сколько сезонов
# Чтобы узнать, насколько продуктивно работает режиссер
# Alastair Fothergill, мы решили посчитать,
# сколько сезонов сериалов он всего снял.
#
# Пример результата:
#
# Длительность всех сериалов режиссера Alastair Fothergill составляет x сезона.
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
    SELECT title, COUNT(title)
    FROM netflix
    WHERE director LIKE '%Alastair Fothergill%'  
    AND "type" = 'TV Show'
    """
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    tv_show_count = result[0][1]
    result = (f'Длительность всех сериалов режиссера Alastair Fothergill составляет {tv_show_count} сезона.')

if __name__ == '__main__':
    print(result)
