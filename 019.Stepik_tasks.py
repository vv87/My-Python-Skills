"""Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9"""


n = int(input())
a = [[0] * n for y in range(n)]
i, j = 0, 0
k = 1
while k <= n**2:  
    a[i][j] = k
    
    if (i <= j + 1) and (i + j < n - 1):
        j += 1
    elif (i < j) and (i + j >= n - 1):
        i += 1
    elif (i >= j) and (i + j > n - 1):
        j -= 1
    else:
        i -= 1
    k += 1
for f in range(n):
    for h in range(n):
        print(a[f][h], end=' ')
    print()
