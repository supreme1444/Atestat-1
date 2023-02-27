def ed_data():
    word_old = input(str('Введите старое слово '))
    word_new = input(str('Введите новое слово ')) 
    with open("data.csv", 'r+',encoding='utf-8') as f:
        text = ''.join([line.replace(word_old, word_new) for line in f.readlines()])
        f.seek(0)
        f.write(text)
    print('Данные отредактированы')
