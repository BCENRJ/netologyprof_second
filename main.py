from pprint import pprint
import csv
from my_tools.my_tools import cook_data, my_pattern

# Читаем адресную книгу в формате CSV в список contacts_list
with open(file="phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

all_column_names = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
cooked_list = cook_data(contacts_list, my_pattern)
cooked_list.insert(0, all_column_names)

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open(file="phonebook.csv", mode="w") as f:
    data_writer = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    data_writer.writerows(cooked_list)


if __name__ == '__main__':
    print('Loaded | Please Check "phonebook.csv" File ☺️')
