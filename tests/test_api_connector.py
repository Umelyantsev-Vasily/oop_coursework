import unittest
from unittest.mock import patch, Mock
import requests
from src.api_connector import HeadHunterAPI
import pytest

class TestHeadHunterAPI(unittest.TestCase):

    def setUp(self):
        self.api = HeadHunterAPI(per_page=2)

    @patch('requests.get')
    def test_connect_to_api_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = self.api.connect_to_api()
        self.assertTrue(result)

    @patch('requests.get')
    def test_connect_to_api_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        result = self.api.connect_to_api()
        self.assertFalse(result)

    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [
                {"name": "Python Developer", "alternate_url": "https://example.com/1"},
                {"name": "Junior Python", "alternate_url": "https://example.com/2"}
            ]
        }
        mock_get.return_value = mock_response

        vacancies = self.api.get_vacancies("Python")
        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Python Developer")

    @patch('src.api_connector.HeadHunterAPI.connect_to_api')  # ✅ Правильный путь!
    @patch('requests.get')
    def test_get_vacancies_api_error(self, mock_get, mock_connect):
        mock_connect.return_value = True  # connect_to_api возвращает True
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        vacancies = self.api.get_vacancies("Python")
        self.assertEqual(vacancies, [])
