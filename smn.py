prog = 0
idig = 0
while prog == 0:
    ask = input('Введите желаемый запрос (без пробелов): \n')
    answ = 0
    for i in range(len(ask)):
        if i == 0:
            idig = i+2
            dig = ask[i]
        # elif ask[i].isdigit() or ask[i] == "+" or ask[i] == "*" or ask[i] == "/":
        elif ask[i].isdigit():
            dig += ask[i]
            idig += 1
        elif ask[i] == "+":
            answ += int(dig)
            dig = ""
        # elif ask[i].isdigit():
        #     answ += int(ask[i])
        elif ask[i] == "*" and ask[i+1].isdigit():
            answ *= int(dig)
            dig = ""
        elif ask[i] == "/" and ask[i+1].isdigit():
            answ /= int(dig)
            dig = ""
        elif ask[i] == '-' and ask[i+1].isdigit():
            answ -= int(dig)
            dig = ""
        i += 1
        idig += 1
    print('Ответ:', answ)
    q = (input('Новый запрос? y/n: '))
    if q == 'n':
        prog += 1
