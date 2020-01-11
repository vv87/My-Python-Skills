"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть 
не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит 
самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
У вас есть неограниченное число попыток.
Время одной попытки: 5 mins"""


def update_dict(diction, string):
    for i in string.split():
        if i in diction:
            diction[i] += 1
            # print('yes')
        else:
            diction.update({i: 1})
            # print('no')


def find_max(diction):
    count = 0
    for i in diction:
        if count < diction[i]:
            count = diction[i]
    return count


def find_word(diction, maximum):
    lst = []
    for i in diction:
        if maximum == diction[i]:
            lst.append(i)
    lst.sort()
    return lst[0] + ' ' + str(maximum)


dic = {}
with open('dataset_3363_3.txt') as file:
    for string in file:
        string = string.strip().lower()
        update_dict(dic, string)
        # print(string)
        # print(dic)
print(find_word(dic, find_max(dic)))
# count = find_max(dic)
# print(count)
