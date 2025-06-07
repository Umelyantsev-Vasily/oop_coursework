from typing import List, Dict
from src.vacancy import Vacancy


def convert_to_vacancy_objects(data: List[Dict]) -> List[Vacancy]:
    """Конвертация данных API в объекты Vacancy"""
    vacancies = []
    for item in data:
        salary = item.get("salary")
        salary_from = salary.get("from") if salary else None
        salary_to = salary.get("to") if salary else None

        vacancy = Vacancy(
            title=item.get("name", ""),
            url=item.get("alternate_url", ""),
            salary_from=salary_from,
            salary_to=salary_to,
            description=item.get("snippet", {}).get("requirement", ""),
        )
        vacancies.append(vacancy)
    return vacancies


def filter_vacancies(vacancies: List[Vacancy], salary_min: int = 0) -> List[Vacancy]:
    """Фильтрация вакансий по минимальной зарплате"""
    return [v for v in vacancies if v._salary_from >= salary_min]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (по убыванию)"""
    return sorted(vacancies, reverse=True, key=lambda v: v._salary_from)
