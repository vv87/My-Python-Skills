a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
	d += 1
print(d)

'''At the Institute of Bioinformatics, a competition is organized between informatics and biologists.  The winners of the competition will get a big and tasty cake.  In a team of biologists
 a
 man, and in the team of computer scientists -
 b
 person.

 It is necessary to cut the cake in advance so that it is possible to distribute the pieces of cake to any team that won the competition, and each participant of this team should get the same number of pieces of cake.  And since you do not want to cut the cake into too small pieces, you need to find the minimum suitable number.

 Write a program that helps to find this number.
 The program must read the size of the commands (two positive integers
 a
  and
 b
 , each number is entered on a separate line) and output the smallest number
 d
 which is divided into both of these numbers without remainder.

В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов 
a
человек, а в команде информатиков — 
b
человек.

Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число. 
Программа должна считывать размеры команд (два положительных целых числа 
a
 и 
b
, каждое число вводится на отдельной строке) и выводить наименьшее число 
d
, которое делится на оба этих числа без остатка.'''
