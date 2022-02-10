import re

# Pattern for 'lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'
my_pattern = r'(^[а-яёА-ЯЁ]+)([^а-яёА-ЯЁ]{1,2})([а-яёА-ЯЁ]+)([^а-яёА-ЯЁ]{1,2})([а-яёА-ЯЁ]+)?([^а-яёА-ЯЁ\w]+)([' \
          r'а-яёА-ЯЁ]+)?([^а-яёА-ЯЁ\w\+]+)([а-яёА-ЯЁc– ]{50,})?(.?(8|\+7|7|\()([\- \(]{0,2})?(\d{3})([\)\- ]{0,' \
          r'2})(\d{3})([\- ]{0,1})(\d{2})([\- ]{0,1})(\d{2})([^а-яёА-ЯЁ\w\+]+))?([Ддоб. -]{4,6}(\d{4}))?([^0-9\w]?([' \
          r'a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]+[a-zA-Z0-9]+[\.]+[\w]{2,4}))?'


# Function to re.match all necessary data and checking repeated once
def cook_data(data_list, pattern):
    """ 1: "data_list" stands for list of csv data and
        2: "pattern" for the way to search """
    my_dict = {}
    for row_index in range(1, len(data_list)):
        row_txt = ' '.join(map(str, data_list[row_index]))
        result = re.match(pattern, row_txt)
        if result is not None:
            g = result.group
            if g(10) is not None:
                if g(22) is not None:
                    new_row = {(g(1), g(3)): {'surname': g(5), 'org': g(7), 'pos': g(9),
                                              'phone': f'+7({g(13)}){g(15)}-{g(17)}-{g(19)} доб.{g(22)}',
                                              'email': g(24)}}
                else:
                    new_row = {(g(1), g(3)): {'surname': g(5), 'org': g(7), 'pos': g(9),
                                              'phone': f'+7({g(13)}){g(15)}-{g(17)}-{g(19)}', 'email': g(24)}}
            else:
                new_row = {(g(1), g(3)): {'surname': g(5), 'org': g(7), 'pos': g(9), 'phone': g(10), 'email': g(24)}}
            c_key = list(new_row.keys())[0]
            if c_key not in my_dict:
                my_dict.update(new_row)
            elif c_key in my_dict:
                details = ('surname', 'org', 'pos', 'phone', 'email')
                for elem in details:
                    if my_dict[c_key][elem] is None:
                        my_dict[c_key][elem] = list(new_row.values())[0][elem]

    return lucky_sort(my_dict)


# Listing/Sorting gathered data and preparing it to export into csv file
def lucky_sort(my_data):
    return [[k[0], k[1], v['surname'], v['org'], v['pos'], v['phone'], v['email']] for k, v in my_data.items()]
