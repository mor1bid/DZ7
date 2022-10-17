print('Здравствуйте! \n')
print('a Просмотреть справочник. \n')
print('b Добавить данные. \n')
print('c Импортировать данные. \n')
print('d Экспортировать данные. \n')
print('e Поиск данных. \n')
print('f Удаление данных. \n')
print('g Завершение работы. \n')
prog = 0
ram = 0
enu = 0
while prog == 0:
    work = input('Введите символ желаемого пункта меню: ')
    if work == 'a':
        with open('DZFORM1.txt', 'r+') as form1:
            ram = 0
            print('Ваш справочник: \n')
            for line in form1:
                print(line.rstrip('\n'))
    elif work == 'b':
        with open('DZFORM1.txt', 'a+') as form1:
            enu += 1
            word = 4
            print('Введите фамилию, имя, телефон и описание (отдельно):')
            form1.writelines(str(enu))
            form1.writelines('. ')
            form1.writelines('\n')
            while word > 0:
                text = input()
                form1.writelines(text)
                form1.writelines('\n')
                word -= 1
    elif work == 'g':
        prog += 1
    else:
        print('Ошибка!')
