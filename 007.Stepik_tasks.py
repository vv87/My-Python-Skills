# -*- coding: utf-8 -*- #
while True:
    n = int(input())
    0 <= n <= 1000
    if (n % 100 == 11 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or
        n % 10 == 8 or n % 10 == 9 or n % 10 == 0 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14):
        print(str(n) + ' программистов')
    elif n == 1 or (n % 10 == 1 and n % 100 != 11):
        print(str(n) + ' программист')
    elif (n % 10 == 2 or 3 or 4):
        print(str(n) + ' программиста')
    else:
        print ('Введите целое число от 1 до 1000')

'''At the Institute of Bioinformatics, a robot is moving around the office.  Recently, students from a group of programmers wrote a program for him, according to which a robot, when it enters a room, counts the number of programmers in it and says it out loud: "n programmers".

 In order for it to sound right, for each n you need to use the correct ending of the word.

 Write a program that reads an integer n (nonnegative) from user input, outputs this number to the console along with the correct word “programmer”, so that the robot can communicate normally with people, for example: 1 programmer, 2 programmers, 5 programmers  .

 There may be a lot of programmers in the room.  Check that your program correctly handles all cases, at least up to 1000 people.

 Additional comment on the condition:
 Please note that the task is not as simple as it seems at first glance.  If your solution does not pass any test, it means that you have not considered any of the cases of input data (the number of programmers is 0≤n≤1000).  Be sure to check your decisions on additional values, and not just on those given in the statement of the task.

 Since the task is of increased complexity, manual decision code will not be checked.  If you encounter an error in the first four tests, check that you only use Russian characters for the answer.  In other cases, look for an error in the logic of the program.

 Sample Input 1:

 five
 Sample Output 1:

 5 programmers
 Sample Input 2:

 0
 Sample Output 2:

 0 programmers
 Sample Input 3:

 one
 Sample Output 3:

 1 programmer
 Sample Input 4:

 2
 Sample Output 4:

 2 programmers



В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000). Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.

Так как задание повышенной сложности, вручную код решений проверяться не будет. Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.

Sample Input 1:

5
Sample Output 1:

5 программистов
Sample Input 2:

0
Sample Output 2:

0 программистов
Sample Input 3:

1
Sample Output 3:

1 программист
Sample Input 4:

2
Sample Output 4:

2 программиста
'''
