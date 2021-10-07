import unittest
import sys
from io import StringIO
import main as student_solution
import solution as author_solution

student = student_solution
author = author_solution

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout



class TrainTestCase(unittest.TestCase):
    def setUp(self):
        with Capturing() as capt:
            student_func = student.main()
        with Capturing() as capt:
            author_func = author.main()
        self.student_structure = student_func.get('structure')
        self.author_structure = author_func.get('structure')
        self.student_rows_numbers = student_func.get('number_of_rows')
        self.author_rows_numbers = author_func.get('number_of_rows')
        self.student_result = student_func.get('query_result')
        self.author_result = author_func.get('query_result')
        self.student_keywords = student_func.get('keywords')
        self.author_keywords = author_func.get('keywords')

    def test_query_structure_has_like_operator(self):
        self.assertIn('like', self.student_keywords,
                     ('Проверьте, что воспользовались оператором like'
                      ' при поиске фильмов'))

    def test_operator_like_has_correct_value(self):
        conditions = self.student_structure.get('условие')
        self.assertTrue("'%train%'" in conditions or '"%train%"' in conditions,
                     ('Проверьте, что правильно указали слово для поиска после оператора LIKE '
                      'в условии запроса'))

    def test_operator_where_has_correct_column(self):
        conditions = self.student_structure.get('доп условие')
        self.assertIn("type='movie'", conditions,
                     ('Проверьте, что выбираете именно фильмы а не фильмы и сериалы'))

    def test_query_has_correct_column(self):
        student_column = self.student_structure.get('колонка')
        author_column = self.author_structure.get('колонка')
        self.assertEqual(student_column, author_column,
            ('Проверьте, что правильно указали колонку в запросе.'
             f'Вы указали {student_column}, тогда как должна быть указана: {author_column}'))

    def test_rows_count_superfluous_condition(self):
        self.assertFalse(self.student_rows_numbers > self.author_rows_numbers,
            ('В запросе имеется лишнее условие.'
             f'Выводится больше строк ({self.student_rows_numbers}) чем предполагалось {self.author_rows_numbers}'))

    def test_rows_count_lack_condition(self):
        self.assertFalse(self.student_rows_numbers < self.author_rows_numbers,
            ('В запросе не хватает условия.'
             f'Выводится меньше строк ({self.student_rows_numbers}) чем предполагалось {self.author_rows_numbers}'))


if __name__ == "__main__":
    unittest.main()