# i = 0
# while i == 0:
ask = input('Введите желаемый запрос (без пробелов): \n')
answ = 0
for i in range(len(ask)):
    if ask[i].isdigit() or ask[i] == "+" or ask[i] == "*" or ask[i] == "/":
        if ask[i+1].isdigit():
            answ += int(ask[i+1])
        elif ask[i].isdigit():
            answ += int(ask[i+1])
        elif ask[i] == "*" and ask[i+1].isdigit():
            answ *= int(ask[i+1])
        elif ask[i] == "/" and ask[i+1].isdigit():
            answ /= int(ask[i+1])
    elif ask[i] == '-' and ask[i+2].isdigit():
        if ask[i+1].isdigit():
            answ -= int(ask[i+1])
print('Ответ:', answ)
