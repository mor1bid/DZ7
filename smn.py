i = 0
with open('DZFORM1.txt', 'a') as form1:
    print(*form1)
    answ = input('\nДобавить новые данные? y/n: ')
    if answ == 'y':
        while i == 0:
            text = input('Введите Фамилию, Имя, Телефон и Описание:')
            form1.writelines('\ntext')
            answ = input('Ещё? y/n: ')
            if answ == 'n':
                i+=1
            else:
                form1.writelines('\n')
