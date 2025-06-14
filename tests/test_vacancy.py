import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_valid_vacancy(self):
        vac = Vacancy(
            title="Python Dev",
            url="https://example.com",
            salary_from=100000,
            salary_to=150000,
            description="Описание"
        )
        self.assertEqual(vac._title, "Python Dev")

    def test_invalid_title_raises(self):
        with self.assertRaises(ValueError):
            Vacancy(title=123, url="https://example.com",  salary_from=100000, salary_to=None, description="")

    def test_salary_defaults(self):
        vac = Vacancy(title="Dev", url="https://example.com",  salary_from=None, salary_to=None, description="")
        self.assertEqual(vac._salary_from, 0)
        self.assertEqual(vac._salary_to, 0)

    def test_comparison_operators(self):
        v1 = Vacancy("A", "https://example.com/1",  80000, 100000, "")
        v2 = Vacancy("B", "https://example.com/2",  90000, 120000, "")

        self.assertTrue(v1 < v2)
        self.assertTrue(v2 > v1)

    def test_str_representation(self):
        vac = Vacancy("Dev", "https://example.com",  80000, 100000, "Описание разработчика на Python")
        expected = (
            "Вакансия: Dev\n"
            "Зарплата: 80000-100000\n"
            "Описание: Описание разработчика на Python...\n"  # ← Полное слово "Python"
            "Ссылка: https://example.com"
        )
        self.assertEqual(str(vac), expected)