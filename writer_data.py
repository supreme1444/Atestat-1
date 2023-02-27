import csv
from datetime import datetime
table = dict(заголовок  = ' ' , тело  = ' ')

def get():
    data_log = datetime.today().strftime('%Y-%m-%d %H:%M')
    txt = input("Введите следующий номер записи ")
    f = open('data.csv', 'a', encoding='utf8')
    f.write(str(txt)+")" + " python notes.py add --title"+' , '+str(data_log) + ' , ')
        
