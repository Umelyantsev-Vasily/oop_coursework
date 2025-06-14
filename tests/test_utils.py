import unittest
from src.utils import convert_to_vacancy_objects, filter_vacancies, sort_vacancies
from src.vacancy import Vacancy


class TestUtilsFunctions(unittest.TestCase):

    def test_convert_to_vacancy_objects(self):
        raw_data = [{
            "name": "Python Developer",
            "alternate_url": "https://example.com",
            "salary": {"from": 100000},
            "snippet": {"requirement": "Умение писать код"}
        }]
        vacancies = convert_to_vacancy_objects(raw_data)
        self.assertIsInstance(vacancies[0], Vacancy)

    def test_filter_vacancies_by_min_salary(self):
        v1 = Vacancy("A", "https://a.com",  80000, 100000, "")
        v2 = Vacancy("B", "https://b.com",  120000, 150000, "")
        filtered = filter_vacancies([v1, v2], salary_min=100000)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "B")

    def test_sort_vacancies_descending(self):
        v1 = Vacancy("A", "https://a.com",  80000, 100000, "")
        v2 = Vacancy("B", "https://b.com",  120000, 150000, "")
        sorted_list = sort_vacancies([v1, v2])
        self.assertEqual(sorted_list[0].salary_from, 120000)