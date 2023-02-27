import io
def word_search():
    word = input("Введите слово для поиска ")
    with io.open('data.csv', encoding='utf-8') as file:
        for line in file:
            if word in line:
                print(line, end='')    
def data_search():
    data1 = input("Введите год полностью ")
    data2 = input("Введите месяц ")
    data3 = input("Введите день ")
    alldata = (data1 + '-' + data2 + '-' + data3)
    with io.open('data.csv', encoding='utf-8') as file:
        for line in file:
            if alldata in line:
                print(line, end='')
    print('Данные найденны')   
