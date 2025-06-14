from abc import ABCMeta
from src.abstract_classes import AbstractVacancyAPI, AbstractFileWorker

def test_abstract_vacancy_api_methods():
    assert 'connect_to_api' in dir(AbstractVacancyAPI)
    assert 'get_vacancies' in dir(AbstractVacancyAPI)

def test_abstract_file_worker_methods():
    assert 'read_file' in dir(AbstractFileWorker)
    assert 'add_to_file' in dir(AbstractFileWorker)
    assert 'delete_from_file' in dir(AbstractFileWorker)