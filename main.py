from src.api_connector import HeadHunterAPI
from src.file_worker import JSONFileWorker
from src.utils import convert_to_vacancy_objects, filter_vacancies, sort_vacancies


def user_interaction():
    """Функция взаимодействия с пользователем"""
    print("Добро пожаловать в анализатор вакансий!")

    # Получение вакансий
    search_query = input("Введите поисковый запрос (например: Python разработчик): ")
    hh_api = HeadHunterAPI()
    raw_vacancies = hh_api.get_vacancies(search_query)

    if not raw_vacancies:
        print("По вашему запросу вакансий не найдено.")
        return

    # Конвертация и обработка
    vacancies = convert_to_vacancy_objects(raw_vacancies)
    salary_min = int(input("Введите минимальную зарплату (0 если не важно): ") or 0)
    filtered_vacancies = filter_vacancies(vacancies, salary_min)
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Сохранение в файл
    file_worker = JSONFileWorker()
    file_worker.add_to_file(raw_vacancies)

    # Вывод результатов
    print(f"\nНайдено {len(sorted_vacancies)} вакансий:")
    for i, vacancy in enumerate(sorted_vacancies[:10], 1):
        print(f"\n{i}. {vacancy}")

    print("\nДанные сохранены в файл vacancies.json")


if __name__ == "__main__":
    user_interaction()
