prog = 0
while prog == 0:
    ask = input('Введите желаемый запрос: \n')
    ask += '+1'
    ask = list(filter(lambda x: ' ' not in x, ask))
    answ = 0
    count = 0
    dig = ''
    for i in range(len(ask)):
        if i == 0:
            dig = ask[i]
        elif ask[i].isdigit():
            dig += ask[i]
            if count == 0:
                answ = int(dig)
        count += 1 
        if ask[i] == '+':
            answ += int(dig)
            dig = ''
        elif ask[i] == '*' and ask[i+1].isdigit():
            answ *= int(dig)
            dig = ''
        elif ask[i] == '/' and ask[i+1].isdigit():
            answ /= int(dig)
            dig = ''
        elif ask[i] == '-' and ask[i+1].isdigit():
            answ -= int(dig)
            dig = ''
        i += 1
    print('Ответ:', answ)
    q = (input('\nНовый запрос? y/n: '))
    if q == 'n':
        prog += 1
