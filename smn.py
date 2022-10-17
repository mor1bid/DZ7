print('Здравствуйте! \n')
print('a Просмотреть справочник. \n')
print('b Добавить данные. \n')
print('c Импортировать данные. \n')
print('d Экспортировать данные. \n')
print('e Поиск данных. \n')
print('f Удаление данных. \n')
print('g Завершение работы.')
prog = 0
ram = 0
# enu = 0
while prog == 0:
    work = input('\nВведите символ желаемого пункта меню: ')
    if work == 'a':
        with open('DZFORM1.txt', 'r+') as form1:
            ram = 0
            print('Ваш справочник: \n')
            for line in form1:
                print(line.rstrip('\n'))
    elif work == 'b':
        form = input('Выберите желаемый формат (список/строка) 1/2:')
        with open('DZFORM1.txt', 'a+') as form1:
            if form == '1':
                # enu += 1
                word = 4
                print('Введите фамилию, имя, телефон и описание (через Enter):')
                # form1.writelines(str(enu))
                # form1.writelines('. ')
                # form1.writelines('\n')
                while word > 0:
                    text = input()
                    form1.writelines(text)
                    form1.writelines('\n')
                    word -= 1
            elif form == '2':
                print('Введите фамилию, имя, телефон и описание (через Spacebar):')
                text = input().split(',')
                form1.writelines(text)
                form1.writelines('\n')
    elif work == 'c':
        path = input('Введите адрес желаемого файла и/или его название: \n')
        with open('DZFORM1.txt', 'a+') as form1:
            with open(path, 'r') as impex:
                text = impex.readlines()
                form1.writelines(text)
                form1.writelines('\n')
    elif work == 'd':
        i = 0
        path = input('Введите адрес желаемого файла и/или его название: \n')
        with open('DZFORM1.txt', 'r') as form1:
            with open(path, 'a') as expex:
                text = form1.readlines()
                expex.writelines(text)
                expex.writelines('\n')
                print('\nГотово!')
                while i == 0 :
                    answ = input('Вывести данные заданного файла? y/n: ')
                    if answ == 'y':
                        with open(path, 'r') as expex:
                            for line in expex:
                                print(line.rstrip('\n'))
                            i += 1
                    elif answ == 'n':
                        i += 1
                    else:
                        print('Ошибка!')
    elif work == 'f':
        i = 0
        while i == 0:
            answ = input('Точно хотите удалить свои данные? y/n: ')
            if answ == 'y':
                path = input('Введите адрес желаемого файла и/или его название (если файл лежит в директории программы): \n')
                choi = input('Удалить все данные либо удалить выборочно? 1/2: ')
                if choi == '1':
                    with open(path, 'w') as delex:
                        delex.seek(0)
                        delex.truncate()
                        i += 1
                        # for line in delex:
                        #     line.rstrip('\n')
                        print('\nГотово!')
                elif choi == '2':
                    cont = input('Введите фамилию желаемого контакта: \n')
                    with open(path, 'r') as delread:
                        with open(path, 'w') as delex:
                            for line in delread:
                                if not line.strip('\n').startswith(cont):
                                    delex.write(line)
                            print('\nГотово!')
                    
                else:
                    print('Ошибка!')
            elif answ == 'n':
                i += 1
            else:
                print('Ошибка!')

    elif work == 'g':
        prog += 1
    else:
        print('Ошибка!')
