import json
import random


def set_data_of_file(data):
    """ записывает данные о вакансиях в файл vacances.json"""
    count = 0
    with open("vacances.json", "w", encoding="utf-8") as file:
        for each in data:
            json.dump(each, file, ensure_ascii=False)
            file.write("\n")
            count += 1
    return count
def set_rezult_of_file(data):
    """ записывает результат в файл rezult.txt"""
    count = 0
    with open("rezult.txt", "w", encoding="utf-8") as file:
        for each in data:
            line="\n".join([each["title"], str(each["salary"]), each["desc"], each["link"]])
            file.write(line)
            file.write("\n")
            file.write("-"*50)
            file.write("\n")
            count += 1
    return count


def get_data_of_file():
    """ считывает данные о вакансиях в файл """
    with open("vacances.json", "r", encoding="utf-8") as file:
        for x in file.readlines():
            yield json.loads(x.strip())


def get_sort(list_lines, key: str = "salary") -> list:
    return sorted(list_lines, key=lambda x: x[key], reverse=True)


def get_limit(list_lines, limit: int) -> list:
    return list_lines[:max(limit, 0)]

def get_random(list_lines, limit: int) -> list:
    num=-1
    list_num=[]
    for _ in range(5):
        num = random.randint(num+1,limit-1)
        list_num.append(num)
    num = 0
    for each in list_lines:
        if num in list_num:
            yield each
        num +=1
def get_more(list_lines, limit: int) -> list:
    for each in list_lines:
        if int(each["salary"])>=limit:
            yield each

