from typing import Optional


class Vacancy:
    """Класс для представления вакансии"""

    __slots__ = ("_title", "_url", "_salary_from", "_salary_to", "_description")

    def __init__(self, title: str, url: str, salary_from: Optional[int], salary_to: Optional[int], description: str):
        self._validate_data(title, url, salary_from, salary_to, description)

        self._title = title
        self._url = url
        self._salary_from = salary_from if salary_from is not None else 0
        self._salary_to = salary_to if salary_to is not None else 0
        self._description = description

    def _validate_data(
        self, title: str, url: str, salary_from: Optional[int], salary_to: Optional[int], description: str
    ) -> None:
        """Приватный метод валидации данных"""
        if not isinstance(title, str) or not title:
            raise ValueError("Название вакансии должно быть непустой строкой")
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("URL должен быть валидной ссылкой")
        if salary_from is not None and not isinstance(salary_from, int):
            raise ValueError("Зарплата 'от' должна быть целым числом")
        if salary_to is not None and not isinstance(salary_to, int):
            raise ValueError("Зарплата 'до' должна быть целым числом")

    # ========== Публичные property ==========
    @property
    def title(self) -> str:
        return self._title

    @property
    def url(self) -> str:
        return self._url

    @property
    def salary_from(self) -> int:
        return self._salary_from

    @property
    def salary_to(self) -> int:
        return self._salary_to

    @property
    def description(self) -> str:
        return self._description

    # ========== Методы сравнения ==========
    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по минимальной зарплате"""
        return self._salary_from < other._salary_from

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по максимальной зарплате"""
        return self._salary_to > other._salary_to

    def __str__(self) -> str:
        return (
            f"Вакансия: {self._title}\n"
            f"Зарплата: {self._salary_from}-{self._salary_to}\n"
            f"Описание: {self._description[:100]}...\n"
            f"Ссылка: {self._url}"
        )
