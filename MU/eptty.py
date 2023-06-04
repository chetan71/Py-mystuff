# Write your code here :-)
spam = ['apples', 'bananas', 'tafu', 'cats']


def Lprinter(Rlists):
    V_collector = ''

    for i in range(len(Rlists)):
        print('we are adding index num:' , i)

        V_collector += Rlists[i]
        V_collector += ', '
        print(V_collector)

Lprinter(spam)
