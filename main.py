from typing import Iterator
from itertools import chain
from classes import HH, SJ
from utils import *


def get_menu() -> str:
    print("Выберите дальнейшее действие:")
    print("1. вывести 5 вакансий с самой высокой оплатой")
    print("2. вывести 5 случайных вакансий")
    print("3. вывести вакансии с зарплатой выше заданной")
    print("4. записать результаты в файл")
    print("5. повторить поиск")
    print("6. выход")
    return input(">>> ")


def print_vacance(vacancies: Iterator) -> None:
    for each in vacancies:
        print(each["title"])
        print(" ", each["salary"])
        print(" ", each["desc"])
        print(" ", each["link"])


def change_menu_item(vacancies: Iterator, count: int):
    while True:
        user_input = get_menu()  # выбор пункта меню
        if user_input != "4":
            vacancies = get_data_of_file()
        if user_input == "1":  # топ 5 зп
            vacancies = get_sort(vacancies)
            vacancies = get_limit(vacancies, 5)
        elif user_input == "2":  # 5 случайных
            vacancies = get_random(vacancies, count)
        elif user_input == "3":  # зп > указанной
            vacancies = get_more(vacancies, int(input("зп >= ")))

        elif user_input == "4":  # записать результат в файл
            count_vac = set_rezult_of_file(vacancies)
            print(f'в файл записано {count_vac} вакансий')

        elif user_input == "5":  # повтор поиска
            break
        elif user_input == "6":  # выход
            exit()
        else:
            print("нет такого пункта")
        if user_input != "4":
            print_vacance(vacancies)


def main():
    print("Добро пожаловать! Какие вакансии будем искать?")
    while True:
        keyword = input("введите ключевое слово: ")
        print('идёт поиск подходящих вакансий ...')
        vacancies = None
        for site in (HH(keyword), SJ(keyword)):  # перебор по двум сайтам
            for page in range(20):
                if vacancies:
                    vacancies = chain(vacancies, site.get_request(page))  # добавляем вакансии в генератор
                else:
                    vacancies = site.get_request(page)  # создаём генератор, если его нет

        count = set_data_of_file(vacancies)  # запись найденных вакансий в файл
        print(f"найдено {count} подходящих вакансий")

        change_menu_item(vacancies, count)  # обработка меню


if __name__ == '__main__':
    main()
