"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
Обработайте индивидуальный набор данных за отведённое время. """


import urllib.request

p = 'https://stepic.org/media/attachments/course67/3.6.3/'
n = '699991.txt'
f = True
while f:
    url = p+n
    webFile = urllib.request.urlopen(url)
    localFile = open(n, 'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()
    with open(n) as input_file:
        for line in input_file:
            if 'We' in line:
               f = False
            if not f:
                print(line.strip())
            if f:
                n = line
