from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractVacancyAPI(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def connect_to_api(self) -> bool:
        """Проверка подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        """Получение вакансий по поисковому запросу"""
        pass


class AbstractFileWorker(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def read_file(self) -> List[Dict]:
        """Чтение данных из файла"""
        pass

    @abstractmethod
    def add_to_file(self, data: List[Dict]) -> None:
        """Добавление данных в файл"""
        pass

    @abstractmethod
    def delete_from_file(self, condition: Dict) -> None:
        """Удаление данных из файла по условию"""
        pass
