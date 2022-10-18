print('Здравствуйте! \n')
print('(a) Просмотреть справочник. \n')
print('(b) Добавить данные. \n')
print('(c) Импортировать данные. \n')
print('(d) Экспортировать данные. \n')
print('(e) Поиск данных. \n')
print('(f) Удаление данных. \n')
print('(g) Завершение работы.')
prog = 0
ram = 0
while prog == 0:
    work = input('\nВведите символ желаемого пункта меню: ')
    if work == 'a':
        with open('DZFORM1.txt', 'r+') as form1:
            ram = 0
            print('Ваш справочник: \n')
            for line in form1:
                print(line.rstrip('\n'))
    elif work == 'b':
        form = input('Выберите желаемый формат (список/строка) 1/2: ')
        with open('DZFORM1.txt', 'a+') as form1:
            if form == '1':
                print('Введите фамилию, имя, телефон и описание:')
                form1.writelines(' \n')
                text = input().split(' ')
                for i in text:
                    if i.isdigit() == False:
                        form1.writelines('\n')
                    form1.writelines(i)
            elif form == '2':
                print('Введите фамилию, имя, телефон и описание:')
                form1.writelines(' \n')
                text = input().split(' ')
                for i in text:
                    form1.writelines(i)
                    if i.isdigit() == False or i != len(text) - 1:
                        form1.writelines(',')
    elif work == 'c':
        path = input('Введите адрес желаемого файла и/или его название: \n')
        choi = input('Хотите перевести содержимое файла в формат списка/строки/ или нет? 1/2/n: ')
        with open('DZFORM1.txt', 'a+') as form1:
            with open(path, 'r') as impex:
                if choi == '1':
                    form1.writelines(' \n')
                    text = impex.readlines()
                    text = str(text).split(',')
                        # if line == ',':
                        #     line = '\n'
                        #     form1.writelines(line)
                    for i in text:
                        if i.isdigit() == False:
                            form1.writelines('\n')
                        form1.writelines(i)
                    form1.writelines(' \n')
                    print('\nГотово!')
                elif choi == '2':
                    for line in impex:
                        form1.writelines(' \n')
                        text = impex.readlines()
                        text = str(text).split('\n')
                        # if line == '\n':
                        #     line = ','
                        for i in text:
                            if i.isdigit() == False and len(i) > 3:
                                form1.writelines(',')
                            elif len(i) <= 3:
                                form1.writelines('\n')
                            form1.writelines(i)
                    form1.writelines(' \n')
                    print('\nГотово!')
                elif choi == 'n':
                    form1.writelines(' \n')
                    text = impex.readlines()
                    form1.writelines(text)
                    form1.writelines(' \n')
                    print('\nГотово!')
    elif work == 'd':
        i = 0
        path = input('Введите адрес желаемого файла и/или его название: \n')
        with open('DZFORM1.txt', 'r') as form1:
            with open(path, 'a') as expex:
                text = form1.readlines()
                expex.writelines(text)
                expex.writelines(' \n')
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
    elif work == 'e':
        path = input('\nВведите адрес желаемого файла и/или его название: \n')
        cont = input('Введите фамилию желаемого контакта: \n')
        with open(path, 'r') as lookex:
            text = lookex.readlines()
            call = 0
            lookex.seek(0)
            for line in text:
                if cont not in line and call == 0:
                    call == 0
                else:
                    print('\n')
                    call = 1
                if line != ' \n' and call == 1:
                    print(line)
                else:
                    call = 0
            print('\nГотово!')
    elif work == 'f':
        i = 0
        while i == 0:
            answ = input('\nТочно хотите удалить свои данные? y/n: ')
            if answ == 'y':
                path = input('Введите адрес желаемого файла и/или его название (если файл лежит в директории программы): \n')
                choi = input('Удалить все данные либо удалить выборочно? 1/2: ')
                if choi == '1':
                    with open(path, 'w') as delex:
                        delex.seek(0)
                        delex.truncate()
                        i += 1
                        print('\nГотово!')
                elif choi == '2':
                    cont = input('Введите фамилию и имя желаемого контакта: \n')
                    with open(path, 'r') as delread:
                        text = delread.readlines()
                        with open(path, 'w') as delex:
                            call = 0
                            delex.seek(0)
                            for line in text:
                                if cont not in line and call == 0:
                                    delex.write(line)
                                else:
                                    call = 1
                                if line != ' \n' and call == 1:
                                    delex.write('')
                                else:
                                    call = 0
                            i += 1
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
