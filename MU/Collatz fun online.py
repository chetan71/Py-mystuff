# Write your code here :-)
def collatz(n):
    while n>1:
        print (n, end=' ')
        num = n %2
        if 0:
            n = n//2
        elif num == 1:
            n = 3*n +1
    print (1, end='')


n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)
