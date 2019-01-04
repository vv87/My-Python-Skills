n = int(input())
for n in range(n):
    print('*' * n)

while True:
    n = int(input())
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()
