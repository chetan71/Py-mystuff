
def collatz(number):
    try:
        num = number%2
        if num == 0:
            print(number // 2)
            return number // 2
        elif num == 1:
            print(3*number + 1)
            return 3*number + 1
    except ValueError:
        print ('Please! Enter Intergerr')
while True:
    number = int(input('Enter Number:'))
    print ('Sequence: ', end='')
    collatz(number)
