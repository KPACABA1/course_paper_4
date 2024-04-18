import json
from abc import ABC, abstractmethod


class AddVacanciesInJSONAbstract(ABC):
    """Абстрактный класс для добавления вакансий в JSON"""
    @staticmethod
    @abstractmethod
    def add_json(vacancies):
        pass


class AddVacanciesInJSON(AddVacanciesInJSONAbstract):
    @staticmethod
    def add_json(vacancies):
        with open('vacancies.json', mode='w') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)
