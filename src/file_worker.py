import json
import os
from typing import List, Dict
from src.abstract_classes import AbstractFileWorker


class JSONFileWorker(AbstractFileWorker):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = 'vacancies.json'):
        # Путь к папке data
        self._data_dir = 'data'
        # Полный путь к файлу
        self._filename = os.path.join(self._data_dir, filename)

        # Создаем папку data, если она не существует
        if not os.path.exists(self._data_dir):
            os.makedirs(self._data_dir)

        # Создаем файл, если он не существует
        if not os.path.exists(self._filename):
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def read_file(self) -> List[Dict]:
        """Чтение данных из файла"""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Убедиться, что это список и каждый элемент - словарь
                if isinstance(data, list):
                    return data
                else:
                    return []
        except (json.JSONDecodeError, FileNotFoundError):
            # Если файл поврежден или не существует, возвращаем пустой список
            return []

    def add_to_file(self, data: List[Dict]) -> None:
        """Добавление данных в файл без дублирования"""
        existing_data = self.read_file()
        existing_urls = {item['url'] for item in existing_data}

        new_data = [item for item in data if item['url'] not in existing_urls]

        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data + new_data, f, ensure_ascii=False, indent=2)

    def delete_from_file(self, condition: Dict) -> None:
        """Удаление данных из файла по условию"""
        data = self.read_file()
        filtered_data = [item for item in data if not all(
            item.get(key) == value for key, value in condition.items()
        )]

        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=2)