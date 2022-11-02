import re

# 368791 % 4 = 3

def list_of_money_reachers(file):
    MY_GROUP = 'P3125'
    money_reachers = []
    for lines in file:
        if re.fullmatch(r'[А-ЯЁ](?:[а-яё]|-[А-ЯЁ](?:[а-яё]))+ ([А-ЯЁ]\.){2} [A-Z]\d+\s', lines):
            surname, initials, group = lines.split()
            if initials[0] != initials[2] or group != MY_GROUP:
                money_reachers.append(surname + ' ' + initials + ' ' + group)
    return money_reachers

for i in range(1,5+1):
    print('Ответ на тест №' + str(i))
    file = open('test' + str(i), encoding='UTF-8')
    l = list_of_money_reachers(file)
    for j in range(len(l)):
        print(l[j])
    print()