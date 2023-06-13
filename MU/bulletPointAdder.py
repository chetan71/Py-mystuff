import pyperclip

massage = pyperclip.paste()

TEXT = massage.split('\n')

#print(TEXT is tuple)
BaddedTEXT = []

for l in TEXT:
    print(l)

    BaddedTEXT.append(f'* {l}')
    print(BaddedTEXT)

TEXT = '\n'.join(BaddedTEXT)
print(TEXT)

pyperclip.copy(TEXT)
