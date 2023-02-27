import write_data as wd1
import read_alldata as r_alld
import delete_data as dd
import searche_data as sd
import edit_data as ed
def ask_user():

    choise = input('(w(Запись)/r(Показать все записи)/d(Удалить запись)/s(Поиск по слову)/s+(Поиск по дате)/e(Редактирование)):')
    if choise == 'w':
        r_alld.find_data()
        wd1.get()        
    elif choise == 'r':
        r_alld.find_data()       
    elif choise == 'd':
        dd.delete_data()
    elif choise == 's':
        sd.word_search()
    elif choise == 's+':    
        sd.data_search()
    elif choise == 'e':
        ed.ed_data()
    else:
        print('Неизвестная команда')

