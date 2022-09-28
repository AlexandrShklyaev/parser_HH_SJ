import json
from itertools import chain

from classes import HH, SJ


def set_data_of_file(data):
    """ записывает данные о вакансиях в файл """
    count = 0
    with open("vacances.json", "w", encoding="utf-8") as file:
        for each in data:
            json.dump(each, file, ensure_ascii=False)
            file.write("\n")
            count += 1
    return count


def get_data_of_file():
    """ считывает данные о вакансиях в файл """
    with open("vacances.json", "r", encoding="utf-8") as file:
        for x in file.readlines():
            yield json.loads(x.strip())


def get_sort(list_lines, key: str = "salary", is_reverse: bool = False) -> list:
    return sorted(list_lines, key=lambda x: x[key], reverse=is_reverse)


def get_limit(list_lines, limit: int) -> list:
    return list_lines[:max(limit, 0)]
