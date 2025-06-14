import os
import tempfile
import json
import unittest
from src.file_worker import JSONFileWorker


class TestJSONFileWorker(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.temp_dir.name, "vacancies.json")
        self.worker = JSONFileWorker(self.filename)

    def test_read_file_empty(self):
        data = self.worker.read_file()
        self.assertEqual(data, [])

    def test_add_to_file(self):
        data = [{"name": "Python Developer", "url": "https://example.com"}]
        self.worker.add_to_file(data)

        with open(self.filename, "r", encoding="utf-8") as f:
            file_data = json.load(f)

        self.assertEqual(file_data, data)

    def test_add_to_file_no_duplicates(self):
        first = [{"name": "Dev", "url": "https://example.com"}]
        second = [{"name": "Dev", "url": "https://example.com"}]

        self.worker.add_to_file(first)
        self.worker.add_to_file(second)

        data = self.worker.read_file()
        self.assertEqual(len(data), 1)

    def test_delete_from_file(self):
        data = [
            {"name": "Dev1", "url": "https://example.com/1"},
            {"name": "Dev2", "url": "https://example.com/2"}
        ]
        self.worker.add_to_file(data)
        self.worker.delete_from_file({"name": "Dev1"})

        result = self.worker.read_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Dev2")