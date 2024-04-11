import requests
from abc import ABC, abstractmethod


class HHAPIAbstract(ABC):
    """Абстрактный класс для получения API с сайта"""
    @abstractmethod
    def __init__(self, url):
        self.url = url
    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения API с сайта и преобразования его в json-объекта"""
        pass


class HHAPI(HHAPIAbstract):
    """Класс для получения API с сайта"""
    def __init__(self, url):
        super().__init__(url)

    def get_info(self):
        """Метод для получения API с сайта и преобразования его в json-объекта"""
        response = requests.get(self.url)
        return response.json()

