import re
import csv
def delete_data():
    request = input('Введите номер записи со скобкой "5)"')
    

    with open('data.csv',encoding='utf-8') as f:
        lines = f.readlines()

    str = request
    pattern = re.compile(re.escape(str))
    with open('data.csv', 'w',encoding='utf-8') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
