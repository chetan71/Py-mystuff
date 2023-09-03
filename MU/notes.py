# Write your code here :-)
V = '''Removing Values from Lists with del Statements-
        del spam[2]
Using for loops with lists
    for i in [2, 'apple', 'banana', 32, 'mango']:
        print(i)
The in and not in Operators
    'howdy' in list
    True
Multiple Assignment Trick
    Cat = ['fat', 'gray', 'loud']
    size, colour, voice = cat
Using the enumerate() Function with Lists
    >>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    >>> for index, item in enumerate(supplies):
    ...     print('Index ' + str(index) + ' in supplies is: ' + item)

    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flamethrowers
    Index 3 in supplies is: binders
Using the random.choice() and random.shuffle() Fuctions with Lists
    random.choice(pet)
Augmented Assignment Operators
    like - "+="
Finding a index in a list with the index() Method
    >>> spam = ['hello', 'hi', 'howdy', 'heyas']
    >>> spam.index('hello')
    0
    >>> spam.index('heyas')
    3
    >>> spam.index('howdy howdy howdy')
    Traceback (most recent call last):
        File "<pyshell#31>", line 1, in <module>
        spam.index('howdy howdy howdy')
    ValueError: 'howdy howdy howdy' is not in list
Removing Values from Lists with the remove() Method
    >spam = ['cat', 'bat', 'rat', 'elephant']
    >spam.remove('bat')
    >spam
    ['cat', 'rat', elephant']

Sorting the Values in a List with the sort() Method
    >>> spam = [2, 5, 3.14, 1, -7]
    >>> spam.sort()
    >>> spam
    [-7, 1, 2, 3.14, 5]
    >>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    >>> spam.sort()
    >>> spam
        ['ants', 'badgers', 'cats', 'dogs', 'elephants']

Reversing the Values in a List with the reverse() Method
    >>> spam = ['cat', 'dog', 'moose']
    >>> spam.reverse()
    >>> spam
        ['moose', 'dog', 'cat']

Converting Types with the list() and tuple() Functions
    >>> tuple(['cat', 'dog', 5])
    ('cat', 'dog', 5)
    >>> list(('cat', 'dog', 5))
    ['cat', 'dog', 5]
    >>> list('hello')
    ['h', 'e', 'l', 'l', 'o']

The copy Module’s copy() and deepcopy() Functions
    >>> import copy
    >>> spam = ['A', 'B', 'C', 'D']
    >>> id(spam)
    44684232
    >>> cheese = copy.copy(spam)
    >>> id(cheese) # cheese is a different list with different identity.
    44685832
    >>> cheese[1] = 42
    >>> spam
    ['A', 'B', 'C', 'D']
    >>> cheese
    ['A', 42, 'C', 'D']

The keys(), values(), and items() Methods
    >>> spam = {'color': 'red', 'age': 42}
    >>> for v in spam.values():
    ...     print(v)

    red
    42
    KEYS() FUNCTION
    >>> for k in spam.keys():
    ...     print(k)

    color
    age
    >>> for i in spam.items():
    ...     print(i)

    ('color', 'red')
    ('age', 42)
    ITEMS() FUNCTION
    >>> spam = {'color': 'red', 'age': 42}
    >>> for k, v in spam.items():
    ...     print('Key: ' + k + ' Value: ' + str(v))

    Key: age Value: 42
    Key: color Value: red




'''
print(v)
