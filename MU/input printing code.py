"""Write code that prints Hello if 1 is stored
in spam, prints Howdy if 2 is stored in spam,
and prints Greetings! if anything else is stored
in spam."""

spam = input()
while True:
    if spam == '1':
        print("Hello")
        break
    if spam == '2':
        print("Howdy")
        break
    else:
        print("Greetings!")
        break
