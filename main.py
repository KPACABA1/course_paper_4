from src.getting_and_working_with_vacancies import HHAPI


hh_url = HHAPI("https://api.hh.ru/vacancies?text=python")
print(hh_url.get_info("python"))