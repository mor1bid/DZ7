i = 0
with open('DZFORM1.txt', 'a+') as form1:
    while i == 0:
        for line in form1:
            print(line.rstrip('\n'))
        answ = input('\nДобавить новые данные? y/n: ')
        if answ == 'y':
            word = 4
            print('Введите Фамилию, Имя, Телефон и Описание:')
            while word > 0:
                text = input()
                form1.writelines(text)
                form1.writelines('\n')
                word -= 1
        elif answ == 'n':
            i += 1
        elif answ != 'n':
            print('Ошибка!')
        # answ = input('Ещё? y/n: ')
        # if answ == 'n':
        #     i += 1
        # elif answ == 'y':
        #     form1.writelines('\n')
        # else:
        #     print('Ошибка!')
