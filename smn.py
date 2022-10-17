print('Здравствуйте!', end=' ')
prog = 0
ram = 0
enu = 0
while prog == 0:
    work = input('Хотите просмотреть справочник? y/n: ')
    if work == 'y':
        with open('DZFORM1.txt', 'r+') as form1:
            ram = 0
            print('Ваш справочник: \n')
            for line in form1:
                print(line.rstrip('\n'))
    elif work == 'n':
        prog += 1
    else:
        print('Ошибка!')
    while ram == 0:
        answ = input('\nДобавить новые данные? y/n: ')
        with open('DZFORM1.txt', 'r+') as form1:
            if answ == 'y':
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
            elif answ == 'n':
                ram += 1
            elif answ != 'n':
                print('Ошибка!')
        # answ = input('Ещё? y/n: ')
        # if answ == 'n':
        #     ram += 1
        # elif answ == 'y':
        #     form1.writelines('\n')
        # else:
        #     print('Ошибка!')
