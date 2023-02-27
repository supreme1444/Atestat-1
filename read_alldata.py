def find_data():
    fp = open('data.csv', 'r',encoding ='utf-8')
    while True:
        line =  fp.readline()
        if not line:
            break
        
        print(line)
