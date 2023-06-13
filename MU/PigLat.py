#English to Pig Latin

print('Enter the english word to translate into Pig Latin')
massage = input()

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin
for word in massage.split():
    #print(f'HERE word IS "{word}" IS PRINTING WHICH IS IN FOR LOOP')
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        #print('PRINTING 1ST WHILE CONDITION IS TRUE OR NOT:'+ str(not word[0].isalpha()))
        prefixNonLetters += word[0]
        #print(f'HERE prefixNonLetters "{prefixNonLetters}" IS PRINTING IN HIS LOOP')
        word = word[1:]
        #print(f'HERE word "{word}" IS PRINTING AFTER ADDING "WORD[1:]" IN IT.')
    if len(word) == 0:
        #print(f'HERE PREFIX IS "{prefixNonLetters}" IS PRINTING, WHICH IS USED IN ANOTHER LOOP')
        pigLatin.append(prefixNonLetters)
        continue

    # Seperate the non-letters at theend of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]
        #print(f'here SUFFIX IS PRINTING "{suffixNonLetters}" WITH ADDED VALUE')
        #print(f'here word IS PRINTING "{word}" AFTER SUFFIX')
    # Remember ifthe word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make theword lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants +'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back togethe into a single string:
print(' '.join(pigLatin))

