while True:
    a = int(input())
    if a > 100:
        break
    elif a >= 10:
        print(a)
    else:
        continue

'''
Write a program that reads integers from the console, one number per line.

 For each entered number, check:
 if the number is less than 10, then skip this number;
 if the number is greater than 100, then stop reading the numbers;
 otherwise, output this number back to the console on a separate line.

 Sample Input 1:

 12
 four
 2
 58
 112
 Sample Output 1:

 12
 58
 Sample Input 2:

 101
 Sample Output 2:

 Sample Input 3:

 one
 2
 102
 Sample Output 3:

Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

Sample Input 1:

12
4
2
58
112
Sample Output 1:

12
58
Sample Input 2:

101
Sample Output 2:

Sample Input 3:

1
2
102
Sample Output 3:'''
