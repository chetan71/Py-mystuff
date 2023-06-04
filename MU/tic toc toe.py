# Write your code here :-)
theboard = { 'top-l':'', 'top-m':'', 'top-r':'',
             'mid-l':'', 'mid-m':'', 'mid-r':'',
             'low-l':'', 'low-m':'', 'low-r':''}

def theboard_p(dic):
    print(dic['top-l'] + 'l' + dic['top-m'] + 'l' + dic['top-r'])
    print('--+--+--')
    print(dic['mid-l'] + 'l' + dic['mid-m'] + 'l' + dic['mid-r'])
    print('--+--+--')
    print(dic['low-l'] + 'l' + dic['low-m'] + 'l' + dic['low-r'])

theboard_p(theboard)

