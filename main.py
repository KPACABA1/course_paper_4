from pprint import pprint

from src.getting_and_working_with_vacancies import HHAPI
from src.add_vacancies_in_json import AddVacanciesInJSON


profession = input("Введите профессию для поиска ")
quantity_profession = int(input("Какое количество вакансий с наибольшей зарплатой вы хотите увидеть?"))

hh_url = HHAPI("https://api.hh.ru/vacancies")
vacancies = hh_url.get_info(profession)
vacancies_sorted = sorted(vacancies, reverse=True)



AddVacanciesInJSON.add_json(vacancies)



pprint(vacancies_sorted[:quantity_profession])
