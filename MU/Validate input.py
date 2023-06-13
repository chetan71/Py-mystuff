#Validate Input Programme
while True:
    print('Please, Enter your Age:')
    resp = input('>')


    if resp.isdecimal():
        print(f' Your Age is : {resp}')
        break
    else:
        print('Please, enter only interger (not enven float)')



while True:
    print('Enter your password with combination of number and alphabate')
    pass1 = input('>')


    if pass1.isalnum():

        break
    else:

        print('Greate! Your password is strong')
