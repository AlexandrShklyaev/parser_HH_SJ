from itertools import chain
from classes import HH, SJ
from utils import *


def get_menu():
    print("Выберите дальнейшее действие:")
    print("1. вывести 5 вакансий с самой высокой оплатой")
    print("2. вывести 5 случайных вакансий")
    print("3. вывести вакансии с зарплатой выше заданной")
    print("4. повторить поиск")
    print("5. выход")
    return input(">>> ")


def main():
    print("Добро пожаловать! Какие вакансии будем искать?")
    while True:
        keyword = input("введите ключевое слово: ")
        print('идёт поиск подходящих вакансий ...')
        vacancies = None
        for site in (HH(keyword), SJ(keyword)):
            for page in range(2):
                if vacancies:
                    vacancies = chain(vacancies, site.get_request(page))
                else:
                    vacancies = site.get_request(page)
        count = set_data_of_file(vacancies)
        print(f"найдено {count} подходящих вакансий")
        vacancies = get_data_of_file()
        while True:
            user_input = get_menu()
            if user_input == "5":
                exit()
            if user_input == "4":
                break
            if user_input == "1":
                vacancies = get_sort(vacancies)
                vacancies = get_limit(vacancies, 5)
            if user_input == "2":
                vacancies = get_random(vacancies, count)
            if user_input == "3":
                vacancies = get_more(vacancies, int(input("зп >= ")))

            for each in vacancies:
                print(each)


if __name__ == '__main__':
    main()
