import requests
from typing import List, Dict
from src.abstract_classes import AbstractVacancyAPI


class HeadHunterAPI(AbstractVacancyAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self, per_page: int = 100):
        self._base_url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "VacancyAnalyzer/1.0"}
        self._params = {"per_page": per_page, "text": "", "area": 1}  # Москва

    def connect_to_api(self) -> bool:
        """Приватный метод проверки подключения к API"""
        try:
            response = requests.get(self._base_url, headers=self._headers, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def get_vacancies(self, search_query: str) -> List[Dict]:
        """Получение вакансий по поисковому запросу"""
        if not self.connect_to_api():
            raise ConnectionError("Не удалось подключиться к API hh.ru")

        self._params["text"] = search_query
        try:
            response = requests.get(self._base_url, headers=self._headers, params=self._params)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.RequestException as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []
